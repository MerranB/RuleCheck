from sqlalchemy import Column, Integer, String
from app.db.base import Base

## The result of evaluating an ActionSubmission against the Rules.


class Decision(Base):
    __tablename__ = "decisions"

    id = Column(Integer, primary_key=True)
    submission_id = Column(String, unique=True, nullable=False)
    decision_type = Column(String, nullable=True)
    explanation = Column(String, nullable=True)
    rule_triggered = Column(String, nullable=True)
