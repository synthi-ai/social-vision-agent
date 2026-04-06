"""Platform rules tool — reads platform constraints from platforms.yaml."""

from __future__ import annotations

from pathlib import Path

import yaml
from langchain_core.tools import tool

from config.settings import settings

_PLATFORMS_PATH = Path(__file__).resolve().parent.parent.parent / "config" / "platforms.yaml"


def _load_platform_rules() -> dict:
    """Load all platform rules from YAML."""
    if not _PLATFORMS_PATH.exists():
        return {}
    with open(_PLATFORMS_PATH, encoding="utf-8") as f:
        return yaml.safe_load(f) or {}


@tool
def get_platform_rules(platform: str) -> str:
    """Get posting rules and best practices for a specific social media platform.

    Args:
        platform: One of 'linkedin', 'x', 'tiktok', 'facebook'.

    Returns:
        YAML-formatted rules for the platform, or error if not found.
    """
    rules = _load_platform_rules()
    platform_key = platform.lower().strip()

    if platform_key in rules:
        return yaml.dump(
            {platform_key: rules[platform_key]},
            allow_unicode=True,
            sort_keys=False,
            default_flow_style=False,
        )

    available = list(rules.keys())
    return f"Platform '{platform}' not found. Available: {', '.join(available)}"


@tool
def get_all_platform_rules() -> str:
    """Get posting rules for all supported platforms at once.

    Returns:
        YAML-formatted rules for all platforms.
    """
    rules = _load_platform_rules()
    if not rules:
        return "No platform rules found in config/platforms.yaml"
    return yaml.dump(rules, allow_unicode=True, sort_keys=False, default_flow_style=False)