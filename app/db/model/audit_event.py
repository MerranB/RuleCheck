from sqlalchemy import Column, Integer, String, DateTime, func
from app.db.base import Base

## A record of what happened — both the action submitted and the decision made.

class AuditEvent(Base):
    __tablename__ = "audit_events"

    id = Column(Integer, primary_key=True, index=True)
    submission_id = Column(String, unique=True, index=True, nullable=False)
    decision_id = Column(String, nullable=True)
    timestamp = Column(DateTime, server_default = func.now())
    explanation = Column(String, nullable=True)
    user = Column(String, nullable=True)