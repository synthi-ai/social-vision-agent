"""Central state for the LangGraph workflow.

Pattern inspired by DeerFlow: a single TypedDict acts as a shared "whiteboard"
across all nodes. Each node reads what it needs and writes its results.
LangGraph checkpoints this state at every step for crash recovery and
human-in-the-loop interrupts.
"""

from __future__ import annotations

from typing import Annotated, Optional, TypedDict

from langgraph.graph.message import add_messages
from langchain_core.messages import BaseMessage
from pydantic import BaseModel, Field


# ── Pydantic sub-models (clean serialization) ────────────────


class PlannedPost(BaseModel):
    """A planned post in the weekly editorial calendar."""

    platform: str = Field(description="linkedin | x | tiktok | facebook")
    theme: str = Field(description="vision | product | engagement | education")
    product_id: Optional[str] = Field(default=None, description="Product ID for product posts")
    hook_idea: str = Field(default="", description="Hook/angle idea")
    format: str = Field(default="text_plus_image", description="Post format type")
    day: str = Field(default="", description="Scheduled day of the week")


class ContentCalendar(BaseModel):
    """Weekly editorial calendar."""

    week: str = Field(description="Format YYYY-WNN")
    posts: list[PlannedPost] = Field(default_factory=list)


class PostDraft(BaseModel):
    """Complete post draft, enriched progressively by each agent."""

    platform: str
    theme: str
    product_focus: Optional[str] = None
    day: str = ""

    # Filled by Writer
    text: str = ""
    hashtags: list[str] = Field(default_factory=list)
    cta: str = ""

    # Filled by Visual Prompter
    visual_prompt: str = ""
    image_path: Optional[str] = None  # URL from config or local path

    # Filled by Optimizer
    optimized_text: str = ""
    optimization_notes: str = ""

    # Workflow status
    status: str = Field(
        default="planned",
        description="planned -> drafted -> optimized -> awaiting_approval -> approved -> posted",
    )


class WeeklyReport(BaseModel):
    """Summary report for the week."""

    week: str
    total_posts_planned: int = 0
    total_posts_drafted: int = 0
    total_posts_approved: int = 0
    total_posts_posted: int = 0
    notes: str = ""


# ── LangGraph State (TypedDict for checkpoint compatibility) ─


class AgentState(TypedDict):
    """Shared state for the weekly content graph.

    Each node receives and returns a subset of this state.
    LangGraph merges updates automatically via annotations.
    """

    # Internal message history
    messages: Annotated[list[BaseMessage], add_messages]

    # Week context
    current_week: str
    vision_summary: str

    # Step 0: Researcher -> web research insights
    research_insights: str

    # Step 1: Strategist -> calendar
    calendar: Optional[ContentCalendar]

    # Step 2: Product Expert -> enriched spotlights
    product_spotlights: dict[str, dict]

    # Steps 3-5: Writer -> Visual -> Optimizer -> drafts
    drafts: list[PostDraft]

    # Step 6: Human approval
    approved_drafts: list[PostDraft]

    # Step 7: Report
    report: Optional[WeeklyReport]

    # Error tracking
    error: Optional[str]