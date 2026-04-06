"""Web search tool — enriches content with real-time web research.

Uses Tavily as the primary search engine (requires API key) with
DuckDuckGo as a free fallback. Agents use this to research trends,
competitor activity, and current events for timely posts.
"""

from __future__ import annotations

import structlog
from langchain_core.tools import tool

from config.settings import settings

logger = structlog.get_logger(__name__)


def _search_tavily(query: str, max_results: int = 5) -> str | None:
    """Try Tavily search. Returns None on failure or missing key."""
    api_key = settings.TAVILY_API_KEY
    if api_key is None:
        return None

    try:
        from tavily import TavilyClient

        client = TavilyClient(api_key=api_key.get_secret_value())
        response = client.search(query=query, max_results=max_results)

        results = []
        for item in response.get("results", []):
            title = item.get("title", "")
            snippet = item.get("content", "")
            url = item.get("url", "")
            results.append(f"**{title}**\n{snippet}\n{url}")

        output = "\n\n".join(results) if results else None
        if output:
            logger.info("web_search.tavily.success", query=query, result_count=len(results))
        return output

    except ImportError:
        logger.warning("web_search.tavily.not_installed")
        return None
    except Exception as e:
        logger.warning("web_search.tavily.error", query=query, error=str(e))
        return None


def _search_duckduckgo(query: str, max_results: int = 5) -> str | None:
    """Fallback DuckDuckGo search. Returns None on failure."""
    try:
        from langchain_community.tools import DuckDuckGoSearchResults

        search = DuckDuckGoSearchResults(max_results=max_results)
        results = search.invoke(query)
        output = str(results)
        logger.info("web_search.ddg.success", query=query, result_length=len(output))
        return output

    except ImportError:
        logger.warning("web_search.ddg.not_installed")
        return None
    except Exception as e:
        logger.warning("web_search.ddg.error", query=query, error=str(e))
        return None


@tool
def web_search(query: str, max_results: int = 5) -> str:
    """Search the web for recent information to enrich social media content.

    Tries Tavily first (if API key configured), then falls back to DuckDuckGo.

    Args:
        query: The search query (e.g. "AI agent frameworks 2026 trends").
        max_results: Maximum number of results to return (default 5).

    Returns:
        Formatted search results with titles, snippets, and URLs.
    """
    # Try Tavily first
    result = _search_tavily(query, max_results)
    if result:
        return result

    # Fallback to DuckDuckGo
    result = _search_duckduckgo(query, max_results)
    if result:
        return result

    return (
        f"[SEARCH_UNAVAILABLE] No search provider available for query: {query}. "
        f"Configure TAVILY_API_KEY or install duckduckgo-search."
    )


@tool
def research_topic(topic: str) -> str:
    """Deep research on a topic — searches multiple angles and synthesizes.

    Args:
        topic: The research topic (e.g. "latest LangGraph features 2026").

    Returns:
        Aggregated research findings from multiple searches.
    """
    queries = [
        topic,
        f"{topic} latest news",
        f"{topic} best practices",
    ]

    all_results = []
    for q in queries:
        result = web_search.invoke({"query": q, "max_results": 3})
        if not result.startswith("[SEARCH_"):
            all_results.append(f"### {q}\n{result}")

    if not all_results:
        return f"No research results found for: {topic}"

    return "\n\n".join(all_results)
