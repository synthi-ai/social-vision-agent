"""Strategist agent — generates the weekly content calendar.

Reads the weekly brief (externalized config) to dynamically determine
how many posts to generate per product, per platform. Supports multiple
products/campaigns per week with configurable post counts.
"""

from __future__ import annotations

from langchain_core.prompts import ChatPromptTemplate

from src.state import ContentCalendar, PlannedPost
from src.utils.json_parser import parse_json
from src.utils.llm_factory import get_llm_with_fallback
from src.skills.loader import get_skill_registry

SYSTEM_PROMPT = """\
You are the **Content Strategist** for a tech startup's social media team.

Your role:
- Create a weekly editorial calendar based on the provided brief
- Respect the exact number of posts requested per campaign per platform
- Balance themes as specified (product, vision, engagement, education)
- Vary formats per platform best practices
- Assign each post a specific day (Monday–Friday), spreading evenly
- For product posts, always include the product_id
- Incorporate research insights when provided
- Apply skill instructions below for expert strategy

{skill_instructions}

Output ONLY valid JSON matching this schema:
{{
  "week": "<YYYY-WNN>",
  "posts": [
    {{
      "platform": "linkedin|x|tiktok|facebook",
      "theme": "vision|product|engagement|education",
      "product_id": "<product_id or null>",
      "hook_idea": "<one-line hook idea>",
      "format": "<format type>",
      "day": "monday|tuesday|wednesday|thursday|friday"
    }}
  ]
}}
"""

HUMAN_PROMPT = """\
Week: {current_week}

Company Vision:
{vision_summary}

Weekly Brief (campaigns, post counts, themes):
{weekly_brief}

Web Research Insights:
{research_insights}

Generate the weekly content calendar with exactly {total_posts} posts as specified in the brief.
Respond ONLY with valid JSON, no markdown fences.
"""


def build_strategist_chain():
    """Build the strategist LLM chain with skill injection."""
    llm = get_llm_with_fallback(temperature=0.8, max_tokens=8192)

    registry = get_skill_registry()
    skill_instructions = registry.get_skills_for_agent("strategist")

    prompt = ChatPromptTemplate.from_messages([
        ("system", SYSTEM_PROMPT),
        ("human", HUMAN_PROMPT),
    ])
    chain = prompt.partial(skill_instructions=skill_instructions) | llm
    return chain


def parse_calendar(raw_output: str, week: str) -> ContentCalendar:
    """Parse the LLM output into a ContentCalendar."""
    data = parse_json(raw_output, default={"posts": []})

    posts = []
    for p in data.get("posts", []):
        posts.append(PlannedPost(
            platform=p.get("platform", "linkedin"),
            theme=p.get("theme", "vision"),
            product_id=p.get("product_id"),
            hook_idea=p.get("hook_idea", ""),
            format=p.get("format", "text_plus_image"),
            day=p.get("day", ""),
        ))

    return ContentCalendar(week=data.get("week", week), posts=posts)