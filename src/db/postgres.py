"""PostgreSQL connection and CRUD operations for posts and weekly batches.

Tables:
  - weekly_batches: one row per week with metadata and post list (JSONB)
  - posts: individual posts with full history and status tracking

Uses asyncpg for async connection pooling. Shares the same PostgreSQL
instance used by LangGraph checkpoints.
"""

from __future__ import annotations

from datetime import datetime, timezone
from typing import Optional

import asyncpg
import structlog

from config.settings import settings
from src.state import PostDraft, WeeklyReport

logger = structlog.get_logger(__name__)

_pool: Optional[asyncpg.Pool] = None


def _asyncpg_dsn() -> str:
    """Convert DATABASE_URL to an asyncpg-compatible DSN.

    LangGraph checkpoint URLs may use the ``postgresql+psycopg`` dialect;
    asyncpg expects a plain ``postgresql://`` prefix.
    """
    dsn = settings.DATABASE_URL
    for suffix in ("+psycopg", "+asyncpg", "+psycopg2"):
        dsn = dsn.replace(f"postgresql{suffix}", "postgresql")
    return dsn


async def _get_pool() -> asyncpg.Pool:
    """Get or create the asyncpg connection pool."""
    global _pool
    if _pool is None:
        dsn = _asyncpg_dsn()
        _pool = await asyncpg.create_pool(dsn, min_size=2, max_size=10)
        logger.info("postgres.connected", dsn=dsn.split("@")[-1])
    return _pool


async def close_database() -> None:
    """Close the PostgreSQL connection pool."""
    global _pool
    if _pool:
        await _pool.close()
        _pool = None
        logger.info("postgres.closed")


# ── Schema ───────────────────────────────────────────────────


async def ensure_tables() -> None:
    """Create tables and indexes if they don't exist."""
    pool = await _get_pool()
    async with pool.acquire() as conn:
        await conn.execute("""
            CREATE TABLE IF NOT EXISTS weekly_batches (
                id          SERIAL PRIMARY KEY,
                week        TEXT NOT NULL UNIQUE,
                post_count  INTEGER NOT NULL DEFAULT 0,
                posts       JSONB NOT NULL DEFAULT '[]'::jsonb,
                report      JSONB,
                created_at  TIMESTAMPTZ NOT NULL DEFAULT now(),
                updated_at  TIMESTAMPTZ NOT NULL DEFAULT now()
            );
        """)
        await conn.execute("""
            CREATE TABLE IF NOT EXISTS posts (
                id                  SERIAL PRIMARY KEY,
                week                TEXT NOT NULL,
                platform            TEXT NOT NULL,
                day                 TEXT NOT NULL,
                theme               TEXT,
                product_focus       TEXT,
                text                TEXT,
                original_text       TEXT,
                hashtags            JSONB NOT NULL DEFAULT '[]'::jsonb,
                cta                 TEXT,
                visual_prompt       TEXT,
                image_path          TEXT,
                optimization_notes  TEXT,
                status              TEXT NOT NULL DEFAULT 'drafted',
                created_at          TIMESTAMPTZ NOT NULL DEFAULT now(),
                updated_at          TIMESTAMPTZ NOT NULL DEFAULT now(),
                published_at        TIMESTAMPTZ,
                engagement_metrics  JSONB NOT NULL DEFAULT '{}'::jsonb,
                UNIQUE (week, platform, day)
            );
        """)
        await conn.execute(
            "CREATE INDEX IF NOT EXISTS idx_posts_platform ON posts (platform);"
        )
        await conn.execute(
            "CREATE INDEX IF NOT EXISTS idx_posts_status ON posts (status);"
        )
        await conn.execute(
            "CREATE INDEX IF NOT EXISTS idx_posts_created_at ON posts (created_at);"
        )
    logger.info("postgres.tables_ensured")


# ── Weekly Batches ───────────────────────────────────────────


async def save_weekly_batch(
    week: str,
    drafts: list[PostDraft],
    report: Optional[WeeklyReport] = None,
) -> str:
    """Save or update a weekly batch row.

    Args:
        week: Week identifier (YYYY-WNN).
        drafts: List of PostDraft objects for this week.
        report: Optional weekly report.

    Returns:
        The row ID as a string.
    """
    import json

    pool = await _get_pool()
    now = datetime.now(timezone.utc)
    posts_json = json.dumps([d.model_dump() for d in drafts], default=str)
    report_json = json.dumps(report.model_dump(), default=str) if report else None

    row = await pool.fetchrow(
        """
        INSERT INTO weekly_batches (week, post_count, posts, report, created_at, updated_at)
        VALUES ($1, $2, $3::jsonb, $4::jsonb, $5, $5)
        ON CONFLICT (week) DO UPDATE SET
            post_count = EXCLUDED.post_count,
            posts      = EXCLUDED.posts,
            report     = EXCLUDED.report,
            updated_at = EXCLUDED.updated_at
        RETURNING id
        """,
        week, len(drafts), posts_json, report_json, now,
    )

    row_id = str(row["id"])
    logger.info("postgres.batch_saved", week=week, row_id=row_id, post_count=len(drafts))
    return row_id


