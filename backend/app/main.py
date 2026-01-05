from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import logging

from app.routes import concept_routes, health
from app.middleware.request_id import RequestIDMiddleware
from app.core.error_handler import register_exception_handlers

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="IdeaForge AI",
    description="Concept-to-Creative Ideation Engine for Retail Media",
    version="1.0.0"
)

logger.info("Starting IdeaForge AI backend...")

# -------------------------------
# Middleware
# -------------------------------
app.add_middleware(RequestIDMiddleware)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -------------------------------
# Exception Handlers
# -------------------------------
register_exception_handlers(app)

# -------------------------------
# Routes (⚠️ THIS WAS THE ISSUE)
# -------------------------------

# ✅ HEALTH CHECK
app.include_router(
    health.router,
    prefix=""
)

# ✅ CONCEPT GENERATION (THIS LINE WAS MISSING / WRONG)
app.include_router(
    concept_routes.router,
    prefix="/api/v1",
    tags=["Concept Generation"]
)

@app.get("/")
def root():
    return {
        "status": "ok",
        "service": "IdeaForge AI backend running"
    }

