from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.security import normalize_email
from app.database import get_db
from app.db_models.review import Review
from app.models.review import ReviewCreate, ReviewPublic
from app.services.products import get_product_model_or_404, get_product_or_404

router = APIRouter(prefix="/products", tags=["Reviews"])


def review_to_public(review: Review) -> dict:
    return {
        "id": review.id,
        "productId": review.productId,
        "name": review.name,
        "rating": review.rating,
        "text": review.text,
        "createdAt": review.createdAt.isoformat() if review.createdAt else "",
    }


def update_product_rating(product_id: int, db: Session):
    product = get_product_model_or_404(db, product_id)

    product_reviews = db.query(Review).filter(Review.productId == product_id).all()

    if not product_reviews:
        return

    average_rating = sum(review.rating for review in product_reviews) / len(product_reviews)
    product.rating = round(average_rating, 1)
    db.commit()


@router.get("/{product_id}/reviews", response_model=List[ReviewPublic])
def get_product_reviews(product_id: int, db: Session = Depends(get_db)):
    get_product_or_404(db, product_id)
    reviews = (
        db.query(Review)
        .filter(Review.productId == product_id)
        .order_by(Review.createdAt.desc())
        .all()
    )

    return [review_to_public(review) for review in reviews]


@router.post("/{product_id}/reviews", response_model=ReviewPublic, status_code=201)
def create_product_review(
    product_id: int,
    review_data: ReviewCreate,
    db: Session = Depends(get_db),
):
    get_product_or_404(db, product_id)

    email = normalize_email(review_data.email)

    review = Review(
        productId=product_id,
        name=review_data.name.strip(),
        email=email,
        rating=review_data.rating,
        text=review_data.text.strip(),
    )
    db.add(review)
    db.commit()
    db.refresh(review)
    update_product_rating(product_id, db)

    return review_to_public(review)
