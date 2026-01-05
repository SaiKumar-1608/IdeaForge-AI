"""
Storyboard Prompt Generator for IdeaForge AI

This module builds a structured prompt for generating
a scene-by-scene storyboard for a retail media campaign.
"""

from typing import Dict


def build_storyboard_prompt(
    product: str,
    campaign_objective: str,
    target_audience: str,
    brand_tone: str,
    concept: Dict
) -> str:
    """
    Builds a prompt for generating a storyboard from a selected concept.

    Args:
        product (str): Product name
        campaign_objective (str): Campaign goal
        target_audience (str): Intended audience
        brand_tone (str): Brand tone
        concept (Dict): Selected concept details

    Returns:
        str: Prompt to send to the LLM
    """

    prompt = f"""
You are a senior retail media creative director working on supermarket advertising campaigns.

Your task is to create a clear, professional storyboard for a retail media ad.

Campaign Details:
- Product: {product}
- Campaign Objective: {campaign_objective}
- Target Audience: {target_audience}
- Brand Tone: {brand_tone}

Selected Creative Concept:
- Concept Title: {concept.get("concept_title")}
- Concept Description: {concept.get("description")}
- Tagline: {concept.get("tagline")}
- Visual Style: {concept.get("visual_style")}
- Color Palette: {", ".join(concept.get("color_palette", []))}

Instructions:
Generate a 4-frame storyboard suitable for a retail media advertisement.

For EACH frame, include:
1. Frame Number
2. Scene Description (what is visually shown)
3. Camera Angle / Shot Type
4. Emotional Focus
5. On-screen Text (if any)
6. Call-to-Action (if applicable)

Rules:
- Do NOT include pricing or legal claims.
- Do NOT generate brand logos or exact packaging text.
- Keep visuals retail-safe and family-friendly.
- Focus on storytelling and clarity.
- Ensure smooth visual flow from frame to frame.

Return the output strictly in JSON format using this structure:

{{
  "storyboard": [
    {{
      "frame": 1,
      "scene_description": "",
      "camera_angle": "",
      "emotion": "",
      "on_screen_text": "",
      "cta": ""
    }}
  ]
}}
"""

    return prompt.strip()
