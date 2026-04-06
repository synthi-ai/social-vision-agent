"""Skill loader and registry — DeerFlow-inspired SKILL.md pattern.

Skills are Markdown files with YAML frontmatter that define specialized
capabilities agents can use. The system discovers skills from:
  - skills/public/   (bundled, versioned)
  - skills/custom/   (user-created, not tracked in git)

Each skill folder must contain a SKILL.md file. The frontmatter provides
metadata (name, description) for discovery. The body provides instructions
injected into agent prompts when the skill is activated.

Progressive disclosure: at startup, only name+description are loaded.
Full instructions are loaded on-demand when an agent needs the skill.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional

import structlog
import yaml

from config.settings import BASE_DIR

logger = structlog.get_logger(__name__)

SKILLS_DIRS = [
    BASE_DIR / "skills" / "public",
    BASE_DIR / "skills" / "custom",
]

# Regex to extract YAML frontmatter
_FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n?(.*)", re.DOTALL)


@dataclass
class Skill:
    """A loaded skill with metadata and instructions."""

    name: str
    description: str
    body: str  # Full Markdown instructions
    path: Path
    license: Optional[str] = None
    allowed_tools: list[str] = field(default_factory=list)
    metadata: dict[str, str] = field(default_factory=dict)

    @property
    def summary(self) -> str:
        """Short summary for prompt injection (name + description only)."""
        return f"- **{self.name}**: {self.description}"


class SkillRegistry:
    """Central registry for all discovered skills.

    Provides:
    - Discovery: scan skills directories for SKILL.md files
    - Lookup: find skills by name or keyword matching
    - Injection: generate prompt text with relevant skill instructions
    """

    def __init__(self) -> None:
        self._skills: dict[str, Skill] = {}

    def discover(self, extra_dirs: list[Path] | None = None) -> int:
        """Scan skill directories and register all valid skills.

        Args:
            extra_dirs: Additional directories to scan beyond the defaults.

        Returns:
            Number of skills discovered.
        """
        dirs = SKILLS_DIRS + (extra_dirs or [])
        count = 0

        for skills_dir in dirs:
            if not skills_dir.exists():
                continue

            for skill_folder in sorted(skills_dir.iterdir()):
                if not skill_folder.is_dir():
                    continue

                skill_file = skill_folder / "SKILL.md"
                if not skill_file.exists():
                    continue

                skill = _parse_skill_file(skill_file)
                if skill:
                    self._skills[skill.name] = skill
                    count += 1

        logger.info("skills.discovered", count=count, names=list(self._skills.keys()))
        return count

    @property
    def all_skills(self) -> list[Skill]:
        """All registered skills."""
        return list(self._skills.values())

    def get(self, name: str) -> Optional[Skill]:
        """Get a skill by exact name."""
        return self._skills.get(name)

    def find(self, keyword: str) -> list[Skill]:
        """Find skills matching a keyword in name or description."""
        keyword_lower = keyword.lower()
        return [
            s for s in self._skills.values()
            if keyword_lower in s.name.lower() or keyword_lower in s.description.lower()
        ]

    def get_catalog_prompt(self) -> str:
        """Generate a catalog of all skills for system prompt injection.

        This is the 'progressive disclosure' first stage:
        agents see the list of available skills and their descriptions,
        then request full instructions for relevant ones.
        """
        if not self._skills:
            return "No skills available."

        lines = ["## Available Skills\n"]
        for skill in self._skills.values():
            lines.append(skill.summary)
        return "\n".join(lines)

    def get_skill_instructions(self, *names: str) -> str:
        """Get full instructions for specific skills.

        This is the second stage of progressive disclosure:
        load complete SKILL.md body for activated skills.

        Args:
            names: Skill names to load instructions for.

        Returns:
            Combined Markdown instructions for all requested skills.
        """
        sections = []
        for name in names:
            skill = self._skills.get(name)
            if skill:
                sections.append(f"# Skill: {skill.name}\n\n{skill.body}")
            else:
                sections.append(f"# Skill: {name}\n\n[Skill not found]")
        return "\n\n---\n\n".join(sections)

    def get_skills_for_agent(self, agent_role: str) -> str:
        """Get relevant skill instructions for a specific agent role.

        Matches skills to agents based on metadata tags or name patterns.

        Args:
            agent_role: The agent role (strategist, writer, optimizer, etc.)

        Returns:
            Combined instructions for matching skills.
        """
        relevant = []
        for skill in self._skills.values():
            target_agents = skill.metadata.get("agents", "").split(",")
            target_agents = [a.strip() for a in target_agents if a.strip()]

            if not target_agents or agent_role in target_agents:
                relevant.append(skill)

        if not relevant:
            return ""

        sections = []
        for skill in relevant:
            sections.append(f"### Skill: {skill.name}\n{skill.body}")
        return "\n\n".join(sections)


def _parse_skill_file(path: Path) -> Optional[Skill]:
    """Parse a SKILL.md file into a Skill object.

    Args:
        path: Path to the SKILL.md file.

    Returns:
        Parsed Skill or None if invalid.
    """
    try:
        content = path.read_text(encoding="utf-8")
    except Exception as e:
        logger.warning("skills.read_error", path=str(path), error=str(e))
        return None

    match = _FRONTMATTER_RE.match(content)
    if not match:
        logger.warning("skills.no_frontmatter", path=str(path))
        return None

    frontmatter_str, body = match.groups()

    try:
        frontmatter = yaml.safe_load(frontmatter_str)
    except yaml.YAMLError as e:
        logger.warning("skills.yaml_error", path=str(path), error=str(e))
        return None

    if not isinstance(frontmatter, dict):
        return None

    name = frontmatter.get("name")
    description = frontmatter.get("description")

    if not name or not description:
        logger.warning("skills.missing_fields", path=str(path))
        return None

    return Skill(
        name=name,
        description=description,
        body=body.strip(),
        path=path,
        license=frontmatter.get("license"),
        allowed_tools=frontmatter.get("allowed-tools", []),
        metadata=frontmatter.get("metadata", {}),
    )


# ── Global registry singleton ────────────────────────────────

_registry: Optional[SkillRegistry] = None


def get_skill_registry() -> SkillRegistry:
    """Get or initialize the global skill registry."""
    global _registry
    if _registry is None:
        _registry = SkillRegistry()
        _registry.discover()
    return _registry
