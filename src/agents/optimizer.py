"""Optimizer agent — adapts each draft to platform-specific constraints.

Checks character limits, hashtag counts, CTA style, and applies
final polish. Ensures every post is platform-compliant before approval.
"""

from __future__ import annotations

from langchain_core.prompts import ChatPromptTemplate

from src.state import PostDraft
from src.utils.json_parser import parse_json
from src.utils.llm_factory import get_llm_with_fallback
from src.skills.loader import get_skill_registry

SYSTEM_PROMPT = """\
You are the **Content Optimizer** for a tech startup's social media team.

Your role:
- Review each draft post and optimize it for its target platform
- Enforce character limits strictly
- Adjust tone to match platform conventions
- Improve hooks (first line must grab attention)
- Verify hashtag count is within platform limits
- Ensure CTA is natural and compelling
- Apply skill instructions below for expert optimization

{skill_instructions}
- Fix any grammar or awkward phrasing

Platform constraints:
- LinkedIn: max 3000 chars, optimal 1300-1800, max 5 hashtags
- X/Twitter: max 280 chars (suggest thread if longer), max 3 hashtags
- TikTok: max 2200 chars caption, optimal 100-150, max 8 hashtags
- Facebook: optimal 40-80 words, max 5 hashtags

Output ONLY valid JSON array:
[
  {{
    "platform": "<platform>",
    "day": "<day>",
    "optimized_text": "<the optimized post text>",
    "hashtags": ["tag1", "tag2"],
    "cta": "<optimized CTA>",
    "optimization_notes": "<what was changed and why>"
  }}
]
"""

HUMAN_PROMPT = """\
Optimize these draft posts for their target platforms:

Platform rules:
{platform_rules}

Drafts to optimize:
{drafts_json}

Optimize ALL {draft_count} posts. Respond ONLY with a valid JSON array.
"""


def build_optimizer_chain():
    """Build the optimizer LLM chain with skill injection."""
    llm = get_llm_with_fallback(temperature=0.4)

    registry = get_skill_registry()
    skill_instructions = registry.get_skills_for_agent("optimizer")

    prompt = ChatPromptTemplate.from_messages([
        ("system", SYSTEM_PROMPT),
        ("human", HUMAN_PROMPT),
    ])
    chain = prompt.partial(skill_instructions=skill_instructions) | llm
    return chain


def parse_optimized(raw_output: str) -> list[dict]:
    """Parse LLM output into optimization dicts."""
    return parse_json(raw_output, default=[])


def merge_optimized_into_drafts(
    drafts: list[PostDraft], optimized: list[dict]
) -> list[PostDraft]:
    """Merge optimized content back into drafts."""
    opt_map: dict[tuple[str, str], dict] = {}
    for o in optimized:
        key = (o.get("platform", ""), o.get("day", ""))
        opt_map[key] = o

    updated = []
    for draft in drafts:
        key = (draft.platform, draft.day)
        if key in opt_map:
            opt = opt_map[key]
            draft.optimized_text = opt.get("optimized_text", draft.text)
            draft.hashtags = opt.get("hashtags", draft.hashtags)
            draft.cta = opt.get("cta", draft.cta)
            draft.optimization_notes = opt.get("optimization_notes", "")
            draft.status = "optimized"
        updated.append(draft)
    return updated