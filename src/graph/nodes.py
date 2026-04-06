"""Graph nodes — each function is a LangGraph node that reads/writes AgentState.

Pattern inspired by DeerFlow: each node is a pure function that takes state,
calls an agent chain, and returns a partial state update. LangGraph merges
the update into the global state and checkpoints automatically.

Key patterns:
- Error recovery: each node catches exceptions and writes to state.error
- Structured logging at entry/exit of each node
- PostgreSQL persistence after approval and publishing
- Weekly brief drives dynamic post count and campaigns
- Web search for content enrichment
- Image URLs from config (not generated)
"""

from __future__ import annotations

import json

import structlog
import yaml
from langchain_core.messages import AIMessage

from config.settings import settings
from src.state import AgentState, PostDraft
from src.agents.strategist import build_strategist_chain, parse_calendar
from src.agents.product_expert import (
    build_product_expert_chain,
    extract_product_ids,
    parse_spotlights,
)
from src.agents.writer import build_writer_chain, parse_drafts
from src.agents.visual import build_visual_chain, parse_visual_prompts, merge_visual_into_drafts
from src.agents.optimizer import (
    build_optimizer_chain,
    parse_optimized,
    merge_optimized_into_drafts,
)
from src.agents.publisher import export_batch_markdown, export_batch_json, build_report
from src.tools.product_knowledge import get_product_info, list_products
from src.tools.platform_rules import get_all_platform_rules
from src.tools.weekly_brief import load_weekly_brief, get_campaign_image_url
from src.tools.web_search import web_search, research_topic
from src.db.postgres import save_weekly_batch, save_all_posts

logger = structlog.get_logger(__name__)


def _assign_image_urls(drafts: list[PostDraft]) -> list[PostDraft]:
    """Assign image URLs from the weekly brief config to each draft."""
    brief = load_weekly_brief()

    for draft in drafts:
        if draft.image_path:
            continue

        # Try campaign images first
        if draft.product_focus:
            for campaign in brief.campaigns:
                if campaign.product_id == draft.product_focus:
                    url = campaign.image_urls.get(draft.platform)
                    if url:
                        draft.image_path = url
                    break

        # Try vision images
        if not draft.image_path and brief.vision_posts:
            url = brief.vision_posts.image_urls.get(draft.platform)
            if url:
                draft.image_path = url

    return drafts


# ── Node 0: Researcher (web search enrichment) ──────────────


def researcher_node(state: AgentState) -> dict:
    """Research current trends and topics from the web to enrich content."""
    logger.info("node.researcher.start")

    try:
        brief = load_weekly_brief()
        topics = brief.research_topics

        if not topics:
            logger.info("node.researcher.skip", reason="no research topics in brief")
            return {
                "research_insights": "",
                "messages": [AIMessage(content="[Researcher] No research topics configured")],
            }

        all_insights = []
        for topic in topics:
            result = research_topic.invoke({"topic": topic})
            if not result.startswith("No research"):
                all_insights.append(f"## {topic}\n{result}")

        insights = "\n\n".join(all_insights) if all_insights else "No insights found."
        logger.info("node.researcher.done", topic_count=len(topics), insight_length=len(insights))

        return {
            "research_insights": insights,
            "messages": [AIMessage(content=f"[Researcher] Researched {len(topics)} topics")],
        }
    except Exception as e:
        logger.error("node.researcher.error", error=str(e))
        return {"research_insights": "", "error": f"Researcher failed: {e}"}


# ── Node 1: Strategist ──────────────────────────────────────


def strategist_node(state: AgentState) -> dict:
    """Generate the weekly content calendar from the weekly brief."""
    logger.info("node.strategist.start", week=state["current_week"])

    try:
        brief = load_weekly_brief()
        brief_yaml = yaml.dump(
            brief.model_dump(exclude_none=True),
            allow_unicode=True,
            sort_keys=False,
        )
        total_posts = brief.total_posts

        chain = build_strategist_chain()
        result = chain.invoke({
            "current_week": state["current_week"],
            "vision_summary": state["vision_summary"],
            "weekly_brief": brief_yaml,
            "research_insights": state.get("research_insights", "None available"),
            "total_posts": total_posts,
        })

        raw = result.content if hasattr(result, "content") else str(result)
        calendar = parse_calendar(raw, state["current_week"])

        logger.info("node.strategist.done", post_count=len(calendar.posts), target=total_posts)

        return {
            "calendar": calendar,
            "messages": [AIMessage(content=f"[Strategist] Calendar: {len(calendar.posts)}/{total_posts} posts")],
        }
    except Exception as e:
        logger.error("node.strategist.error", error=str(e))
        return {"error": f"Strategist failed: {e}"}


