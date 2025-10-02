from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.db.base import Base

## A specific, enforceable condition derived from a Policy.


class Rule(Base):
    __tablename__ = "rules"

    id = Column(Integer, primary_key=True, autoincrement=True)

    action = Column(String, nullable=True)
    description = Column(String, nullable=True)
    expense_category = Column(String, nullable=True)
    field = Column(String, nullable=True)
    operator = Column(String, nullable=True)
    value = Column(String, nullable=True)

    policy_id = Column(
        Integer, ForeignKey("policies.id", ondelete="CASCADE"), nullable=False
    )
    policy = relationship("Policy", back_populates="rules")
