from pydantic import BaseModel, Field


class UserRegister(BaseModel):
    fullName: str = Field(..., min_length=2, max_length=80)
    email: str
    password: str = Field(..., min_length=6)


class UserLogin(BaseModel):
    email: str
    password: str


class UserPublic(BaseModel):
    id: int
    fullName: str
    email: str


class AuthResponse(BaseModel):
    accessToken: str
    tokenType: str = "bearer"
    user: UserPublic


class UpdateProfile(BaseModel):
    fullName: str = Field(..., min_length=2, max_length=80)
    email: str


class ChangePassword(BaseModel):
    currentPassword: str = Field(..., min_length=6)
    newPassword: str = Field(..., min_length=6)
