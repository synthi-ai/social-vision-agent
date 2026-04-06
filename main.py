"""FastAPI application — trigger, manage, and query weekly content generation.

Endpoints:
  GET  /                        -> Health check
  POST /run                     -> Trigger a weekly content generation run
  POST /approve/{week}          -> Resume graph after human approval
  GET  /status/{week}           -> Check status of a weekly run
  GET  /posts/{week}            -> Get all posts for a week (from PostgreSQL)
  GET  /posts/platform/{name}   -> Get recent posts by platform
  GET  /batches                 -> List recent weekly batches
  POST /images/upload/{week}    -> Upload images for a week
"""

from __future__ import annotations

import shutil
from contextlib import asynccontextmanager
from datetime import datetime
from pathlib import Path

from fastapi import FastAPI, HTTPException, UploadFile, File
from fastapi.responses import JSONResponse
from pydantic import BaseModel

from config.settings import settings
from src.db.postgres import (
    ensure_tables,
    close_database,
    get_posts_by_week,
    get_posts_by_platform,
    list_weekly_batches,
    update_post_image,
)
from src.graph.weekly_content_graph import build_graph
from src.skills.loader import get_skill_registry
from src.utils.logger import setup_logging

setup_logging()


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Startup/shutdown lifecycle — PostgreSQL tables + skills discovery + cleanup."""
    await ensure_tables()
    registry = get_skill_registry()
    registry.discover()
    yield
    await close_database()


app = FastAPI(
    title="Social Vision Agents",
    description="Production-ready social media content automation powered by LangGraph + Llama 4",
    version="1.0.0",
    lifespan=lifespan,
)

_graph = build_graph()


class RunResponse(BaseModel):
    week: str
    thread_id: str
    status: str
    message: str


class ApproveRequest(BaseModel):
    approved_post_indices: list[int] | None = None


# ── Core Endpoints ───────────────────────────────────────────


@app.get("/")
async def health():
    return {
        "service": "social-vision-agents",
        "status": "healthy",
        "version": "1.0.0",
    }


@app.post("/run", response_model=RunResponse)
async def trigger_run(week: str | None = None):
    """Trigger a new weekly content generation run."""
    week = week or datetime.now().strftime("%Y-W%W")
    thread_id = f"weekly-{week}"

    vision_path = settings.KNOWLEDGE_DIR / "vision.md"
    if not vision_path.exists():
        raise HTTPException(status_code=500, detail="knowledge/vision.md not found")

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

    config = {"configurable": {"thread_id": thread_id}}

    try:
        async for event in _graph.astream(initial_state, config=config):
            pass

        return RunResponse(
            week=week,
            thread_id=thread_id,
            status="awaiting_approval",
            message=f"Content generated. Review output/ folder, then POST /approve/{week}",
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/approve/{week}", response_model=RunResponse)
async def approve_run(week: str, request: ApproveRequest | None = None):
    """Resume the graph after human approval."""
    thread_id = f"weekly-{week}"
    config = {"configurable": {"thread_id": thread_id}}

    try:
        async for event in _graph.astream(None, config=config):
            pass

        return RunResponse(
            week=week,
            thread_id=thread_id,
            status="completed",
            message="Posts approved, saved to PostgreSQL, and exported.",
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/status/{week}")
async def get_status(week: str):
    """Check the status of a weekly run."""
    thread_id = f"weekly-{week}"
    config = {"configurable": {"thread_id": thread_id}}

    try:
        state = await _graph.aget_state(config)
        if state and state.values:
            report = state.values.get("report")
            drafts = state.values.get("drafts", [])
            return {
                "week": week,
                "thread_id": thread_id,
                "draft_count": len(drafts),
                "status": "completed" if report else "in_progress",
                "report": report.model_dump() if report else None,
                "next_node": state.next if hasattr(state, "next") else None,
            }
        return {"week": week, "thread_id": thread_id, "status": "not_found"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# ── PostgreSQL Query Endpoints ──────────────────────────────


@app.get("/posts/{week}")
async def get_week_posts(week: str):
    """Get all posts for a given week from PostgreSQL."""
    posts = await get_posts_by_week(week)
    return {"week": week, "count": len(posts), "posts": posts}


@app.get("/posts/platform/{platform}")
async def get_platform_posts(platform: str, limit: int = 20):
    """Get recent posts for a specific platform from PostgreSQL."""
    posts = await get_posts_by_platform(platform, limit)
    return {"platform": platform, "count": len(posts), "posts": posts}


@app.get("/batches")
async def get_batches(limit: int = 10):
    """List recent weekly batches from PostgreSQL."""
    batches = await list_weekly_batches(limit)
    return {"count": len(batches), "batches": batches}


# ── Image Upload Endpoint ────────────────────────────────────


@app.post("/images/upload/{week}")
async def upload_images(week: str, files: list[UploadFile] = File(...)):
    """Upload images for a specific week.

    Images should be named: {platform}_{day}.{ext}
    Example: linkedin_tuesday.png, x_wednesday.jpg
    """
    upload_dir = settings.IMAGES_DIR / week
    upload_dir.mkdir(parents=True, exist_ok=True)

    saved = []
    for file in files:
        if not file.filename:
            continue

        dest = upload_dir / file.filename
        with open(dest, "wb") as f:
            content = await file.read()
            f.write(content)
        saved.append(str(dest))

        # Try to match to an existing post in PostgreSQL
        stem = Path(file.filename).stem.lower()
        parts = stem.split("_", 1)
        if len(parts) == 2:
            platform, day = parts
            await update_post_image(week, platform, day, str(dest))

    return {
        "week": week,
        "uploaded": len(saved),
        "files": saved,
        "hint": "Name files as {platform}_{day}.ext (e.g. linkedin_tuesday.png)",
    }


# ── Skills Endpoints ─────────────────────────────────────────


@app.get("/skills")
async def list_skills():
    """List all available skills with metadata."""
    registry = get_skill_registry()
    skills = registry.all_skills
    return {
        "count": len(skills),
        "skills": [
            {
                "name": s.name,
                "description": s.description,
                "license": s.license,
                "metadata": s.metadata,
                "path": str(s.path),
            }
            for s in skills
        ],
    }


@app.get("/skills/{name}")
async def get_skill(name: str):
    """Get full details and instructions for a specific skill."""
    registry = get_skill_registry()
    skill = registry.get(name)
    if not skill:
        raise HTTPException(status_code=404, detail=f"Skill '{name}' not found")
    return {
        "name": skill.name,
        "description": skill.description,
        "license": skill.license,
        "metadata": skill.metadata,
        "instructions": skill.body,
    }
