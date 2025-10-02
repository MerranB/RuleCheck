from pydantic import BaseModel, field_validator
from datetime import datetime
from typing import Optional

from app.utils.sanitize import sanitize_string, enforce_positive


class ActionSubmissionBase(BaseModel):
    action_type: str
    amount: float
    detail: Optional[str] = None
    expense_category: str
    location: Optional[str] = None
    purchase_date: datetime
    purchase_type: str
    user_id: str
    vendor: str

    # 🔹 Apply sanitization to all string fields
    @field_validator(
        "user_id",
        "action_type",
        "expense_category",
        "purchase_type",
        "vendor",
        "location",
        "detail",
    )
    @classmethod
    def sanitize_strings(cls, v):
        return sanitize_string(v)

    @field_validator("amount")
    @classmethod
    def validate_amount(cls, v):
        return enforce_positive(v)


class ActionSubmissionCreate(ActionSubmissionBase):
    pass


class ActionSubmissionRead(ActionSubmissionBase):
    id: int
    submitted_at: datetime

    class Config:
        orm_mode = True
