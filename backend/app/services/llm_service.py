from typing import List, Dict, Any, Optional
import logging

from app.prompts.concept_prompt import build_concept_prompt
from app.utils.response_parser import LLMResponseParser
from app.utils.content_guard import (
    validate_user_prompt,
    validate_generated_output
)
from app.services.llm_provider import get_llm_provider
from app.core.exceptions import LLMServiceError

logger = logging.getLogger(__name__)


class LLMService:
    """
    Service layer for interacting with the LLM.

    Guarantees:
    - input safety
    - prompt consistency
    - provider abstraction
    - output safety
    - structured parsing
    - request_id propagation
    """

    @staticmethod
    def generate_concepts(
        product: str,
        objective: str,
        audience: str,
        tone: str,
        keywords: Optional[str] = None,
        request_id: Optional[str] = None
    ) -> List[Dict[str, Any]]:

        logger.info(
            "Starting concept generation | request_id=%s",
            request_id
        )

        # -------------------------------------------------
        # 1️⃣ INPUT SAFETY VALIDATION
        # -------------------------------------------------
        validate_user_prompt(
            product,
            objective,
            audience,
            tone,
            keywords or ""
        )

        logger.info(
            "User input passed safety validation | request_id=%s",
            request_id
        )

        # -------------------------------------------------
        # 2️⃣ PROMPT CONSTRUCTION
        # -------------------------------------------------
        prompt = build_concept_prompt(
            product=product,
            objective=objective,
            audience=audience,
            tone=tone,
            keywords=keywords
        )

        # -------------------------------------------------
        # 3️⃣ LLM PROVIDER INVOCATION
        # -------------------------------------------------
        try:
            provider = get_llm_provider()
            raw_response = provider.generate(
                prompt=prompt,
                request_id=request_id
            )
        except Exception as e:
            logger.exception(
                "LLM provider failed | request_id=%s",
                request_id
            )
            raise LLMServiceError(
                message="Failed to generate content from LLM"
            ) from e

        # -------------------------------------------------
        # 4️⃣ STRUCTURED RESPONSE PARSING
        # -------------------------------------------------
        try:
            concepts = LLMResponseParser.parse_concept_response(raw_response)
        except ValueError as e:
            logger.error(
                "LLM response parsing failed | request_id=%s | error=%s",
                request_id,
                str(e)
            )
            raise LLMServiceError(
                message="LLM returned an invalid response format"
            ) from e

        logger.info(
            "LLM response parsed successfully | request_id=%s",
            request_id
        )

        # -------------------------------------------------
        # 5️⃣ OUTPUT SAFETY VALIDATION
        # -------------------------------------------------
        try:
            for concept in concepts:
                validate_generated_output(concept["concept_title"])
                validate_generated_output(concept["description"])
                validate_generated_output(concept["tagline"])
        except ValueError as e:
            logger.error(
                "Generated output failed safety validation | request_id=%s | error=%s",
                request_id,
                str(e)
            )
            raise LLMServiceError(
                message="Generated content failed safety validation"
            ) from e

        # -------------------------------------------------
        # 6️⃣ FINAL SANITY CHECK
        # -------------------------------------------------
        if not concepts:
            logger.error(
                "Empty concepts generated | request_id=%s",
                request_id
            )
            raise LLMServiceError(
                message="No creative concepts generated"
            )

        logger.info(
            "Concept generation completed successfully | request_id=%s",
            request_id
        )

        return concepts
