from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, func, JSON
from app.db.base import Base

## The result of evaluating an ActionSubmission against the Rules.


class Decision(Base):
    __tablename__ = "decisions"

    id = Column(Integer, primary_key=True, autoincrement=True)
    decision_type = Column(String, nullable=False)
    explanation = Column(String, nullable=False)
    timestamp = Column(DateTime, server_default=func.now())
    submission_id = Column(Integer, ForeignKey("action_submissions.id"), nullable=False)
    matched_rule_ids = Column(JSON, nullable=True)
