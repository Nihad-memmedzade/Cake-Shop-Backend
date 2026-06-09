from sqlalchemy import Column, DateTime, ForeignKey, Integer, UniqueConstraint
from sqlalchemy.sql import func

from app.database import Base


class WishlistItem(Base):
    __tablename__ = "wishlist_items"
    __table_args__ = (
        UniqueConstraint("userId", "productId", name="unique_user_wishlist_product"),
    )

    id = Column(Integer, primary_key=True, index=True)
    userId = Column(Integer, ForeignKey("users.id"), nullable=False, index=True)
    productId = Column(Integer, ForeignKey("products.id"), nullable=False, index=True)
    createdAt = Column(DateTime(timezone=True), server_default=func.now())
