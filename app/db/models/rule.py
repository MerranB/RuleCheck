from sqlalchemy import Column, Integer, String
from app.db.base import Base

## A specific, enforceable condition derived from a Policy.


class Rule(Base):
    __tablename__ = "rules"

    id = Column(Integer, primary_key=True)
    policy_id = Column(String, unique=True, nullable=False)
    condition = Column(String, nullable=True)
    action = Column(String, nullable=True)
    description = Column(String, nullable=True)
