from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.sql import func

from app.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    fullName = Column(String(80), nullable=False)
    email = Column(String(160), unique=True, index=True, nullable=False)
    passwordHash = Column(String(255), nullable=False)
    createdAt = Column(DateTime(timezone=True), server_default=func.now())
