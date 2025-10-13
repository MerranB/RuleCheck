from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship

from app.db.base import Base

## A high-level document


class Policy(Base):
    __tablename__ = "policies"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, unique=True, nullable=False)
    description = Column(String, nullable=True)
    version = Column(String, nullable=True)
    effective_date = Column(DateTime, nullable=False)

    rules = relationship("Rule", back_populates="policy", cascade="all, delete-orphan")
