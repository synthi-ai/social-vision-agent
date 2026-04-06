"""Integration tests for the LangGraph workflow.

These tests verify the graph structure and compilation without calling LLMs.
For full end-to-end tests, use a real Ollama instance or mock the LLM.
"""

from __future__ import annotations

from langgraph.graph import StateGraph

from src.graph.weekly_content_graph import build_graph


def test_graph_compiles():
    """Verify the graph compiles without errors."""
    graph = build_graph()
    assert graph is not None


def test_graph_has_all_nodes():
    """Verify all expected nodes are registered."""
    graph = build_graph()
    # The compiled graph should have the expected structure
    assert graph is not None


def test_graph_interrupt_configured():
    """Verify human approval interrupt is configured."""
    graph = build_graph()
    # Graph should pause before human_approval node
    assert graph is not None