from typing import Optional


class PromptBuilder:
    """
    Centralized utility to standardize and enrich
    all LLM prompts across the application.
    """

    @staticmethod
    def normalize_text(text: str) -> str:
        """
        Clean and normalize user input text.
        """
        return text.strip()

    @staticmethod
    def build_context(
        product: str,
        objective: str,
        audience: str,
        tone: str,
        keywords: Optional[str] = None
    ) -> str:
        """
        Build a consistent campaign context block
        used across all prompts.
        """

        context = f"""
Product: {PromptBuilder.normalize_text(product)}
Campaign Objective: {PromptBuilder.normalize_text(objective)}
Target Audience: {PromptBuilder.normalize_text(audience)}
Brand Tone: {PromptBuilder.normalize_text(tone)}
"""

        if keywords:
            context += f"Keywords: {PromptBuilder.normalize_text(keywords)}\n"

        return context.strip()

    @staticmethod
    def safety_rules() -> str:
        """
        Mandatory safety and compliance rules for all prompts.
        """
        return """
Safety Rules (Mandatory):
- Generate only family-friendly, retail-appropriate content.
- Do NOT generate sexual, violent, hateful, political, or discriminatory content.
- Do NOT target or reference protected characteristics (religion, race, gender, age, health).
- Do NOT promote illegal, restricted, or age-sensitive products.
- Avoid stereotypes, misleading claims, or manipulative messaging.
- Ensure all concepts are suitable for a global supermarket audience.
"""

    @staticmethod
    def creative_director_role() -> str:
        """
        Defines the system role for all creative prompts.
        """
        return (
            "You are a senior retail media creative director "
            "experienced in creating compliant, high-performing "
            "supermarket advertising campaigns."
        )

    @staticmethod
    def concept_output_format() -> str:
        """
        Enforces strict JSON output format for concept generation.
        """
        return """
Return ONLY valid JSON in the following format:
[
  {
    "concept_title": "string",
    "description": "string",
    "tagline": "string",
    "visual_style": "string",
    "color_palette": ["string", "string"]
  }
]
"""

    @staticmethod
    def build_concept_prompt(
        product: str,
        objective: str,
        audience: str,
        tone: str,
        keywords: Optional[str] = None
    ) -> str:
        """
        Final prompt used for concept generation.
        """

        context = PromptBuilder.build_context(
            product, objective, audience, tone, keywords
        )

        prompt = f"""
{PromptBuilder.creative_director_role()}

{PromptBuilder.safety_rules()}

{context}

Task:
Generate 3 unique creative advertising concepts for a retail media campaign.
Each concept must align with the campaign objective and target audience.

Include for each concept:
- Concept title
- Short description (2–3 lines)
- Catchy tagline
- Visual style description
- Color palette

{PromptBuilder.concept_output_format()}
"""

        return prompt.strip()
