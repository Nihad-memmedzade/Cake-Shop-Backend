from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from app.core.security import get_current_user
from app.database import get_db
from app.db_models.cart import CartItem
from app.db_models.user import User
from app.models.cart import (
    CartActionResponse,
    CartItemCreate,
    CartItemUpdate,
)
from app.services.products import (
    get_product_or_404,
    get_product_with_quantity,
)

router = APIRouter(prefix="/cart", tags=["Cart"])


@router.get("")
def get_cart(
    lang: str = Query("en"),
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    cart_items = (
        db.query(CartItem)
        .filter(CartItem.userId == current_user.id)
        .order_by(CartItem.createdAt.desc())
        .all()
    )

    products = []

    for item in cart_items:
        product = get_product_with_quantity(
            db=db,
            product_id=item.productId,
            quantity=item.quantity,
            size=item.size,
            lang=lang,
        )

        if product:
            products.append(product)

    return products


@router.post("", status_code=201)
def add_to_cart(
    cart_data: CartItemCreate,
    lang: str = Query("en"),
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    get_product_or_404(
        db=db,
        product_id=cart_data.productId,
        lang=lang,
    )

    normalized_size = (
        cart_data.size.strip()
        if cart_data.size
        else None
    )

    existing_item = (
        db.query(CartItem)
        .filter(
            CartItem.userId == current_user.id,
            CartItem.productId == cart_data.productId,
            CartItem.size == normalized_size,
        )
        .first()
    )

    if existing_item:
        existing_item.quantity += cart_data.quantity

        db.commit()
        db.refresh(existing_item)

        return get_product_with_quantity(
            db=db,
            product_id=existing_item.productId,
            quantity=existing_item.quantity,
            size=existing_item.size,
            lang=lang,
        )

    cart_item = CartItem(
        userId=current_user.id,
        productId=cart_data.productId,
        quantity=cart_data.quantity,
        size=normalized_size,
    )

    db.add(cart_item)
    db.commit()
    db.refresh(cart_item)

    return get_product_with_quantity(
        db=db,
        product_id=cart_item.productId,
        quantity=cart_item.quantity,
        size=cart_item.size,
        lang=lang,
    )


@router.put("/{product_id}")
def update_cart_item(
    product_id: int,
    cart_data: CartItemUpdate,
    lang: str = Query("en"),
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    normalized_size = (
        cart_data.size.strip()
        if cart_data.size
        else None
    )

    cart_item = (
        db.query(CartItem)
        .filter(
            CartItem.userId == current_user.id,
            CartItem.productId == product_id,
            CartItem.size == normalized_size,
        )
        .first()
    )

    if not cart_item:
        raise HTTPException(
            status_code=404,
            detail="Product is not in cart",
        )

    cart_item.quantity = cart_data.quantity

    db.commit()
    db.refresh(cart_item)

    return get_product_with_quantity(
        db=db,
        product_id=cart_item.productId,
        quantity=cart_item.quantity,
        size=cart_item.size,
        lang=lang,
    )


@router.delete(
    "/{product_id}",
    response_model=CartActionResponse,
)
def remove_from_cart(
    product_id: int,
    size: str | None = None,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    normalized_size = size.strip() if size else None

    cart_item = (
        db.query(CartItem)
        .filter(
            CartItem.userId == current_user.id,
            CartItem.productId == product_id,
            CartItem.size == normalized_size,
        )
        .first()
    )

    if not cart_item:
        raise HTTPException(
            status_code=404,
            detail="Product is not in cart",
        )

    db.delete(cart_item)
    db.commit()

    return {
        "message": "Product removed from cart",
        "productId": product_id,
    }


@router.delete("", response_model=CartActionResponse)
def clear_cart(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    (
        db.query(CartItem)
        .filter(CartItem.userId == current_user.id)
        .delete()
    )

    db.commit()

    return {
        "message": "Cart cleared",
        "productId": None,
    }