from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, UniqueConstraint
from sqlalchemy.sql import func

from app.database import Base


class CartItem(Base):
    __tablename__ = "cart_items"
    __table_args__ = (
        UniqueConstraint("userId", "productId", "size", name="unique_user_cart_product_size"),
    )

    id = Column(Integer, primary_key=True, index=True)
    userId = Column(Integer, ForeignKey("users.id"), nullable=False, index=True)
    productId = Column(Integer, ForeignKey("products.id"), nullable=False, index=True)
    quantity = Column(Integer, nullable=False, default=1)
    size = Column(String(40), nullable=True)
    createdAt = Column(DateTime(timezone=True), server_default=func.now())
