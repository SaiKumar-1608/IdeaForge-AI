from fastapi import APIRouter
from datetime import datetime

router = APIRouter()


@router.get(
    "/health",
    summary="Health check",
    tags=["Health"]
)
def health_check():
    """
    Health check endpoint for uptime monitoring.
    """
    return {
        "status": "ok",
        "service": "IdeaForge AI",
        "version": "v1",
        "timestamp": datetime.utcnow().isoformat()
    }
