from sqlalchemy import Column, Integer, String, DateTime, func
from app.db.base import Base

## Something a user/system submits for evaluation.

class ActionSubmission(Base):
    __tablename__ = "action_submissions"

    id = Column(Integer, primary_key=True, index=True)
    submitted_by = Column(String, nullable=True)
    timestamp = Column(DateTime, server_default = func.now())