from pydantic import BaseModel

class ActionSubmissionBase(BaseModel):
    name: str
    description: str | None = None


class ActionSubmissionCreate(ActionSubmissionBase):
    pass
