from sqlalchemy import Column, Integer, String, DateTime, func, JSON
from app.db.base import Base

## Something a user/system submits for evaluation.


class ActionSubmission(Base):
    __tablename__ = "action_submissions"

    id = Column(Integer, primary_key=True, autoincrement=True)
    timestamp = Column(DateTime, server_default=func.now(), nullable=False)

    action_type = Column(String, nullable=True)
    amount = Column(JSON, nullable=True)
    detail = Column(String, nullable=True)
    expense_category = Column(String, nullable=True)
    location = Column(String, nullable=True)
    purchase_date = Column(DateTime, nullable=False)
    purchase_type = Column(String, nullable=False)
    user_id = Column(String, nullable=True)
    vendor = Column(String, nullable=False)
