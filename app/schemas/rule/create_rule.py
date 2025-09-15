from pydantic import BaseModel

class RuleBase(BaseModel):
    name: str
    description: str | None = None


class RuleCreate(RuleBase):
    pass
