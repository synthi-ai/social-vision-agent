"""Writer agent — creates multi-platform copy from the calendar and product spotlights.

Generates the actual post text, hashtags, and CTA for each planned post,
respecting platform-specific constraints and tone guidelines.
Uses loaded skills (social-media-writing, viral-hooks, hashtag-strategy, etc.)
for expert-level content patterns.
"""

from __future__ import annotations

from langchain_core.prompts import ChatPromptTemplate

from src.state import PostDraft
from src.utils.json_parser import parse_json
from src.utils.llm_factory import get_llm_with_fallback
from src.skills.loader import get_skill_registry

SYSTEM_PROMPT = """\
You are the **Content Writer** for a tech startup's social media team.

Your role:
- Write compelling, authentic social media posts
- Match the tone and constraints of each platform
- Use the hook idea as inspiration (don't copy it literally)
- Include relevant hashtags (respect platform limits)
- Include a clear call-to-action (CTA)
- For product posts, weave in the product spotlight naturally — no hard sell
- Apply the skill instructions below for expert-level writing patterns

Writing style:
- Tech-savvy but accessible
- Concrete examples over abstract claims
- Short sentences, strong verbs
- No corporate jargon or buzzword soup
- Authentic founder/builder voice

{skill_instructions}

Output ONLY valid JSON array:
[
  {{
    "platform": "<platform>",
    "theme": "<theme>",
    "product_focus": "<product_id or null>",
    "day": "<day>",
    "text": "<the full post text>",
    "hashtags": ["tag1", "tag2"],
    "cta": "<call to action text>"
  }}
]
"""

HUMAN_PROMPT = """\
Write posts for this week's calendar.

Company vision (for tone alignment):
{vision_summary}

Platform rules:
{platform_rules}

Content calendar:
{calendar_json}

Product spotlights (use for product-themed posts):
{spotlights_json}

Write ALL {post_count} posts. Respond ONLY with a valid JSON array.
"""


def build_writer_chain():
    """Build the writer LLM chain with skill injection."""
    llm = get_llm_with_fallback(temperature=0.85, max_tokens=8192)

    registry = get_skill_registry()
    skill_instructions = registry.get_skills_for_agent("writer")

    prompt = ChatPromptTemplate.from_messages([
        ("system", SYSTEM_PROMPT),
        ("human", HUMAN_PROMPT),
    ])
    chain = prompt.partial(skill_instructions=skill_instructions) | llm
    return chain


def parse_drafts(raw_output: str) -> list[PostDraft]:
    """Parse LLM output into PostDraft objects."""
    items = parse_json(raw_output, default=[])

    drafts = []
    for item in items:
        drafts.append(PostDraft(
            platform=item.get("platform", "linkedin"),
            theme=item.get("theme", "vision"),
            product_focus=item.get("product_focus"),
            day=item.get("day", ""),
            text=item.get("text", ""),
            hashtags=item.get("hashtags", []),
            cta=item.get("cta", ""),
            status="drafted",
        ))
    return drafts