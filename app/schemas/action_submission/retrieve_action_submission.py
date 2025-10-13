from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class ActionSubmissionBase(BaseModel):
    submitted_by: str
    action_type: str
    amount: float
    expense_category: str
    detail: Optional[str] = None
    purchase_date: datetime
