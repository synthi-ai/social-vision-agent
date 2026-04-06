"""Weekly brief tool — loads the externalized weekly configuration."""

from __future__ import annotations

from pathlib import Path
from typing import Optional

import yaml
from langchain_core.tools import tool
from pydantic import BaseModel, Field


class CampaignConfig(BaseModel):
    """A single product/campaign to promote this week."""

    product_id: str
    name: str
    priority: str = "medium"
    posts_per_platform: int = 1
    themes: list[str] = Field(default_factory=list)
    key_messages: list[str] = Field(default_factory=list)
    image_urls: dict[str, str] = Field(default_factory=dict)


class VisionPostsConfig(BaseModel):
    """Vision/thought-leadership posts configuration."""

    posts_per_platform: int = 1
    themes: list[str] = Field(default_factory=list)
    topics: list[str] = Field(default_factory=list)
    image_urls: dict[str, str] = Field(default_factory=dict)


class WeeklyBrief(BaseModel):
    """Complete weekly brief parsed from YAML."""

    platforms: list[str] = Field(default_factory=lambda: ["linkedin", "x", "tiktok", "facebook"])
    default_posts_per_platform: int = 2
    campaigns: list[CampaignConfig] = Field(default_factory=list)
    vision_posts: Optional[VisionPostsConfig] = None
    research_topics: list[str] = Field(default_factory=list)

    @property
    def total_posts(self) -> int:
        """Calculate total number of posts to generate."""
        total = 0
        for campaign in self.campaigns:
            total += campaign.posts_per_platform * len(self.platforms)
        if self.vision_posts:
            total += self.vision_posts.posts_per_platform * len(self.platforms)
        return total


_BRIEF_PATH = Path(__file__).resolve().parent.parent.parent / "config" / "weekly_brief.yaml"


def load_weekly_brief(path: Path | None = None) -> WeeklyBrief:
    """Load and parse the weekly brief from YAML.

    Args:
        path: Path to the YAML file. Defaults to config/weekly_brief.yaml.

    Returns:
        Parsed WeeklyBrief object.
    """
    path = path or _BRIEF_PATH
    if not path.exists():
        return WeeklyBrief()

    with open(path, encoding="utf-8") as f:
        data = yaml.safe_load(f) or {}

    campaigns = []
    for c in data.get("campaigns", []):
        campaigns.append(CampaignConfig(**c))

    vision = None
    if "vision_posts" in data:
        vision = VisionPostsConfig(**data["vision_posts"])

    return WeeklyBrief(
        platforms=data.get("platforms", ["linkedin", "x", "tiktok", "facebook"]),
        default_posts_per_platform=data.get("default_posts_per_platform", 2),
        campaigns=campaigns,
        vision_posts=vision,
        research_topics=data.get("research_topics", []),
    )


@tool
def get_weekly_brief() -> str:
    """Load the weekly content brief configuration.

    Returns the full brief including products to promote, image URLs,
    post counts, themes, and research topics for this week.
    """
    brief = load_weekly_brief()
    return yaml.dump(
        brief.model_dump(exclude_none=True),
        allow_unicode=True,
        sort_keys=False,
        default_flow_style=False,
    )


@tool
def get_campaign_image_url(product_id: str, platform: str) -> str:
    """Get the image URL for a specific product and platform.

    Args:
        product_id: The product/campaign ID.
        platform: The target platform (linkedin, x, tiktok, facebook).

    Returns:
        The image URL or a message if not found.
    """
    brief = load_weekly_brief()
    for campaign in brief.campaigns:
        if campaign.product_id == product_id:
            url = campaign.image_urls.get(platform.lower())
            if url:
                return url
            return f"No image URL for {product_id} on {platform}"

    if brief.vision_posts:
        url = brief.vision_posts.image_urls.get(platform.lower())
        if url:
            return url

    return f"Campaign '{product_id}' not found in weekly brief"