from pydantic import BaseModel, ConfigDict


class RuleBase(BaseModel):
    action: str
    description: str
    expense_category: str
    field: str
    operator: str
    value: str


class RuleCreate(RuleBase):
    policy_id: int  # 👈 This links the rule to a policy


class RuleRead(RuleBase):
    id: int
    policy_id: int  # 👈 Show the parent Policy id when reading
    model_config = ConfigDict(from_attributes=True)
