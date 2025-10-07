import os
import uvicorn
from fastapi import FastAPI
from app.api.monitoring import healthcheck
from app.api import action_submissions, audit_events, decisions, policies, rules
from app.core.logging_config import setup_logging, logger
from app.core.error_handler import ExceptionLoggingMiddleware
from contextlib import asynccontextmanager

setup_logging()


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Application is starting up...")
    yield
    logger.info("Application is shutting down...")


app = FastAPI(title="RuleCheck", lifespan=lifespan)
app.add_middleware(ExceptionLoggingMiddleware)
app.include_router(healthcheck.router, prefix="/rulecheck", tags=["items"])
app.include_router(rules.router, prefix="/rulecheck/rules", tags=["rules"])
app.include_router(policies.router, prefix="/rulecheck/policies", tags=["policies"])
app.include_router(decisions.router, prefix="/rulecheck/decisions", tags=["decisions"])
app.include_router(
    action_submissions.router,
    prefix="/rulecheck/action_submissions",
    tags=["action_submissions"],
)
app.include_router(
    audit_events.router, prefix="/rulecheck/audit_events", tags=["audit_events"]
)

if __name__ == "__main__":
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    LOGGING_CONFIG = os.path.join(BASE_DIR, "app", "core", "logging_config.yaml")

    uvicorn.run(
        "app.main:app",
        host="127.0.0.1",
        port=8000,
        reload=True,
        log_config=LOGGING_CONFIG,
    )
