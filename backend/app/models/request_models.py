from pydantic import BaseModel, Field
from typing import Optional, List


# -----------------------------
# Day 1: Creative Brief Request
# -----------------------------
class CreativeBriefRequest(BaseModel):
    """
    Input model for generating creative concepts.
    """

    product_name: str = Field(
        ...,
        example="Orange Juice",
        description="Name of the product to advertise"
    )

    campaign_objective: str = Field(
        ...,
        example="Healthy morning awareness",
        description="Goal of the campaign (awareness, promotion, seasonal, etc.)"
    )

    target_audience: str = Field(
        ...,
        example="Families",
        description="Primary audience for the campaign"
    )

    brand_tone: str = Field(
        ...,
        example="Fresh and positive",
        description="Tone of the brand communication"
    )

    keywords: Optional[str] = Field(
        None,
        example="Morning, energy, health",
        description="Optional keywords to guide creative direction"
    )


# ------------------------------------
# Day 2 (Future): Storyboard Request
# ------------------------------------
class StoryboardRequest(BaseModel):
    """
    Input model for generating storyboard from a selected concept.
    """

    concept_title: str = Field(
        ...,
        example="Morning Energy Boost",
        description="Selected concept title"
    )

    concept_description: str = Field(
        ...,
        example="A bright morning family scene highlighting freshness and vitality.",
        description="Description of the selected concept"
    )

    brand_tone: str = Field(
        ...,
        example="Fresh and positive",
        description="Brand tone to maintain consistency"
    )


# ------------------------------------
# Day 2 (Future): Mood Board Request
# ------------------------------------
class MoodBoardRequest(BaseModel):
    """
    Input model for generating mood board image prompts.
    """

    visual_style: str = Field(
        ...,
        example="Lifestyle, natural lighting, family breakfast",
        description="Overall visual style of the concept"
    )

    color_palette: List[str] = Field(
        ...,
        example=["Orange", "White", "Soft Yellow"],
        description="Preferred color palette"
    )

    theme_keywords: Optional[str] = Field(
        None,
        example="Fresh, morning, natural",
        description="Optional keywords to guide mood board generation"
    )
    
class ConceptRequest(BaseModel):
    """
    Request schema for concept generation.
    """

    product: str = Field(..., description="Product name")
    objective: str = Field(..., description="Campaign objective")
    audience: str = Field(..., description="Target audience")
    tone: str = Field(..., description="Brand tone")
    keywords: Optional[str] = Field(
        None, description="Optional creative keywords"
    )
