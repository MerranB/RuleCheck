from pydantic import BaseModel

class PolicyBase(BaseModel):
    name: str
    description: str | None = None


class PolicyCreate(PolicyBase):
    pass
