from typing import Optional, List
from pydantic import BaseModel
from datetime import datetime


class DecisionBase(BaseModel):
    decision_type: str
    explanation: str
    timestamp: datetime
    matched_rule_ids: Optional[List[int]]


class DecisionCreate(DecisionBase):
    submission_id: int  # 👈 This links the rule to a policy
