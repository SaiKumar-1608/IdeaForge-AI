from fastapi import APIRouter, Request, status
from typing import Dict, Any
import time

from app.models.request_models import ConceptRequest
from app.models.response_models import ConceptResponse
from app.services.llm_service import LLMService
from app.core.exceptions import RateLimitError

router = APIRouter()

# -------------------------------------------------
# SIMPLE IN-MEMORY RATE LIMITER
# -------------------------------------------------

REQUEST_LIMIT = 10
TIME_WINDOW = 60
request_log = {}


def rate_limit(client_ip: str):
    current_time = time.time()
    timestamps = request_log.get(client_ip, [])

    timestamps = [t for t in timestamps if current_time - t < TIME_WINDOW]

    if len(timestamps) >= REQUEST_LIMIT:
        raise RateLimitError(
            message="Too many requests. Please wait and try again."
        )

    timestamps.append(current_time)
    request_log[client_ip] = timestamps


@router.post(
    "/generate-concepts",
    response_model=ConceptResponse,
    status_code=status.HTTP_200_OK,
    summary="Generate creative concepts from campaign brief",
    tags=["Concept Generation"]
)
def generate_concepts(
    request: ConceptRequest,
    http_request: Request
) -> Dict[str, Any]:

    request_id = getattr(http_request.state, "request_id", None)
    client_ip = http_request.client.host
    rate_limit(client_ip)

    concepts = LLMService.generate_concepts(
        product=request.product,
        objective=request.objective,
        audience=request.audience,
        tone=request.tone,
        keywords=request.keywords,
        request_id=request_id
    )

    return {
        "success": True,
        "concepts": concepts
    }
