from typing import List, Optional

from fastapi import APIRouter, Depends, Query
from sqlalchemy import or_
from sqlalchemy.orm import Session

from app.database import get_db
from app.db_models.product import Product
from app.services.products import (
    get_product_model_or_404,
    get_product_or_404,
    products_to_dict,
)

router = APIRouter(prefix="/products", tags=["Products"])


def get_product_price_value(product: dict) -> float:
    discounted_price = product.get("discountedPrice") or 0
    return discounted_price if discounted_price > 0 else product["price"]


@router.get("")
def get_products(lang: str = Query("en"), db: Session = Depends(get_db)):
    products = db.query(Product).order_by(Product.id.asc()).all()
    return products_to_dict(products, lang)


@router.get("/filter")
def filter_products(
    category: Optional[str] = None,
    flavors: Optional[List[str]] = Query(None),
    tags: Optional[List[str]] = Query(None),
    sizes: Optional[List[str]] = Query(None),
    minPrice: Optional[float] = None,
    maxPrice: Optional[float] = None,
    sort: Optional[str] = None,
    lang: str = Query("en"),
    db: Session = Depends(get_db),
):
    db_products = db.query(Product).order_by(Product.id.asc()).all()

    if category:
        db_products = [
            product
            for product in db_products
            if product.category.lower() == category.lower()
        ]

    if flavors:
        flavors_lower = [flavor.lower() for flavor in flavors]
        db_products = [
            product
            for product in db_products
            if product.flavor.lower() in flavors_lower
        ]

    if tags:
        tags_lower = [tag.lower() for tag in tags]
        db_products = [
            product
            for product in db_products
            if any(tag.lower() in tags_lower for tag in product.tags or [])
        ]

    if sizes:
        sizes_lower = [size.lower() for size in sizes]
        db_products = [
            product
            for product in db_products
            if any(size["label"].lower() in sizes_lower for size in product.sizes or [])
        ]

    filtered_products = products_to_dict(db_products, lang)

    if minPrice is not None:
        filtered_products = [
            product
            for product in filtered_products
            if get_product_price_value(product) >= minPrice
        ]

    if maxPrice is not None:
        filtered_products = [
            product
            for product in filtered_products
            if get_product_price_value(product) <= maxPrice
        ]

    if sort == "priceLow":
        filtered_products = sorted(filtered_products, key=get_product_price_value)

    elif sort == "priceHigh":
        filtered_products = sorted(
            filtered_products,
            key=get_product_price_value,
            reverse=True,
        )

    elif sort == "ratingHigh":
        filtered_products = sorted(
            filtered_products,
            key=lambda product: product["rating"],
            reverse=True,
        )

    elif sort == "newest":
        filtered_products = [
            product for product in filtered_products if product.get("isNewArrival")
        ]

    elif sort == "bestSeller":
        filtered_products = [
            product for product in filtered_products if product.get("isBestSeller")
        ]

    return filtered_products


@router.get("/new-arrivals")
def get_new_arrivals_products(lang: str = Query("en"), db: Session = Depends(get_db)):
    products = (
        db.query(Product)
        .filter(Product.isNewArrival.is_(True))
        .order_by(Product.id.asc())
        .all()
    )
    return products_to_dict(products, lang)


@router.get("/top-rated")
def get_top_rated_products(lang: str = Query("en"), db: Session = Depends(get_db)):
    products = (
        db.query(Product)
        .filter(Product.isTopRated.is_(True))
        .order_by(Product.rating.desc())
        .all()
    )
    return products_to_dict(products, lang)


@router.get("/best-seller")
def get_best_seller_products(lang: str = Query("en"), db: Session = Depends(get_db)):
    products = (
        db.query(Product)
        .filter(Product.isBestSeller.is_(True))
        .order_by(Product.id.asc())
        .all()
    )
    return products_to_dict(products, lang)


@router.get("/limited-edition")
def get_limited_edition_products(
    lang: str = Query("en"),
    db: Session = Depends(get_db),
):
    products = (
        db.query(Product)
        .filter(Product.isLimitedEdition.is_(True))
        .order_by(Product.id.asc())
        .all()
    )
    return products_to_dict(products, lang)


@router.get("/search")
def search_products(
    q: Optional[str] = Query(None),
    lang: str = Query("en"),
    db: Session = Depends(get_db),
):
    query = db.query(Product)

    if q:
        keyword = f"%{q.strip()}%"
        query = query.filter(
            or_(
                Product.title.ilike(keyword),
                Product.titleAz.ilike(keyword),
                Product.titlePl.ilike(keyword),
                Product.category.ilike(keyword),
                Product.categoryAz.ilike(keyword),
                Product.categoryPl.ilike(keyword),
                Product.flavor.ilike(keyword),
                Product.flavorAz.ilike(keyword),
                Product.flavorPl.ilike(keyword),
            )
        )

    products = query.order_by(Product.id.asc()).all()
    return products_to_dict(products, lang)


@router.get("/{product_id}/related")
def get_related_products(
    product_id: int,
    limit: int = Query(8, ge=1, le=20),
    lang: str = Query("en"),
    db: Session = Depends(get_db),
):
    current_product = get_product_model_or_404(db, product_id)
    products = db.query(Product).order_by(Product.id.asc()).all()

    related_products = []
    used_ids = {product_id}

    for product in products:
        if (
            product.id not in used_ids
            and product.category.lower() == current_product.category.lower()
        ):
            related_products.append(product)
            used_ids.add(product.id)

            if len(related_products) >= limit:
                return products_to_dict(related_products, lang)

    for product in products:
        if (
            product.id not in used_ids
            and product.flavor.lower() == current_product.flavor.lower()
        ):
            related_products.append(product)
            used_ids.add(product.id)

            if len(related_products) >= limit:
                return products_to_dict(related_products, lang)

    for product in products:
        if product.id not in used_ids:
            related_products.append(product)
            used_ids.add(product.id)

            if len(related_products) >= limit:
                return products_to_dict(related_products, lang)

    return products_to_dict(related_products, lang)


@router.get("/{product_id}")
def get_product_by_id(
    product_id: int,
    lang: str = Query("en"),
    db: Session = Depends(get_db),
):
    return get_product_or_404(db, product_id, lang)