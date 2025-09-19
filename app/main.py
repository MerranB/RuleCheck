from fastapi import FastAPI
from .api.monitoring import healthcheck
from .api import action_submissions, audit_events, decisions, policies, rules
from app.core.logging_config import setup_logging, logger
from .db import model, database

model.Base.metadata.create_all(bind=database.engine)
setup_logging()

async def lifespan(app: FastAPI):
    logger.info("Application is starting up...")
    yield
    logger.info("Application is shutting down...")

app = FastAPI(title="RuleCheck", lifespan=lifespan)

app.include_router(healthcheck.router, prefix="/rulecheck", tags=["items"])
app.include_router(rules.router, prefix="/rulecheck/rules", tags=["rules"])
app.include_router(policies.router, prefix="/rulecheck/policies", tags=["policies"])
app.include_router(decisions.router, prefix="/rulecheck/decisions", tags=["decisions"])
app.include_router(action_submissions.router, prefix="/rulecheck/action_submissions", tags=["action_submissions"])
app.include_router(audit_events.router, prefix="/rulecheck/audit_events", tags=["audit_events"])