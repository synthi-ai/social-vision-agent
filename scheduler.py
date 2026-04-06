"""Scheduler — runs the weekly pipeline automatically via APScheduler.

Default: every Monday at 8:00 AM (configurable).

Usage:
    python scheduler.py              # Start the scheduler daemon
"""

from __future__ import annotations

import asyncio
from datetime import datetime

import structlog
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger

from src.utils.logger import setup_logging

setup_logging()
logger = structlog.get_logger(__name__)


def weekly_job():
    """Execute the weekly pipeline as a scheduled job."""
    from run_weekly import run_pipeline

    week = datetime.now().strftime("%Y-W%W")
    logger.info("scheduler.trigger", week=week)

    try:
        asyncio.run(run_pipeline(week=week, resume=False))
        logger.info("scheduler.complete", week=week)
    except Exception as e:
        logger.error("scheduler.failed", week=week, error=str(e))


def main():
    """Start the scheduler daemon."""
    scheduler = BlockingScheduler()

    # Every Monday at 8:00 AM
    scheduler.add_job(
        weekly_job,
        trigger=CronTrigger(day_of_week="mon", hour=8, minute=0),
        id="weekly_content_generation",
        name="Weekly Content Generation Pipeline",
        replace_existing=True,
    )

    logger.info("scheduler.started", schedule="Monday 08:00")
    print("Scheduler started. Weekly pipeline will run every Monday at 08:00.")
    print("Press Ctrl+C to stop.")

    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        logger.info("scheduler.stopped")
        print("\nScheduler stopped.")


if __name__ == "__main__":
    main()