from pydantic import BaseModel


class WishlistActionResponse(BaseModel):
    message: str
    productId: int
