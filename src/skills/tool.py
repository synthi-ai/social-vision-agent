"""Skill access tool — allows agents to query and load skills at runtime."""

from __future__ import annotations

from langchain_core.tools import tool

from src.skills.loader import get_skill_registry


@tool
def list_available_skills() -> str:
    """List all available skills with their names and descriptions.

    Returns a catalog of skills that can be loaded for detailed instructions.
    """
    registry = get_skill_registry()
    return registry.get_catalog_prompt()


@tool
def load_skill(skill_name: str) -> str:
    """Load the full instructions for a specific skill by name.

    Args:
        skill_name: The skill name (e.g. 'viral-hooks', 'hashtag-strategy').

    Returns:
        Complete skill instructions in Markdown format.
    """
    registry = get_skill_registry()
    skill = registry.get(skill_name)
    if skill:
        return f"# Skill: {skill.name}\n\n{skill.body}"
    return f"Skill '{skill_name}' not found. Use list_available_skills() to see available skills."