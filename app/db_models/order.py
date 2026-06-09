from sqlalchemy import Column, DateTime, Float, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.database import Base


class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    userId = Column(Integer, ForeignKey("users.id"), nullable=False, index=True)
    status = Column(String(40), nullable=False, default="pending")
    firstName = Column(String(80), nullable=False)
    lastName = Column(String(80), nullable=False)
    country = Column(String(80), nullable=False)
    city = Column(String(80), nullable=False)
    streetAddress = Column(String(180), nullable=False)
    postcode = Column(String(30), nullable=False)
    phone = Column(String(40), nullable=False)
    email = Column(String(160), nullable=False)
    paymentMethod = Column(String(80), nullable=False, default="cash_on_delivery")
    subtotal = Column(Float, nullable=False, default=0)
    shipping = Column(Float, nullable=False, default=0)
    vat = Column(Float, nullable=False, default=0)
    total = Column(Float, nullable=False, default=0)
    createdAt = Column(DateTime(timezone=True), server_default=func.now())

    items = relationship("OrderItem", cascade="all, delete-orphan", back_populates="order")


class OrderItem(Base):
    __tablename__ = "order_items"

    id = Column(Integer, primary_key=True, index=True)
    orderId = Column(Integer, ForeignKey("orders.id"), nullable=False, index=True)
    productId = Column(Integer, ForeignKey("products.id"), nullable=False)
    title = Column(String(160), nullable=False)
    image = Column(Text, nullable=True)
    price = Column(Float, nullable=False)
    quantity = Column(Integer, nullable=False, default=1)
    size = Column(String(40), nullable=True)
    subtotal = Column(Float, nullable=False, default=0)

    order = relationship("Order", back_populates="items")