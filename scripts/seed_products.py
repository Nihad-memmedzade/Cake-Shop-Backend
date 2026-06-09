import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[1]
sys.path.append(str(ROOT_DIR))

from app.data.products import products
from app.database import Base, SessionLocal, engine
from app.db_models import Product


PRODUCT_FIELDS = [
    "id",
    "title",
    "titleAz",
    "titlePl",
    "quantity",
    "category",
    "categoryAz",
    "categoryPl",
    "flavor",
    "flavorAz",
    "flavorPl",
    "tags",
    "price",
    "discountedPrice",
    "rating",
    "images",
    "brand",
    "sizes",
    "description",
    "descriptionAz",
    "descriptionPl",
    "isNewArrival",
    "isTopRated",
    "isBestSeller",
    "isLimitedEdition",
]


def normalize_product(product: dict) -> dict:
    return {
        field: product[field]
        for field in PRODUCT_FIELDS
        if field in product
    }


def seed_products() -> None:
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()

    try:
        for product_data in products:
            payload = normalize_product(product_data)

            product = (
                db.query(Product)
                .filter(Product.id == payload["id"])
                .first()
            )

            if product is None:
                db.add(Product(**payload))
                continue

            for key, value in payload.items():
                setattr(product, key, value)

        db.commit()
        print(f"{len(products)} products seeded successfully.")

    except Exception:
        db.rollback()
        raise

    finally:
        db.close()


if __name__ == "__main__":
    seed_products()