# ── Node 2: Product Expert ─────────────────────────────────


def product_expert_node(state: AgentState) -> dict:
    """Enrich product-focused posts with detailed spotlights."""
    calendar = state.get("calendar")
    if not calendar or not calendar.posts:
        logger.warning("node.product_expert.skip", reason="no calendar")
        return {"product_spotlights": {}}

    product_ids = extract_product_ids(calendar)
    if not product_ids:
        logger.info("node.product_expert.skip", reason="no product posts")
        return {"product_spotlights": {}}

    logger.info("node.product_expert.start", product_ids=product_ids)

    try:
        details = []
        for pid in product_ids:
            info = get_product_info.invoke({"product_id": pid})
            details.append(info)

        chain = build_product_expert_chain()
        result = chain.invoke({
            "product_ids": ", ".join(product_ids),
            "product_details": "\n---\n".join(details),
        })

        raw = result.content if hasattr(result, "content") else str(result)
        spotlights = parse_spotlights(raw)

        logger.info("node.product_expert.done", spotlight_count=len(spotlights))

        return {
            "product_spotlights": spotlights,
            "messages": [AIMessage(content=f"[Product Expert] {len(spotlights)} spotlights created")],
        }
    except Exception as e:
        logger.error("node.product_expert.error", error=str(e))
        return {"product_spotlights": {}, "error": f"Product Expert failed: {e}"}


# ── Node 3: Writer ───────────────────────────────────────────


def writer_node(state: AgentState) -> dict:
    """Write all post drafts from the calendar."""
    calendar = state.get("calendar")
    if not calendar or not calendar.posts:
        logger.warning("node.writer.skip", reason="no calendar")
        return {"drafts": []}

    logger.info("node.writer.start", post_count=len(calendar.posts))

    try:
        platform_rules = get_all_platform_rules.invoke({})
        spotlights = state.get("product_spotlights", {})
        calendar_data = [p.model_dump() for p in calendar.posts]
        chain = build_writer_chain()

        result = chain.invoke({
            "vision_summary": state["vision_summary"],
            "platform_rules": platform_rules,
            "calendar_json": json.dumps(calendar_data, ensure_ascii=False, indent=2),
            "spotlights_json": json.dumps(spotlights, ensure_ascii=False, indent=2),
            "post_count": len(calendar.posts),
        })

        raw = result.content if hasattr(result, "content") else str(result)
        drafts = parse_drafts(raw)

        logger.info("node.writer.done", draft_count=len(drafts))

        return {
            "drafts": drafts,
            "messages": [AIMessage(content=f"[Writer] {len(drafts)} drafts written")],
        }
    except Exception as e:
        logger.error("node.writer.error", error=str(e))
        return {"drafts": [], "error": f"Writer failed: {e}"}


# ── Node 4: Visual Prompter ─────────────────────────────────


def visual_node(state: AgentState) -> dict:
    """Generate visual prompts and assign image URLs from config.

    Image URLs are defined in config/weekly_brief.yaml per campaign/platform.
    Visual prompts are still generated for content alignment guidance.
    """
    drafts = state.get("drafts", [])
    if not drafts:
        logger.warning("node.visual.skip", reason="no drafts")
        return {"drafts": []}

    logger.info("node.visual.start", draft_count=len(drafts))

    try:
        drafts_data = [
            {"platform": d.platform, "day": d.day, "theme": d.theme, "text_preview": d.text[:200]}
            for d in drafts
        ]

        chain = build_visual_chain()
        result = chain.invoke({
            "drafts_json": json.dumps(drafts_data, ensure_ascii=False, indent=2),
            "draft_count": len(drafts),
        })

        raw = result.content if hasattr(result, "content") else str(result)
        visuals = parse_visual_prompts(raw)
        updated_drafts = merge_visual_into_drafts(drafts, visuals)

        # Assign image URLs from weekly brief config
        updated_drafts = _assign_image_urls(updated_drafts)

        images_assigned = sum(1 for d in updated_drafts if d.image_path)
        logger.info("node.visual.done", visuals=len(visuals), images_assigned=images_assigned)

        return {
            "drafts": updated_drafts,
            "messages": [AIMessage(
                content=f"[Visual] {len(visuals)} prompts, {images_assigned} images assigned"
            )],
        }
    except Exception as e:
        logger.error("node.visual.error", error=str(e))
        return {"drafts": drafts, "error": f"Visual failed: {e}"}


