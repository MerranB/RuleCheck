from pydantic import BaseModel
from datetime import datetime


class PolicyBase(BaseModel):
    title: str
    description: str
    version: str
    effective_date: datetime


class PolicyCreate(PolicyBase):
    pass
