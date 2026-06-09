from pydantic import BaseModel, Field


class OrderBillingDetails(BaseModel):
    firstName: str = Field(..., min_length=2, max_length=80)
    lastName: str = Field(..., min_length=2, max_length=80)
    country: str = Field(..., min_length=2, max_length=80)
    city: str = Field(..., min_length=2, max_length=80)
    streetAddress: str = Field(..., min_length=3, max_length=180)
    postcode: str = Field(..., min_length=2, max_length=30)
    phone: str = Field(..., min_length=5, max_length=40)
    email: str


class OrderItemCreate(BaseModel):
    productId: int
    quantity: int = Field(..., ge=1)
    size: str | None = None


class OrderCreate(BaseModel):
    billingDetails: OrderBillingDetails
    items: list[OrderItemCreate] | None = None
    paymentMethod: str = "cash_on_delivery"


class OrderItemPublic(BaseModel):
    id: int
    productId: int
    title: str
    image: str | None = None
    price: float
    quantity: int
    size: str | None = None
    subtotal: float


class OrderPublic(BaseModel):
    id: int
    status: str
    firstName: str
    lastName: str
    country: str
    city: str
    streetAddress: str
    postcode: str
    phone: str
    email: str
    paymentMethod: str
    subtotal: float
    shipping: float
    vat: float
    total: float
    createdAt: str
    items: list[OrderItemPublic]