async def get_weekly_batch(week: str) -> Optional[dict]:
    """Retrieve a weekly batch by week identifier."""
    pool = await _get_pool()
    row = await pool.fetchrow(
        "SELECT week, post_count, posts, report, created_at, updated_at "
        "FROM weekly_batches WHERE week = $1",
        week,
    )
    if row is None:
        return None
    return dict(row)


async def list_weekly_batches(limit: int = 10) -> list[dict]:
    """List recent weekly batches, newest first."""
    pool = await _get_pool()
    rows = await pool.fetch(
        "SELECT week, post_count, updated_at "
        "FROM weekly_batches ORDER BY updated_at DESC LIMIT $1",
        limit,
    )
    return [dict(r) for r in rows]


# ── Individual Posts ─────────────────────────────────────────


async def save_post(week: str, draft: PostDraft) -> str:
    """Save an individual post (upsert by week+platform+day).

    Returns:
        The row ID as a string.
    """
    import json

    pool = await _get_pool()
    now = datetime.now(timezone.utc)

    row = await pool.fetchrow(
        """
        INSERT INTO posts (
            week, platform, day, theme, product_focus,
            text, original_text, hashtags, cta,
            visual_prompt, image_path, optimization_notes,
            status, created_at, updated_at
        ) VALUES (
            $1, $2, $3, $4, $5,
            $6, $7, $8::jsonb, $9,
            $10, $11, $12,
            $13, $14, $14
        )
        ON CONFLICT (week, platform, day) DO UPDATE SET
            theme              = EXCLUDED.theme,
            product_focus      = EXCLUDED.product_focus,
            text               = EXCLUDED.text,
            original_text      = EXCLUDED.original_text,
            hashtags           = EXCLUDED.hashtags,
            cta                = EXCLUDED.cta,
            visual_prompt      = EXCLUDED.visual_prompt,
            image_path         = EXCLUDED.image_path,
            optimization_notes = EXCLUDED.optimization_notes,
            status             = EXCLUDED.status,
            updated_at         = EXCLUDED.updated_at
        RETURNING id
        """,
        week,
        draft.platform,
        draft.day,
        draft.theme,
        draft.product_focus,
        draft.optimized_text or draft.text,
        draft.text,
        json.dumps(draft.hashtags),
        draft.cta,
        draft.visual_prompt,
        draft.image_path,
        draft.optimization_notes,
        draft.status,
        now,
    )

    row_id = str(row["id"])
    logger.info("postgres.post_saved", week=week, platform=draft.platform, day=draft.day)
    return row_id


async def save_all_posts(week: str, drafts: list[PostDraft]) -> list[str]:
    """Save all posts from a weekly batch."""
    ids = []
    for draft in drafts:
        row_id = await save_post(week, draft)
        ids.append(row_id)
    return ids


async def get_posts_by_week(week: str) -> list[dict]:
    """Retrieve all posts for a given week."""
    pool = await _get_pool()
    rows = await pool.fetch(
        "SELECT week, platform, day, theme, product_focus, text, original_text, "
        "hashtags, cta, visual_prompt, image_path, optimization_notes, "
        "status, created_at, updated_at, published_at, engagement_metrics "
        "FROM posts WHERE week = $1 ORDER BY day",
        week,
    )
    return [dict(r) for r in rows]


async def get_posts_by_platform(platform: str, limit: int = 20) -> list[dict]:
    """Retrieve recent posts for a specific platform."""
    pool = await _get_pool()
    rows = await pool.fetch(
        "SELECT week, platform, day, theme, product_focus, text, original_text, "
        "hashtags, cta, visual_prompt, image_path, optimization_notes, "
        "status, created_at, updated_at, published_at, engagement_metrics "
        "FROM posts WHERE platform = $1 ORDER BY created_at DESC LIMIT $2",
        platform, limit,
    )
    return [dict(r) for r in rows]


async def update_post_status(
    week: str, platform: str, day: str, status: str
) -> bool:
    """Update the status of a specific post."""
    pool = await _get_pool()
    now = datetime.now(timezone.utc)
    result = await pool.execute(
        "UPDATE posts SET status = $4, updated_at = $5, "
        "published_at = CASE WHEN $4 = 'posted' THEN $5 ELSE published_at END "
        "WHERE week = $1 AND platform = $2 AND day = $3",
        week, platform, day, status, now,
    )
    return result.endswith("1")


async def update_post_image(
    week: str, platform: str, day: str, image_path: str
) -> bool:
    """Attach an image path to a specific post."""
    pool = await _get_pool()
    now = datetime.now(timezone.utc)
    result = await pool.execute(
        "UPDATE posts SET image_path = $4, updated_at = $5 "
        "WHERE week = $1 AND platform = $2 AND day = $3",
        week, platform, day, image_path, now,
    )
    return result.endswith("1")
