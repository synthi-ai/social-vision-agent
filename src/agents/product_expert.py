"""Product Expert agent — enriches planned posts with product details.

For each post with a product_id in the calendar, fetches the product info
and builds a spotlight summary the Writer can use.
"""

from __future__ import annotations

from langchain_core.prompts import ChatPromptTemplate

from src.state import ContentCalendar
from src.tools.product_knowledge import get_product_info, list_products
from src.utils.json_parser import parse_json
from src.utils.llm_factory import get_llm_with_fallback

SYSTEM_PROMPT = """\
You are the **Product Expert** for a tech startup's social media team.

Your role:
- For each product-focused post, create a concise product spotlight
- Highlight the most compelling feature for the target platform audience
- Include: key benefit, differentiator, and a suggested angle for the writer
- Keep each spotlight to 3-5 bullet points max

Output valid JSON:
{{
  "<product_id>": {{
    "name": "<product name>",
    "key_benefit": "<main value proposition>",
    "differentiator": "<what makes it unique>",
    "suggested_angle": "<content angle for the writer>",
    "proof_point": "<metric, testimonial, or concrete example>"
  }}
}}
"""

HUMAN_PROMPT = """\
The following products need spotlight summaries for this week's content:

Product IDs needed: {product_ids}

Product catalog data:
{product_details}

Generate a spotlight summary for each product. Respond ONLY with valid JSON.
"""


def build_product_expert_chain():
    """Build the product expert LLM chain."""
    llm = get_llm_with_fallback(temperature=0.5)
    prompt = ChatPromptTemplate.from_messages([
        ("system", SYSTEM_PROMPT),
        ("human", HUMAN_PROMPT),
    ])
    return prompt | llm


def extract_product_ids(calendar: ContentCalendar) -> list[str]:
    """Extract unique product IDs from the calendar."""
    ids = set()
    for post in calendar.posts:
        if post.product_id:
            ids.add(post.product_id)
    return sorted(ids)


def parse_spotlights(raw_output: str) -> dict[str, dict]:
    """Parse LLM output into product spotlight dict."""
    return parse_json(raw_output, default={})