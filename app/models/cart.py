from pydantic import BaseModel, Field


class CartItemCreate(BaseModel):
    productId: int
    quantity: int = Field(default=1, ge=1)
    size: str | None = None


class CartItemUpdate(BaseModel):
    quantity: int = Field(..., ge=1)
    size: str | None = None


class CartActionResponse(BaseModel):
    message: str
    productId: int | None = None
