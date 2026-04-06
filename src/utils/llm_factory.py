"""LLM factory with automatic fallback.

DeerFlow-inspired pattern: configurable factory that automatically switches
to the fallback provider if the primary one fails.
Ollama (Llama 4 local) by default, Groq as fallback.
"""

from __future__ import annotations

import structlog
from langchain_core.language_models import BaseChatModel

from config.settings import settings

logger = structlog.get_logger(__name__)


def get_llm(
    provider: str | None = None,
    temperature: float = 0.7,
    max_tokens: int | None = None,
) -> BaseChatModel:
    """Instantiate an LLM for the requested provider.

    Args:
        provider: "ollama", "groq", or "gemini". If None, uses the primary provider.
        temperature: Model creativity (0.0 = deterministic, 1.5 = very creative).
        max_tokens: Output token limit. Defaults from settings.

    Returns:
        A ready-to-use BaseChatModel instance.
    """
    provider = provider or settings.llm.provider
    max_tokens = max_tokens or settings.llm.max_tokens

    if provider == "ollama":
        from langchain_ollama import ChatOllama

        logger.info("llm.init", provider="ollama", model=settings.OLLAMA_MODEL)
        return ChatOllama(
            base_url=settings.OLLAMA_BASE_URL,
            model=settings.OLLAMA_MODEL,
            temperature=temperature,
            num_predict=max_tokens,
        )

    if provider == "groq":
        from langchain_groq import ChatGroq

        api_key = settings.GROQ_API_KEY
        if api_key is None:
            raise ValueError("GROQ_API_KEY not configured in .env")

        model = settings.GROQ_FALLBACK_MODEL
        logger.info("llm.init", provider="groq", model=model)
        return ChatGroq(
            api_key=api_key.get_secret_value(),
            model=model,
            temperature=temperature,
            max_tokens=max_tokens,
        )

    if provider == "gemini":
        from langchain_google_genai import ChatGoogleGenerativeAI

        api_key = settings.GOOGLE_API_KEY
        if api_key is None:
            raise ValueError("GOOGLE_API_KEY not configured in .env")

        model = settings.GEMINI_MODEL
        logger.info("llm.init", provider="gemini", model=model)
        return ChatGoogleGenerativeAI(
            google_api_key=api_key.get_secret_value(),
            model=model,
            temperature=temperature,
            max_output_tokens=max_tokens,
        )

    raise ValueError(f"Unknown LLM provider: {provider}")


def get_llm_with_fallback(
    temperature: float = 0.7,
    max_tokens: int | None = None,
) -> BaseChatModel:
    """Try the primary provider, fall back to the secondary on failure.

    Returns:
        A working LLM instance (primary or fallback).

    Raises:
        RuntimeError: If both providers fail.
    """
    primary = settings.llm.provider
    fallback = settings.llm.fallback_provider

    try:
        llm = get_llm(provider=primary, temperature=temperature, max_tokens=max_tokens)
        llm.invoke("ping")
        logger.info("llm.ready", provider=primary)
        return llm
    except Exception as e:
        logger.warning("llm.primary_failed", provider=primary, error=str(e))

    try:
        llm = get_llm(provider=fallback, temperature=temperature, max_tokens=max_tokens)
        logger.info("llm.fallback_ready", provider=fallback)
        return llm
    except Exception as e:
        logger.error("llm.all_failed", primary=primary, fallback=fallback, error=str(e))
        raise RuntimeError(
            f"Failed to initialize any LLM. Primary ({primary}) and fallback ({fallback}) "
            f"both failed. Check your .env and make sure Ollama is running."
        ) from e
