from abc import ABC, abstractmethod
import os
import time
import logging
from typing import Optional

from app.core.config import get_config
from app.core.exceptions import LLMServiceError, ValidationError

logger = logging.getLogger(__name__)

try:
    from openai import OpenAI, OpenAIError
except ImportError:
    OpenAI = None
    OpenAIError = Exception


# ======================================================
# TOKEN ESTIMATION
# ======================================================
def estimate_tokens(text: str) -> int:
    return max(1, len(text) // 4)


# ======================================================
# BASE PROVIDER
# ======================================================
class BaseLLMProvider(ABC):
    @abstractmethod
    def generate(self, prompt: str, request_id: Optional[str] = None) -> str:
        pass


# ======================================================
# OPENAI PROVIDER
# ======================================================
class OpenAILLMProvider(BaseLLMProvider):
    def __init__(
        self,
        api_key: str,
        model: str,
        temperature: float,
        timeout_seconds: int,
        max_retries: int,
        max_prompt_tokens: int,
        max_completion_tokens: int,
    ):
        if OpenAI is None:
            raise ImportError("openai package not installed")

        self.client = OpenAI(
            api_key=api_key,
            timeout=timeout_seconds,
        )

        self.model = model
        self.temperature = temperature
        self.max_retries = max_retries
        self.max_prompt_tokens = max_prompt_tokens
        self.max_completion_tokens = max_completion_tokens

    # 🔴 REQUIRED METHOD — MUST MATCH BASE CLASS
    def generate(self, prompt: str, request_id: Optional[str] = None) -> str:
        estimated_tokens = estimate_tokens(prompt)

        if estimated_tokens > self.max_prompt_tokens:
            raise ValidationError(
                message="Prompt size exceeds allowed token limit"
            )

        last_exception: Optional[Exception] = None

        for attempt in range(1, self.max_retries + 2):
            try:
                logger.info(
                    "request_id=%s | OpenAI attempt=%s | model=%s",
                    request_id,
                    attempt,
                    self.model,
                )

                response = self.client.chat.completions.create(
                    model=self.model,
                    messages=[
                        {
                            "role": "system",
                            "content": (
                                "You are a senior retail media creative director. "
                                "Respond ONLY with valid JSON. No markdown."
                            ),
                        },
                        {"role": "user", "content": prompt},
                    ],
                    temperature=self.temperature,
                    max_tokens=self.max_completion_tokens,
                )

                return response.choices[0].message.content

            except OpenAIError as e:
                last_exception = e
                logger.warning(
                    "request_id=%s | OpenAI error | attempt=%s | error=%s",
                    request_id,
                    attempt,
                    str(e),
                )
                time.sleep(1.5 * attempt)

            except Exception as e:
                last_exception = e
                logger.exception("Unexpected LLM failure")
                break

        raise LLMServiceError(
            message="Failed to generate content from OpenAI"
        ) from last_exception


# ======================================================
# PROVIDER FACTORY
# ======================================================
def get_llm_provider() -> BaseLLMProvider:
    config = get_config()

    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise LLMServiceError("OPENAI_API_KEY not configured")

    return OpenAILLMProvider(
        api_key=api_key,
        model=config.LLM_MODEL_NAME,
        temperature=config.LLM_TEMPERATURE,
        timeout_seconds=config.LLM_TIMEOUT_SECONDS,
        max_retries=config.LLM_MAX_RETRIES,
        max_prompt_tokens=config.LLM_MAX_PROMPT_TOKENS,
        max_completion_tokens=config.LLM_MAX_COMPLETION_TOKENS,
    )
