from typing import List
from pydantic import BaseModel, Field, ConfigDict


class Concept(BaseModel):
    """
    Single creative concept schema.
    """

    concept_title: str = Field(..., description="Title of the creative concept")
    description: str = Field(..., description="Short description of the concept")
    tagline: str = Field(..., description="Catchy tagline for the concept")
    visual_style: str = Field(..., description="Visual and design style")
    color_palette: List[str] = Field(
        ..., description="List of dominant colors used in the creative"
    )

    model_config = ConfigDict(
        extra="forbid",          # ❌ No extra fields allowed
        str_min_length=1     # ❌ Empty strings not allowed
    )


class ConceptResponse(BaseModel):
    """
    API response schema for concept generation.
    """

    success: bool = Field(..., description="Status of the request")
    concepts: List[Concept] = Field(
        ..., description="List of generated creative concepts"
    )

    model_config = ConfigDict(
        extra="forbid"
    )
