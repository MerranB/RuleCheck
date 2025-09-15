from pydantic import BaseModel

class DecisionBase(BaseModel):
    name: str
    description: str | None = None


class DecisionCreate(DecisionBase):
    pass
