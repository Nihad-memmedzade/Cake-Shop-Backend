from collections.abc import Sequence

from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.db_models.product import Product

SUPPORTED_PRODUCT_LANGUAGES = {"en", "az", "pl"}


def normalize_product_language(lang: str | None) -> str:
    if not lang:
        return "en"

    normalized_lang = lang.lower().split("-")[0]
    return normalized_lang if normalized_lang in SUPPORTED_PRODUCT_LANGUAGES else "en"


def localized_value(product: Product, field: str, lang: str) -> str:
    if lang == "az":
        return getattr(product, f"{field}Az") or getattr(product, field)

    if lang == "pl":
        return getattr(product, f"{field}Pl") or getattr(product, field)

    return getattr(product, field)


def product_to_dict(product: Product, lang: str | None = "en") -> dict:
    product_lang = normalize_product_language(lang)

    return {
        "id": product.id,
        "title": localized_value(product, "title", product_lang),
        "quantity": product.quantity,
        "category": localized_value(product, "category", product_lang),
        "flavor": localized_value(product, "flavor", product_lang),
        "tags": product.tags or [],
        "price": product.price,
        "discountedPrice": product.discountedPrice,
        "rating": product.rating,
        "images": product.images or [],
        "brand": product.brand,
        "sizes": product.sizes or [],
        "description": localized_value(product, "description", product_lang),
        "isNewArrival": product.isNewArrival,
        "isTopRated": product.isTopRated,
        "isBestSeller": product.isBestSeller,
        "isLimitedEdition": product.isLimitedEdition,
    }


def products_to_dict(products: Sequence[Product], lang: str | None = "en") -> list[dict]:
    return [product_to_dict(product, lang) for product in products]


def find_product_model(db: Session, product_id: int) -> Product | None:
    return db.query(Product).filter(Product.id == product_id).first()


def find_product(db: Session, product_id: int, lang: str | None = "en") -> dict | None:
    product = find_product_model(db, product_id)
    return product_to_dict(product, lang) if product else None


def get_product_or_404(db: Session, product_id: int, lang: str | None = "en") -> dict:
    product = find_product(db, product_id, lang)

    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")

    return product


def get_product_model_or_404(db: Session, product_id: int) -> Product:
    product = find_product_model(db, product_id)

    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")

    return product


def get_product_price(product: dict) -> float:
    discounted_price = product.get("discountedPrice") or 0

    if discounted_price > 0:
        return float(discounted_price)

    return float(product["price"])


def get_product_with_quantity(
    db: Session,
    product_id: int,
    quantity: int,
    size: str | None = None,
    lang: str | None = "en",
) -> dict | None:
    product = find_product(db, product_id, lang)

    if product is None:
        return None

    return {
        **product,
        "quantity": quantity,
        "selectedSize": size,
    }