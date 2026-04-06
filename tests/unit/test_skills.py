"""Tests for the skills loader and registry."""

from pathlib import Path

from src.skills.loader import SkillRegistry, _parse_skill_file, get_skill_registry


def test_parse_valid_skill(tmp_path: Path):
    """Parse a valid SKILL.md file."""
    skill_dir = tmp_path / "test-skill"
    skill_dir.mkdir()
    skill_file = skill_dir / "SKILL.md"
    skill_file.write_text(
        "---\n"
        "name: test-skill\n"
        "description: A test skill for unit testing.\n"
        "license: MIT\n"
        "metadata:\n"
        "  agents: writer,optimizer\n"
        "  category: test\n"
        "---\n"
        "\n"
        "# Test Skill\n"
        "\n"
        "These are the skill instructions.\n"
        "\n"
        "## Guidelines\n"
        "- Be awesome\n"
    )
    skill = _parse_skill_file(skill_file)
    assert skill is not None
    assert skill.name == "test-skill"
    assert skill.description == "A test skill for unit testing."
    assert skill.license == "MIT"
    assert skill.metadata["agents"] == "writer,optimizer"
    assert "Test Skill" in skill.body
    assert "Be awesome" in skill.body


def test_parse_missing_name(tmp_path: Path):
    """Reject SKILL.md without name field."""
    skill_file = tmp_path / "SKILL.md"
    skill_file.write_text("---\ndescription: No name here\n---\nBody text\n")
    skill = _parse_skill_file(skill_file)
    assert skill is None


def test_parse_no_frontmatter(tmp_path: Path):
    """Reject file without YAML frontmatter."""
    skill_file = tmp_path / "SKILL.md"
    skill_file.write_text("# Just a regular markdown file\n\nNo frontmatter here.\n")
    skill = _parse_skill_file(skill_file)
    assert skill is None


def test_registry_discover():
    """Discover bundled public skills."""
    registry = SkillRegistry()
    count = registry.discover()
    assert count >= 7  # We have 7 public skills
    assert registry.get("viral-hooks") is not None
    assert registry.get("social-media-writing") is not None
    assert registry.get("hashtag-strategy") is not None


def test_registry_find():
    """Find skills by keyword."""
    registry = SkillRegistry()
    registry.discover()

    results = registry.find("hook")
    assert len(results) >= 1
    assert any(s.name == "viral-hooks" for s in results)


def test_registry_catalog_prompt():
    """Generate a catalog prompt for system injection."""
    registry = SkillRegistry()
    registry.discover()

    catalog = registry.get_catalog_prompt()
    assert "Available Skills" in catalog
    assert "viral-hooks" in catalog
    assert "social-media-writing" in catalog


def test_registry_skills_for_agent():
    """Get relevant skills for a specific agent role."""
    registry = SkillRegistry()
    registry.discover()

    writer_skills = registry.get_skills_for_agent("writer")
    assert "social-media-writing" in writer_skills.lower() or "Social Media Writing" in writer_skills

    visual_skills = registry.get_skills_for_agent("visual")
    assert "visual-branding" in visual_skills.lower() or "Visual Branding" in visual_skills


def test_skill_summary():
    """Test skill summary format."""
    registry = SkillRegistry()
    registry.discover()
    skill = registry.get("viral-hooks")
    assert skill is not None
    summary = skill.summary
    assert "viral-hooks" in summary
    assert "scroll-stopping" in summary.lower() or "hooks" in summary.lower()


def test_global_registry_singleton():
    """Ensure get_skill_registry returns the same instance."""
    r1 = get_skill_registry()
    r2 = get_skill_registry()
    assert r1 is r2