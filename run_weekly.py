"""CLI entry point — run the weekly content generation pipeline.

Usage:
    python run_weekly.py              # Run for current week
    python run_weekly.py --week 2026-W13
    python run_weekly.py --resume     # Resume after human approval
"""

from __future__ import annotations

import argparse
import asyncio
from datetime import datetime
from pathlib import Path

import structlog

from config.settings import settings
from src.graph.weekly_content_graph import build_graph
from src.utils.logger import setup_logging

setup_logging()
logger = structlog.get_logger(__name__)


async def run_pipeline(week: str, resume: bool = False) -> None:
    """Execute the weekly content generation pipeline.

    Args:
        week: Week identifier (YYYY-WNN format).
        resume: If True, resume from human approval interrupt.
    """
    graph = build_graph()
    thread_id = f"weekly-{week}"
    config = {"configurable": {"thread_id": thread_id}}

    if resume:
        logger.info("pipeline.resume", week=week, thread_id=thread_id)
        async for event in graph.astream(None, config=config):
            node_name = list(event.keys())[0] if isinstance(event, dict) else "unknown"
            logger.info("pipeline.node_complete", node=node_name)

        logger.info("pipeline.done", week=week)
        print(f"\nPipeline completed for {week}. Check output/ folder.")
        return

    # Fresh run
    vision_path = settings.KNOWLEDGE_DIR / "vision.md"
    if not vision_path.exists():
        logger.error("pipeline.error", reason="knowledge/vision.md not found")
        print("ERROR: knowledge/vision.md not found. Create it first.")
        return

    vision_text = vision_path.read_text(encoding="utf-8")

    initial_state = {
        "messages": [],
        "current_week": week,
        "vision_summary": vision_text,
        "research_insights": "",
        "calendar": None,
        "product_spotlights": {},
        "drafts": [],
        "approved_drafts": [],
        "report": None,
        "error": None,
    }

    logger.info("pipeline.start", week=week, thread_id=thread_id)

    async for event in graph.astream(initial_state, config=config):
        if isinstance(event, dict):
            node_name = list(event.keys())[0]
            logger.info("pipeline.node_complete", node=node_name)

    logger.info("pipeline.paused_for_approval", week=week)
    print(f"\nContent generated for {week}.")
    print(f"Review the output in: {settings.OUTPUT_DIR}/")
    print(f"Then run: python run_weekly.py --week {week} --resume")


def main_sync():
    """Synchronous entry point for pyproject.toml scripts."""
    parser = argparse.ArgumentParser(description="Social Vision Agents — Weekly Pipeline")
    parser.add_argument(
        "--week",
        default=datetime.now().strftime("%Y-W%W"),
        help="Week identifier (default: current week)",
    )
    parser.add_argument(
        "--resume",
        action="store_true",
        help="Resume pipeline after human approval",
    )
    args = parser.parse_args()

    asyncio.run(run_pipeline(week=args.week, resume=args.resume))


if __name__ == "__main__":
    main_sync()