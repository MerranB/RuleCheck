import logging
from fastapi import Request, status
from fastapi.responses import JSONResponse

logger = logging.getLogger("rulecheck")

async def log_exceptions(request: Request, call_next):
    try:
        response = await call_next(request)
        return response
    except Exception as e:
        logger.exception(f"Unhandled error during request: {request.url.path}")
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={"error": "Something went wrong. Please try again later."},
        )
