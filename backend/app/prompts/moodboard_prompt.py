"""
Moodboard Prompt Generator for IdeaForge AI

This module generates a structured prompt for an LLM
to create image-generation prompts used to build a
visual mood board for retail media campaigns.
"""

from typing import Dict


def build_moodboard_prompt(
    concept_title: str,
    concept_description: str,
    visual_style: str,
    color_palette: list,
    brand_tone: str,
    target_audience: str
) -> str:
    """
    Builds a prompt that instructs the LLM to generate
    image prompts for a creative mood board.

    The output will be used for text-to-image models
    (e.g., DALL·E / Stable Diffusion).
    """

    colors = ", ".join(color_palette)

    prompt = f"""
You are a senior retail media visual designer.

Your task is to generate image prompts for a creative mood board.
The mood board should inspire designers and marketers
before final ad production.

DO NOT include:
- Product packaging
- Logos
- Brand names
- Prices
- Text overlays

Focus only on lifestyle, environment, lighting, and emotions.

Campaign Details:
Concept Title: {concept_title}
Concept Description: {concept_description}
Visual Style: {visual_style}
Brand Tone: {brand_tone}
Target Audience: {target_audience}
Color Palette: {colors}

Generate 4 image prompts for a mood board.
Each image prompt should describe:
- Scene / environment
- Lighting style
- Mood & emotion
- Composition
- Color usage

Return the output strictly in JSON format as an array.

Example format:
[
  {{
    "image_title": "Warm Family Morning",
    "image_prompt": "A bright kitchen scene with natural sunlight, warm tones..."
  }}
]
"""
    return prompt.strip()
