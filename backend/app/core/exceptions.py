from typing import Optional


class AppException(Exception):
    """
    Base class for all application-level exceptions.
    """

    def __init__(
        self,
        message: str,
        status_code: int,
        error_code: str,
        details: Optional[str] = None
    ):
        self.message = message
        self.status_code = status_code
        self.error_code = error_code
        self.details = details
        super().__init__(message)


class ValidationError(AppException):
    def __init__(self, message: str, details: Optional[str] = None):
        super().__init__(
            message=message,
            status_code=400,
            error_code="VALIDATION_ERROR",
            details=details
        )


class RateLimitError(AppException):
    def __init__(self, message: str = "Too many requests"):
        super().__init__(
            message=message,
            status_code=429,
            error_code="RATE_LIMIT_EXCEEDED"
        )


class LLMServiceError(AppException):
    def __init__(self, message: str = "LLM service failed"):
        super().__init__(
            message=message,
            status_code=500,
            error_code="LLM_ERROR"
        )


class InternalServerError(AppException):
    def __init__(self, message: str = "Internal server error"):
        super().__init__(
            message=message,
            status_code=500,
            error_code="INTERNAL_ERROR"
        )
