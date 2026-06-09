from pydantic import BaseModel, Field


class ReviewCreate(BaseModel):
    name: str = Field(..., min_length=2, max_length=80)
    email: str
    rating: int = Field(..., ge=1, le=5)
    text: str = Field(..., min_length=5, max_length=1000)


class ReviewPublic(BaseModel):
    id: int
    productId: int
    name: str
    rating: int
    text: str
    createdAt: str
