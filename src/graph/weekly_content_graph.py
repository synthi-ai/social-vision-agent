"""Weekly content graph — the main LangGraph workflow.

Architecture (DeerFlow-inspired + LangGraph best practices 2026):

    START
      │
      ▼
    researcher ──── web search for trends & insights
      │
      ▼
    strategist ──── generates dynamic content calendar from weekly brief
      │
      ▼
    product_expert ── enriches product posts with spotlights
      │
      ▼
    writer ───────── writes all post drafts (multi-platform)
      │
      ▼
    visual ────────── generates visual prompts + assigns image URLs from config
      │
      ▼
    optimizer ─────── adapts to platform constraints
      │
      ▼
    human_approval ── [INTERRUPT] exports batch, saves to PostgreSQL, waits for review
      │
      ▼
    publisher ─────── finalizes, saves final state to PostgreSQL
      │
      ▼
    END

Key features:
- Checkpointing at every step (crash recovery)
- Human interrupt before approval (resume with same thread_id)
- Dynamic post count from config/weekly_brief.yaml
- Image URLs from config (not generated)
- PostgreSQL persistence for all posts
- Web search enrichment for timely content
"""

from __future__ import annotations

from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint.memory import MemorySaver

from src.state import AgentState
from src.graph.nodes import (
    researcher_node,
    strategist_node,
    product_expert_node,
    writer_node,
    visual_node,
    optimizer_node,
    human_approval_node,
    publisher_node,
)


def build_graph(checkpointer=None):
    """Build and compile the weekly content graph.

    Args:
        checkpointer: LangGraph checkpointer instance.
                      Defaults to MemorySaver (dev). Use PostgresSaver in prod.

    Returns:
        Compiled LangGraph graph ready for invocation.
    """
    if checkpointer is None:
        checkpointer = MemorySaver()

    workflow = StateGraph(AgentState)

    # Register all nodes
    workflow.add_node("researcher", researcher_node)
    workflow.add_node("strategist", strategist_node)
    workflow.add_node("product_expert", product_expert_node)
    workflow.add_node("writer", writer_node)
    workflow.add_node("visual", visual_node)
    workflow.add_node("optimizer", optimizer_node)
    workflow.add_node("human_approval", human_approval_node)
    workflow.add_node("publisher", publisher_node)

    # Pipeline: researcher -> strategist -> ... -> publisher
    workflow.add_edge(START, "researcher")
    workflow.add_edge("researcher", "strategist")
    workflow.add_edge("strategist", "product_expert")
    workflow.add_edge("product_expert", "writer")
    workflow.add_edge("writer", "visual")
    workflow.add_edge("visual", "optimizer")
    workflow.add_edge("optimizer", "human_approval")
    workflow.add_edge("human_approval", "publisher")
    workflow.add_edge("publisher", END)

    # Compile with checkpointing and human interrupt
    graph = workflow.compile(
        checkpointer=checkpointer,
        interrupt_before=["human_approval"],
    )

    return graph


def get_default_graph():
    """Get the default graph instance with MemorySaver (for dev/CLI use)."""
    return build_graph()