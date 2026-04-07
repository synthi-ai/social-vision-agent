"""
Centralized configuration — Pydantic Settings v2.
Auto-loads from .env + environment variables.
"""

from pathlib import Path
from typing import Literal, Optional

from pydantic import BaseModel, Field, SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_DIR = Path(__file__).resolve().parent.parent


class LLMConfig(BaseModel):
    """Primary LLM + fallback configuration."""

    provider: Literal["ollama", "groq", "gemini", "xai"] = "ollama"
    model: str = "llama4"
    fallback_provider: Literal["ollama", "groq", "gemini", "xai"] = "groq"
    fallback_model: str = "llama-4-scout-17b-16e-instruct"
    temperature: float = Field(0.7, ge=0.0, le=1.5)
    max_tokens: int = 4096


class GrokImagineConfig(BaseModel):
    """Grok/xAI image generation configuration (optional)."""

    api_key: Optional[SecretStr] = None
    endpoint: str = "https://api.x.ai/v1/images/generations"
    model: str = "grok-2-image"
    enabled: bool = False


class AppSettings(BaseSettings):
    """Main settings — loaded from .env automatically."""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )

    # ── Paths ────────────────────────────────────────────────
    KNOWLEDGE_DIR: Path = BASE_DIR / "knowledge"
    OUTPUT_DIR: Path = BASE_DIR / "output"
    IMAGES_DIR: Path = BASE_DIR / "images"
    VECTORSTORE_DIR: Path = BASE_DIR / "knowledge" / "vectorstore"

    # ── Ollama ───────────────────────────────────────────────
    OLLAMA_BASE_URL: str = "http://localhost:11434"
    OLLAMA_MODEL: str = "llama4"

    # ── Groq ─────────────────────────────────────────────────
    GROQ_API_KEY: Optional[SecretStr] = None
    GROQ_FALLBACK_MODEL: str = "llama-4-scout-17b-16e-instruct"

    # ── Google Gemini ─────────────────────────────────────────
    GOOGLE_API_KEY: Optional[SecretStr] = None
    GEMINI_MODEL: str = "gemini-3-pro"

    # ── xAI (Grok LLM) ───────────────────────────────────────
    XAI_API_KEY: Optional[SecretStr] = None
    XAI_MODEL: str = "grok-3-mini-fast"

    # ── Grok Imagine (optional — images are provided manually by default)
    GROK_IMAGINE_API_KEY: Optional[SecretStr] = None
    GROK_IMAGINE_ENABLED: bool = False

    # ── Tavily (web search) ──────────────────────────────────
    TAVILY_API_KEY: Optional[SecretStr] = None

    # ── Database (PostgreSQL — checkpoints + post storage) ───
    DATABASE_URL: str = "postgresql://svagent:changeme_in_production@localhost:5432/social_vision"

    # ── LLM routing ────────────────────────────────────────
    LLM_PROVIDER: Literal["ollama", "groq", "gemini", "xai"] = "ollama"
    LLM_FALLBACK_PROVIDER: Literal["ollama", "groq", "gemini", "xai"] = "groq"

    # ── Observability ────────────────────────────────────────
    LANGSMITH_API_KEY: Optional[SecretStr] = None
    LANGSMITH_PROJECT: str = "social-vision-agents-prod"
    LANGSMITH_TRACING: bool = False

    # ── Human approval ───────────────────────────────────────
    HUMAN_APPROVAL_REQUIRED: bool = True
    APPROVAL_METHOD: Literal["file", "slack", "api"] = "file"
    SLACK_WEBHOOK_URL: Optional[SecretStr] = None

    # ── Posting APIs ──────────────────────────��──────────────
    LINKEDIN_ACCESS_TOKEN: Optional[SecretStr] = None
    X_BEARER_TOKEN: Optional[SecretStr] = None
    X_API_KEY: Optional[SecretStr] = None
    X_API_SECRET: Optional[SecretStr] = None
    TIKTOK_ACCESS_TOKEN: Optional[SecretStr] = None
    META_ACCESS_TOKEN: Optional[SecretStr] = None

    @property
    def llm(self) -> LLMConfig:
        return LLMConfig(
            provider=self.LLM_PROVIDER,
            model=self.OLLAMA_MODEL,
            fallback_provider=self.LLM_FALLBACK_PROVIDER,
            fallback_model=self.GROQ_FALLBACK_MODEL,
        )

    @property
    def grok_imagine(self) -> GrokImagineConfig:
        return GrokImagineConfig(
            api_key=self.GROK_IMAGINE_API_KEY,
            enabled=self.GROK_IMAGINE_ENABLED,
        )

    @property
    def is_postgres(self) -> bool:
        return self.DATABASE_URL.startswith("postgresql")


settings = AppSettings()
