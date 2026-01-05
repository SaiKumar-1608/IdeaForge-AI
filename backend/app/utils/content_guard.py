import re
from typing import Iterable

# Restricted keywords for retail media safety
SENSITIVE_KEYWORDS = {
    "politics", "political", "election", "government",
    "religion", "religious", "faith",
    "sexual", "sex", "adult", "porn",
    "violence", "violent", "weapon", "gun",
    "hate", "racist", "discrimination",
    "drugs", "narcotics", "smoking",
    "alcohol", "gambling",
    "terrorism", "extremism"
}


def _normalize(text: str) -> str:
    """Normalize text for keyword comparison."""
    return re.sub(r"\s+", " ", text.lower()).strip()


def _contains_sensitive_keyword(text: str) -> bool:
    """Check if text contains restricted keywords."""
    normalized = _normalize(text)
    return any(keyword in normalized for keyword in SENSITIVE_KEYWORDS)


def validate_user_prompt(*fields: Iterable[str]):
    """
    Validate user-provided input fields before LLM call.
    Raises ValueError if unsafe content is detected.
    """
    for field in fields:
        if not field or not isinstance(field, str):
            continue

        if _contains_sensitive_keyword(field):
            raise ValueError(
                "Input contains sensitive or restricted content. "
                "Please revise your campaign brief."
            )


def validate_generated_output(text: str):
    """
    Validate LLM-generated output as a final safety check.
    Raises ValueError if unsafe content is detected.
    """
    if not text or not isinstance(text, str):
        return

    if _contains_sensitive_keyword(text):
        raise ValueError(
            "Generated content contains restricted language. "
            "Please regenerate the concepts."
        )
