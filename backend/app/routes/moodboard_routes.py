from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List

from app.services.image_service import generate_moodboard_images
from app.utils.prompt_builder import build_moodboard_prompt

router = APIRouter()


# -----------------------------
# Request Model
# -----------------------------
class MoodboardRequest(BaseModel):
    concept_title: str
    visual_style: str
    color_palette: List[str]
    product: str
    brand_tone: str


# -----------------------------
# Response Model
# -----------------------------
class MoodboardResponse(BaseModel):
    concept_title: str
    image_prompts: List[str]
    image_urls: List[str]


# -----------------------------
# API Route
# -----------------------------
@router.post("/generate-moodboard", response_model=MoodboardResponse)
async def generate_moodboard(request: MoodboardRequest):
    """
    Generates a moodboard for a selected creative concept.
    The moodboard contains AI-generated inspiration images
    (abstract & lifestyle focused, not exact product replicas).
    """

    try:
        # 1. Build image generation prompts
        image_prompts = build_moodboard_prompt(
            concept_title=request.concept_title,
            visual_style=request.visual_style,
            color_palette=request.color_palette,
            product=request.product,
            brand_tone=request.brand_tone
        )

        # 2. Call image generation service
        image_urls = generate_moodboard_images(image_prompts)

        # 3. Return response
        return MoodboardResponse(
            concept_title=request.concept_title,
            image_prompts=image_prompts,
            image_urls=image_urls
        )

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Failed to generate moodboard: {str(e)}"
        )
