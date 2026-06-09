from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from app.core.security import get_current_user, normalize_email
from app.database import get_db
from app.db_models.cart import CartItem
from app.db_models.order import Order, OrderItem
from app.db_models.user import User
from app.models.order import OrderCreate, OrderPublic
from app.services.products import find_product, get_product_price

router = APIRouter(prefix="/orders", tags=["Orders"])


def order_item_to_public(db: Session, item: OrderItem, lang: str) -> dict:
    product = find_product(db, item.productId, lang)

    return {
        "id": item.id,
        "productId": item.productId,
        "title": product["title"] if product else item.title,
        "image": item.image,
        "price": item.price,
        "quantity": item.quantity,
        "size": item.size,
        "subtotal": item.subtotal,
    }


def order_to_public(db: Session, order: Order, lang: str = "en") -> dict:
    return {
        "id": order.id,
        "status": order.status,
        "firstName": order.firstName,
        "lastName": order.lastName,
        "country": order.country,
        "city": order.city,
        "streetAddress": order.streetAddress,
        "postcode": order.postcode,
        "phone": order.phone,
        "email": order.email,
        "paymentMethod": order.paymentMethod,
        "subtotal": order.subtotal,
        "shipping": order.shipping,
        "vat": order.vat,
        "total": order.total,
        "createdAt": order.createdAt.isoformat() if order.createdAt else "",
        "items": [
            order_item_to_public(db, item, lang)
            for item in order.items
        ],
    }


@router.get("", response_model=list[OrderPublic])
def get_orders(
    lang: str = Query("en"),
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    orders = (
        db.query(Order)
        .filter(Order.userId == current_user.id)
        .order_by(Order.createdAt.desc())
        .all()
    )

    return [order_to_public(db, order, lang) for order in orders]


@router.get("/{order_id}", response_model=OrderPublic)
def get_order_by_id(
    order_id: int,
    lang: str = Query("en"),
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    order = (
        db.query(Order)
        .filter(Order.id == order_id, Order.userId == current_user.id)
        .first()
    )

    if not order:
        raise HTTPException(status_code=404, detail="Order not found")

    return order_to_public(db, order, lang)


@router.post("", response_model=OrderPublic, status_code=201)
def create_order(
    order_data: OrderCreate,
    lang: str = Query("en"),
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    email = normalize_email(order_data.billingDetails.email)
    incoming_items = order_data.items or []

    if not incoming_items:
        cart_items = db.query(CartItem).filter(CartItem.userId == current_user.id).all()
        incoming_items = [
            {
                "productId": item.productId,
                "quantity": item.quantity,
                "size": item.size,
            }
            for item in cart_items
        ]

    if not incoming_items:
        raise HTTPException(status_code=400, detail="Order items are required")

    subtotal = 0.0
    order_items: list[OrderItem] = []

    for item in incoming_items:
        product_id = item["productId"] if isinstance(item, dict) else item.productId
        quantity = item["quantity"] if isinstance(item, dict) else item.quantity
        size = item.get("size") if isinstance(item, dict) else item.size

        product = find_product(db, product_id, lang)

        if product is None:
            raise HTTPException(status_code=404, detail=f"Product {product_id} not found")

        price = get_product_price(product)
        item_subtotal = price * quantity
        subtotal += item_subtotal

        order_items.append(
            OrderItem(
                productId=product_id,
                title=product["title"],
                image=product["images"][0] if product.get("images") else None,
                price=price,
                quantity=quantity,
                size=size,
                subtotal=item_subtotal,
            )
        )

    shipping = 0.0
    vat = round(subtotal * 0.05, 2)
    total = round(subtotal + shipping + vat, 2)
    billing = order_data.billingDetails

    order = Order(
        userId=current_user.id,
        status="pending",
        firstName=billing.firstName.strip(),
        lastName=billing.lastName.strip(),
        country=billing.country.strip(),
        city=billing.city.strip(),
        streetAddress=billing.streetAddress.strip(),
        postcode=billing.postcode.strip(),
        phone=billing.phone.strip(),
        email=email,
        paymentMethod=order_data.paymentMethod,
        subtotal=round(subtotal, 2),
        shipping=shipping,
        vat=vat,
        total=total,
        items=order_items,
    )

    db.add(order)
    db.query(CartItem).filter(CartItem.userId == current_user.id).delete()
    db.commit()
    db.refresh(order)

    return order_to_public(db, order, lang)