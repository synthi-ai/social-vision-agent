"""Visual Prompter agent — generates image prompts (and optionally images) for each post.

Creates detailed visual descriptions that can be sent to Grok Imagine or
any image generation API. Ensures visual consistency with brand identity.
"""

from __future__ import annotations

from langchain_core.prompts import ChatPromptTemplate

from src.state import PostDraft
from src.utils.json_parser import parse_json
from src.utils.llm_factory import get_llm_with_fallback
from src.skills.loader import get_skill_registry

SYSTEM_PROMPT = """\
You are the **Visual Director** for a tech startup's social media team.

Your role:
- Create detailed image generation prompts for each social media post
- Ensure visual consistency with a modern tech brand identity
- Adapt visual style to each platform's best practices
- Use clean, professional aesthetics with a tech/developer vibe

Visual guidelines:
- LinkedIn: professional, clean infographics or abstract tech visuals
- X/Twitter: eye-catching, bold typography overlays, memes when appropriate
- TikTok: vibrant, dynamic, text overlays, vertical format (9:16)
- Facebook: warm, community-focused, relatable imagery

{skill_instructions}

Output ONLY valid JSON array:
[
  {{
    "platform": "<platform>",
    "day": "<day>",
    "visual_prompt": "<detailed image generation prompt, 2-3 sentences>",
    "style_notes": "<brief style direction>"
  }}
]
"""

HUMAN_PROMPT = """\
Generate visual prompts for these posts:

{drafts_json}

Create one visual prompt per post ({draft_count} total).
Respond ONLY with a valid JSON array.
"""


def build_visual_chain():
    """Build the visual prompter LLM chain with skill injection."""
    llm = get_llm_with_fallback(temperature=0.9)

    registry = get_skill_registry()
    skill_instructions = registry.get_skills_for_agent("visual")

    prompt = ChatPromptTemplate.from_messages([
        ("system", SYSTEM_PROMPT),
        ("human", HUMAN_PROMPT),
    ])
    chain = prompt.partial(skill_instructions=skill_instructions) | llm
    return chain


def parse_visual_prompts(raw_output: str) -> list[dict]:
    """Parse LLM output into visual prompt dicts."""
    return parse_json(raw_output, default=[])


def merge_visual_into_drafts(
    drafts: list[PostDraft], visuals: list[dict]
) -> list[PostDraft]:
    """Merge visual prompts back into the corresponding drafts."""
    visual_map: dict[tuple[str, str], dict] = {}
    for v in visuals:
        key = (v.get("platform", ""), v.get("day", ""))
        visual_map[key] = v

    updated = []
    for draft in drafts:
        key = (draft.platform, draft.day)
        if key in visual_map:
            draft.visual_prompt = visual_map[key].get("visual_prompt", "")
        updated.append(draft)
    return updated