# ── Node 5: Optimizer ───────────────────────────────────────


def optimizer_node(state: AgentState) -> dict:
    """Optimize each draft for its target platform."""
    drafts = state.get("drafts", [])
    if not drafts:
        logger.warning("node.optimizer.skip", reason="no drafts")
        return {"drafts": []}

    logger.info("node.optimizer.start", draft_count=len(drafts))

    try:
        platform_rules = get_all_platform_rules.invoke({})
        drafts_data = [d.model_dump() for d in drafts]

        chain = build_optimizer_chain()
        result = chain.invoke({
            "platform_rules": platform_rules,
            "drafts_json": json.dumps(drafts_data, ensure_ascii=False, indent=2),
            "draft_count": len(drafts),
        })

        raw = result.content if hasattr(result, "content") else str(result)
        optimized = parse_optimized(raw)
        updated_drafts = merge_optimized_into_drafts(drafts, optimized)

        logger.info("node.optimizer.done", optimized_count=len(optimized))

        return {
            "drafts": updated_drafts,
            "messages": [AIMessage(content=f"[Optimizer] {len(optimized)} posts optimized")],
        }
    except Exception as e:
        logger.error("node.optimizer.error", error=str(e))
        return {"drafts": drafts, "error": f"Optimizer failed: {e}"}


# ── Node 6: Human Approval (interrupt) ──────────────────────


async def human_approval_node(state: AgentState) -> dict:
    """Pause for human review.

    The graph is compiled with interrupt_before=["human_approval"].
    Exports batch to output/ (Markdown + JSON) and saves to PostgreSQL.
    """
    drafts = state.get("drafts", [])
    week = state.get("current_week", "unknown")

    logger.info("node.human_approval.waiting", draft_count=len(drafts))

    try:
        md_path = export_batch_markdown(drafts, week)
        json_path = export_batch_json(drafts, week)

        # Save to PostgreSQL
        await save_weekly_batch(week, drafts)
        await save_all_posts(week, drafts)

        logger.info("node.human_approval.exported", markdown=str(md_path), json=str(json_path))

        for draft in drafts:
            draft.status = "awaiting_approval"

        return {
            "drafts": drafts,
            "approved_drafts": drafts,
            "messages": [AIMessage(
                content="[Approval] Batch exported and saved to PostgreSQL. Waiting for review."
            )],
        }
    except Exception as e:
        logger.error("node.human_approval.error", error=str(e))
        return {"drafts": drafts, "error": f"Human approval failed: {e}"}


# ── Node 7: Publisher ────────────────────────────────────────


async def publisher_node(state: AgentState) -> dict:
    """Finalize approved posts — save to PostgreSQL and export."""
    approved = state.get("approved_drafts", [])
    week = state.get("current_week", "unknown")

    if not approved:
        logger.warning("node.publisher.skip", reason="no approved drafts")
        return {"report": build_report([], week)}

    logger.info("node.publisher.start", approved_count=len(approved))

    try:
        for draft in approved:
            draft.status = "approved"

        export_batch_markdown(approved, week)
        export_batch_json(approved, week)

        report = build_report(approved, week)

        # Save final state to PostgreSQL
        await save_weekly_batch(week, approved, report)
        await save_all_posts(week, approved)

        logger.info("node.publisher.done", report=report.model_dump())

        return {
            "approved_drafts": approved,
            "report": report,
            "messages": [AIMessage(
                content=f"[Publisher] {report.total_posts_approved} posts approved and saved to PostgreSQL."
            )],
        }
    except Exception as e:
        logger.error("node.publisher.error", error=str(e))
        return {"approved_drafts": approved, "error": f"Publisher failed: {e}"}
