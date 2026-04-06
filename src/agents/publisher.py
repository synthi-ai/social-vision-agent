"""Publisher agent — exports approved posts and optionally posts via APIs.

Phase 1: Writes approved posts to output/ as Markdown + JSON.
Phase 2 (future): Posts directly via LinkedIn, X, TikTok, Meta APIs.
"""

from __future__ import annotations

import json
from datetime import datetime
from pathlib import Path

import structlog

from config.settings import settings
from src.state import PostDraft, WeeklyReport

logger = structlog.get_logger(__name__)


def export_batch_markdown(
    drafts: list[PostDraft], week: str, output_dir: Path | None = None
) -> Path:
    """Export all approved drafts as a human-readable Markdown file.

    Args:
        drafts: List of approved PostDraft objects.
        week: Week identifier (YYYY-WNN).
        output_dir: Target directory (defaults to settings.OUTPUT_DIR).

    Returns:
        Path to the generated Markdown file.
    """
    output_dir = output_dir or settings.OUTPUT_DIR
    output_dir.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.now().strftime("%Y-%m-%d_%H%M%S")
    filepath = output_dir / f"weekly_batch_{week}_{timestamp}.md"

    lines = [
        f"# Weekly Content Batch — {week}",
        f"Generated: {datetime.now().isoformat()}",
        f"Total posts: {len(drafts)}",
        "",
        "---",
        "",
    ]

    for i, draft in enumerate(drafts, 1):
        text = draft.optimized_text or draft.text
        tags = " ".join(f"#{t}" for t in draft.hashtags)

        lines.extend([
            f"## Post {i} — {draft.platform.upper()} ({draft.day})",
            f"**Theme:** {draft.theme}",
            f"**Product:** {draft.product_focus or 'N/A'}",
            f"**Status:** {draft.status}",
            "",
            text,
            "",
            f"**Hashtags:** {tags}",
            f"**CTA:** {draft.cta}",
            "",
        ])

        if draft.visual_prompt:
            lines.extend([
                f"**Visual prompt:** {draft.visual_prompt}",
                "",
            ])

        if draft.image_path:
            lines.append(f"**Image:** {draft.image_path}")
            lines.append("")

        if draft.optimization_notes:
            lines.extend([
                f"*Optimization notes: {draft.optimization_notes}*",
                "",
            ])

        lines.append("---")
        lines.append("")

    filepath.write_text("\n".join(lines), encoding="utf-8")
    logger.info("publisher.markdown_exported", filepath=str(filepath), post_count=len(drafts))
    return filepath


def export_batch_json(
    drafts: list[PostDraft], week: str, output_dir: Path | None = None
) -> Path:
    """Export all approved drafts as structured JSON for API consumption.

    Args:
        drafts: List of approved PostDraft objects.
        week: Week identifier (YYYY-WNN).
        output_dir: Target directory (defaults to settings.OUTPUT_DIR).

    Returns:
        Path to the generated JSON file.
    """
    output_dir = output_dir or settings.OUTPUT_DIR
    output_dir.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.now().strftime("%Y-%m-%d_%H%M%S")
    filepath = output_dir / f"weekly_batch_{week}_{timestamp}.json"

    data = {
        "week": week,
        "generated_at": datetime.now().isoformat(),
        "posts": [draft.model_dump() for draft in drafts],
    }

    filepath.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    logger.info("publisher.json_exported", filepath=str(filepath), post_count=len(drafts))
    return filepath


def build_report(drafts: list[PostDraft], week: str) -> WeeklyReport:
    """Build a summary report of the weekly batch."""
    return WeeklyReport(
        week=week,
        total_posts_planned=len(drafts),
        total_posts_drafted=sum(1 for d in drafts if d.status != "planned"),
        total_posts_approved=sum(1 for d in drafts if d.status in ("approved", "posted")),
        total_posts_posted=sum(1 for d in drafts if d.status == "posted"),
        notes=f"Batch exported at {datetime.now().isoformat()}",
    )