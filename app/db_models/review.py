from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Text
from sqlalchemy.sql import func

from app.database import Base


class Review(Base):
    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True, index=True)
    productId = Column(Integer, ForeignKey("products.id"), index=True, nullable=False)
    userId = Column(Integer, ForeignKey("users.id"), nullable=True)
    name = Column(String(80), nullable=False)
    email = Column(String(160), nullable=False)
    rating = Column(Integer, nullable=False)
    text = Column(Text, nullable=False)
    createdAt = Column(DateTime(timezone=True), server_default=func.now())
