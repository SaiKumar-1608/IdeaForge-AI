from fastapi import APIRouter, HTTPException
from app.models.request_models import StoryboardRequest
from app.models.response_models import StoryboardResponse
from app.services.llm_service import call_llm
from app.prompts.storyboard_prompt import build_storyboard_prompt
from app.utils.response_parser import parse_storyboard_response

router = APIRouter()


@router.post(
    "/generate-storyboard",
    response_model=StoryboardResponse,
    tags=["Storyboard"]
)
async def generate_storyboard(request: StoryboardRequest):
    """
    Generates a multi-frame storyboard for a selected creative concept.
    """

    try:
        # 1. Build prompt from concept details
        prompt = build_storyboard_prompt(
            concept_title=request.concept_title,
            concept_description=request.concept_description,
            tagline=request.tagline,
            visual_style=request.visual_style,
            audience=request.audience
        )

        # 2. Call LLM
        llm_response = call_llm(prompt)

        # 3. Parse structured output
        storyboard = parse_storyboard_response(llm_response)

        return StoryboardResponse(
            concept_title=request.concept_title,
            frames=storyboard
        )

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Storyboard generation failed: {str(e)}"
        )
