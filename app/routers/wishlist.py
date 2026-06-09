from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from app.core.security import get_current_user
from app.database import get_db
from app.db_models.user import User
from app.db_models.wishlist import WishlistItem
from app.models.wishlist import WishlistActionResponse
from app.services.products import (
    get_product_or_404,
    get_product_with_quantity,
)

router = APIRouter(prefix="/wishlist", tags=["Wishlist"])


@router.get("")
def get_wishlist(
    lang: str = Query("en"),
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    wishlist_items = (
        db.query(WishlistItem)
        .filter(WishlistItem.userId == current_user.id)
        .order_by(WishlistItem.createdAt.desc())
        .all()
    )

    products = []

    for item in wishlist_items:
        product = get_product_with_quantity(
            db=db,
            product_id=item.productId,
            quantity=1,
            lang=lang,
        )

        if product:
            products.append(product)

    return products


@router.post(
    "/{product_id}",
    response_model=WishlistActionResponse,
    status_code=201,
)
def add_to_wishlist(
    product_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    get_product_or_404(
        db=db,
        product_id=product_id,
    )

    existing_item = (
        db.query(WishlistItem)
        .filter(
            WishlistItem.userId == current_user.id,
            WishlistItem.productId == product_id,
        )
        .first()
    )

    if existing_item:
        return {
            "message": "Product already exists in wishlist",
            "productId": product_id,
        }

    wishlist_item = WishlistItem(
        userId=current_user.id,
        productId=product_id,
    )

    db.add(wishlist_item)
    db.commit()

    return {
        "message": "Product added to wishlist",
        "productId": product_id,
    }


@router.delete(
    "/{product_id}",
    response_model=WishlistActionResponse,
)
def remove_from_wishlist(
    product_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    wishlist_item = (
        db.query(WishlistItem)
        .filter(
            WishlistItem.userId == current_user.id,
            WishlistItem.productId == product_id,
        )
        .first()
    )

    if not wishlist_item:
        raise HTTPException(
            status_code=404,
            detail="Product is not in wishlist",
        )

    db.delete(wishlist_item)
    db.commit()

    return {
        "message": "Product removed from wishlist",
        "productId": product_id,
    }
    