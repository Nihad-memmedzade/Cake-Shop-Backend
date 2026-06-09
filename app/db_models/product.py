from sqlalchemy import Boolean, Column, Float, Integer, String, Text
from sqlalchemy.dialects.postgresql import JSONB

from app.database import Base


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(180), nullable=False)
    titleAz = Column("titleAz", String(180), nullable=True)
    titlePl = Column("titlePl", String(180), nullable=True)
    quantity = Column(Integer, nullable=False, default=1)
    category = Column(String(100), nullable=False, index=True)
    categoryAz = Column("categoryAz", String(100), nullable=True)
    categoryPl = Column("categoryPl", String(100), nullable=True)
    flavor = Column(String(100), nullable=False, index=True)
    flavorAz = Column("flavorAz", String(100), nullable=True)
    flavorPl = Column("flavorPl", String(100), nullable=True)
    tags = Column(JSONB, nullable=False, default=list)
    price = Column(Float, nullable=False)
    discountedPrice = Column("discountedPrice", Float, nullable=False, default=0)
    rating = Column(Float, nullable=False, default=0)
    images = Column(JSONB, nullable=False, default=list)
    brand = Column(String(120), nullable=False)
    sizes = Column(JSONB, nullable=False, default=list)
    description = Column(Text, nullable=False)
    descriptionAz = Column("descriptionAz", Text, nullable=True)
    descriptionPl = Column("descriptionPl", Text, nullable=True)
    isNewArrival = Column("isNewArrival", Boolean, nullable=False, default=False)
    isTopRated = Column("isTopRated", Boolean, nullable=False, default=False)
    isBestSeller = Column("isBestSeller", Boolean, nullable=False, default=False)
    isLimitedEdition = Column("isLimitedEdition", Boolean, nullable=False, default=False)