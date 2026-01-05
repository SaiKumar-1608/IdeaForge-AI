import logging
from fastapi import Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError

from app.core.exceptions import AppException

logger = logging.getLogger(__name__)


def register_exception_handlers(app):
    """
    Register global exception handlers on FastAPI app.
    """

    @app.exception_handler(AppException)
    async def handle_app_exception(request: Request, exc: AppException):
        logger.warning(
            "AppException | path=%s | code=%s | message=%s",
            request.url.path,
            exc.error_code,
            exc.message
        )

        return JSONResponse(
            status_code=exc.status_code,
            content={
                "success": False,
                "error": {
                    "code": exc.error_code,
                    "message": exc.message,
                    "details": exc.details
                }
            }
        )

    @app.exception_handler(RequestValidationError)
    async def handle_request_validation_error(
        request: Request,
        exc: RequestValidationError
    ):
        logger.warning(
            "RequestValidationError | path=%s | errors=%s",
            request.url.path,
            exc.errors()
        )

        return JSONResponse(
            status_code=400,
            content={
                "success": False,
                "error": {
                    "code": "REQUEST_VALIDATION_ERROR",
                    "message": "Invalid request payload",
                    "details": exc.errors()
                }
            }
        )

    @app.exception_handler(Exception)
    async def handle_unhandled_exception(request: Request, exc: Exception):
        logger.exception(
            "UnhandledException | path=%s",
            request.url.path
        )

        return JSONResponse(
            status_code=500,
            content={
                "success": False,
                "error": {
                    "code": "UNEXPECTED_ERROR",
                    "message": "An unexpected error occurred"
                }
            }
        )
