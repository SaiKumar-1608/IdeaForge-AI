import uuid
import logging
from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware

logger = logging.getLogger(__name__)


class RequestIDMiddleware(BaseHTTPMiddleware):
    """
    Middleware to attach a unique Request ID to each request.
    """

    HEADER_NAME = "X-Request-ID"

    async def dispatch(self, request: Request, call_next):
        # 1️⃣ Get request ID from header or generate new
        request_id = request.headers.get(self.HEADER_NAME)
        if not request_id:
            request_id = str(uuid.uuid4())

        # 2️⃣ Attach to request state (accessible everywhere)
        request.state.request_id = request_id

        # 3️⃣ Log request start
        logger.info(
            "Request started | method=%s | path=%s | request_id=%s",
            request.method,
            request.url.path,
            request_id
        )

        # 4️⃣ Process request
        response = await call_next(request)

        # 5️⃣ Attach request ID to response headers
        response.headers[self.HEADER_NAME] = request_id

        # 6️⃣ Log request end
        logger.info(
            "Request completed | status=%s | request_id=%s",
            response.status_code,
            request_id
        )

        return response
