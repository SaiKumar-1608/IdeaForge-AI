import os
from typing import List
from pydantic import BaseModel
from functools import lru_cache
from dotenv import load_dotenv
load_dotenv()


class AppConfig(BaseModel):
    """
    Central application configuration.
    Loaded once and reused across the app.
    """

    # -----------------------------
    # ENVIRONMENT
    # -----------------------------
    ENV: str = os.getenv("ENV", "development")
    DEBUG: bool = os.getenv("DEBUG", "true").lower() == "true"

    # -----------------------------
    # API SETTINGS
    # -----------------------------
    API_PREFIX: str = "/api"
    API_VERSION: str = "v1"

    # -----------------------------
    # RATE LIMITING
    # -----------------------------
    RATE_LIMIT_REQUESTS: int = int(os.getenv("RATE_LIMIT_REQUESTS", 10))
    RATE_LIMIT_WINDOW_SECONDS: int = int(os.getenv("RATE_LIMIT_WINDOW", 60))

    # -----------------------------
    # CONTENT SAFETY
    # -----------------------------
    SENSITIVE_KEYWORDS: List[str] = [
        "politics", "political", "election", "government",
        "religion", "religious", "faith",
        "sexual", "sex", "adult", "porn",
        "violence", "violent", "weapon", "gun",
        "hate", "racist", "discrimination",
        "drugs", "narcotics", "smoking",
        "alcohol", "gambling",
        "terrorism", "extremism"
    ]

    # -----------------------------
    # LLM CONFIG
    # -----------------------------
    LLM_PROVIDER: str = os.getenv("LLM_PROVIDER", "mock")  # mock | openai | azure
    LLM_MODEL_NAME: str = os.getenv("LLM_MODEL_NAME", "gpt-4o-mini")
    LLM_TEMPERATURE: float = float(os.getenv("LLM_TEMPERATURE", 0.7))

    # 🔐 LLM RELIABILITY (NEW)
    LLM_TIMEOUT_SECONDS: int = int(os.getenv("LLM_TIMEOUT_SECONDS", 10))
    LLM_MAX_RETRIES: int = int(os.getenv("LLM_MAX_RETRIES", 2))

    # 🧮 LLM COST GUARD (FUTURE USE – SAFE TO ADD NOW)
    LLM_MAX_PROMPT_TOKENS: int = int(os.getenv("LLM_MAX_PROMPT_TOKENS", 4000))
    LLM_MAX_COMPLETION_TOKENS: int = int(
        os.getenv("LLM_MAX_COMPLETION_TOKENS", 800)
    )

    # -----------------------------
    # LOGGING
    # -----------------------------
    LOG_LEVEL: str = os.getenv("LOG_LEVEL", "INFO")
    
    # -----------------------------
    # CREATIVE GENERATION
    # -----------------------------
    CONCEPT_COUNT: int = int(os.getenv("CONCEPT_COUNT", 3))
    CREATIVITY_LEVEL: float = float(os.getenv("CREATIVITY_LEVEL", 0.8))
    
    # -----------------------------
    # LLM SAFETY & COST CONTROLS
    # -----------------------------
    MAX_PROMPT_TOKENS: int = int(os.getenv("MAX_PROMPT_TOKENS", 1200))
    MAX_COMPLETION_TOKENS: int = int(os.getenv("MAX_COMPLETION_TOKENS", 600))

    LLM_TIMEOUT_SECONDS: int = int(os.getenv("LLM_TIMEOUT_SECONDS", 10))
    LLM_MAX_RETRIES: int = int(os.getenv("LLM_MAX_RETRIES", 2))

print("OPENAI_API_KEY loaded:", bool(os.getenv("OPENAI_API_KEY")))




@lru_cache
def get_config() -> AppConfig:
    """
    Cached config loader (singleton).
    """
    return AppConfig()
