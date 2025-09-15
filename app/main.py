from fastapi import FastAPI
from .api.monitoring import healthcheck
from .api import action_submissions, audit_events, decisions, policies, rules
from .db import model, database

model.Base.metadata.create_all(bind=database.engine)

app = FastAPI(title="RuleCheck")

app.include_router(healthcheck.router, prefix="/rulecheck", tags=["items"])
app.include_router(rules.router, prefix="/rulecheck/rules", tags=["rules"])
app.include_router(policies.router, prefix="/rulecheck/policies", tags=["policies"])
app.include_router(decisions.router, prefix="/rulecheck/decisions", tags=["decisions"])
app.include_router(action_submissions.router, prefix="/rulecheck/action_submissions", tags=["action_submissions"])
app.include_router(audit_events.router, prefix="/rulecheck/audit_events", tags=["audit_events"])