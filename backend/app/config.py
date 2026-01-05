import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


class Settings:
    """
    Central configuration class for IdeaForge AI backend
    """

    # =========================
    # Application Settings
    # =========================
    APP_NAME: str = "IdeaForge AI"
    APP_ENV: str = os.getenv("APP_ENV", "development")
    DEBUG: bool = os.getenv("DEBUG", "True").lower() == "true"

    # =========================
    # Server Settings
    # =========================
    HOST: str = os.getenv("HOST", "0.0.0.0")
    PORT: int = int(os.getenv("PORT", 8000))

    # =========================
    # OpenAI / LLM Settings
    # =========================
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY", "")
    LLM_MODEL: str = os.getenv("LLM_MODEL", "gpt-4o-mini")
    LLM_TEMPERATURE: float = float(os.getenv("LLM_TEMPERATURE", 0.7))
    LLM_MAX_TOKENS: int = int(os.getenv("LLM_MAX_TOKENS", 800))

    # =========================
    # Image Generation (Future)
    # =========================
    IMAGE_MODEL: str = os.getenv("IMAGE_MODEL", "gpt-image-1")
    IMAGE_SIZE: str = os.getenv("IMAGE_SIZE", "1024x1024")

    # =========================
    # Security / CORS
    # =========================
    ALLOWED_ORIGINS: list = os.getenv(
        "ALLOWED_ORIGINS",
        "http://localhost:3000"
    ).split(",")

    # =========================
    # Validation
    # =========================
    def validate(self):
        if not self.OPENAI_API_KEY:
            raise ValueError(
                "OPENAI_API_KEY is missing. Please set it in the .env file."
            )


# Create a singleton settings instance
settings = Settings()
settings.validate()
