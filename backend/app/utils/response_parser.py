import json
import re
from typing import List, Dict, Any


class LLMResponseParser:
    """
    Strict parser for validating and normalizing LLM outputs.
    Ensures frontend-safe, schema-compliant responses.
    """

    REQUIRED_FIELDS = {
        "concept_title": str,
        "description": str,
        "tagline": str,
        "visual_style": str,
        "color_palette": list,
    }

    @staticmethod
    def _clean_text(text: str) -> str:
        """
        Remove markdown fences and trim whitespace.
        """
        text = text.strip()

        # Remove ```json or ``` wrappers
        text = re.sub(r"```(?:json)?", "", text, flags=re.IGNORECASE)
        text = re.sub(r"```", "", text)

        return text.strip()

    @staticmethod
    def extract_json(text: str) -> Any:
        """
        Extract JSON safely from LLM response.
        """
        cleaned = LLMResponseParser._clean_text(text)

        # 1. Try direct JSON load
        try:
            return json.loads(cleaned)
        except json.JSONDecodeError:
            pass

        # 2. Regex-based extraction (array preferred)
        patterns = [
            r"\[\s*\{.*?\}\s*\]",   # list of objects
            r"\{.*?\}"              # single object
        ]

        for pattern in patterns:
            match = re.search(pattern, cleaned, re.DOTALL)
            if match:
                try:
                    return json.loads(match.group())
                except json.JSONDecodeError:
                    continue

        raise ValueError(
            "LLM response does not contain valid JSON. "
            "Ensure the model returns pure JSON."
        )

    @staticmethod
    def _validate_color_palette(palette: Any) -> List[str]:
        """
        Ensure color_palette is a list of strings.
        """
        if not isinstance(palette, list):
            raise ValueError("color_palette must be a list")

        cleaned_palette = []
        for color in palette:
            if not isinstance(color, str):
                raise ValueError("color_palette items must be strings")
            cleaned_palette.append(color.strip())

        if not cleaned_palette:
            raise ValueError("color_palette cannot be empty")

        return cleaned_palette

    @staticmethod
    def validate_concepts(data: Any) -> List[Dict[str, Any]]:
        """
        Enforce strict schema for concept list.
        """
        if not isinstance(data, list):
            raise ValueError("Concept response must be a list of objects")

        if len(data) == 0:
            raise ValueError("Concept list cannot be empty")

        validated_concepts = []

        for idx, concept in enumerate(data):
            if not isinstance(concept, dict):
                raise ValueError(f"Concept at index {idx} is not an object")

            # Check required fields
            for field, expected_type in LLMResponseParser.REQUIRED_FIELDS.items():
                if field not in concept:
                    raise ValueError(
                        f"Concept at index {idx} missing required field '{field}'"
                    )
                if not isinstance(concept[field], expected_type):
                    raise ValueError(
                        f"Field '{field}' in concept {idx} must be of type "
                        f"{expected_type.__name__}"
                    )

            validated_concepts.append({
                "concept_title": concept["concept_title"].strip(),
                "description": concept["description"].strip(),
                "tagline": concept["tagline"].strip(),
                "visual_style": concept["visual_style"].strip(),
                "color_palette": LLMResponseParser._validate_color_palette(
                    concept["color_palette"]
                ),
            })

        return validated_concepts

    @staticmethod
    def parse_concept_response(llm_response: str) -> List[Dict[str, Any]]:
        """
        Entry point for concept parsing.
        Always returns a clean, validated list or raises an error.
        """
        if not llm_response or not isinstance(llm_response, str):
            raise ValueError("Empty or invalid LLM response")

        json_data = LLMResponseParser.extract_json(llm_response)
        return LLMResponseParser.validate_concepts(json_data)
