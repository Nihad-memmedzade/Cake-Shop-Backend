from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.security import (
    create_access_token,
    get_current_user,
    hash_password,
    normalize_email,
    to_public_user,
    verify_password,
)
from app.database import get_db
from app.db_models.user import User
from app.models.auth import (
    AuthResponse,
    ChangePassword,
    UpdateProfile,
    UserLogin,
    UserPublic,
    UserRegister,
)

router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("/register", response_model=AuthResponse, status_code=201)
def register_user(user_data: UserRegister, db: Session = Depends(get_db)):
    email = normalize_email(user_data.email)
    existing_user = db.query(User).filter(User.email == email).first()

    if existing_user:
        raise HTTPException(status_code=409, detail="This email is already registered")

    user = User(
        fullName=user_data.fullName.strip(),
        email=email,
        passwordHash=hash_password(user_data.password),
    )
    db.add(user)
    db.commit()
    db.refresh(user)

    return {
        "accessToken": create_access_token(user.id),
        "tokenType": "bearer",
        "user": to_public_user(user),
    }


@router.post("/login", response_model=AuthResponse)
def login_user(login_data: UserLogin, db: Session = Depends(get_db)):
    email = normalize_email(login_data.email)
    user = db.query(User).filter(User.email == email).first()

    if not user or not verify_password(login_data.password, user.passwordHash):
        raise HTTPException(status_code=401, detail="Invalid email or password")

    return {
        "accessToken": create_access_token(user.id),
        "tokenType": "bearer",
        "user": to_public_user(user),
    }


@router.get("/me", response_model=UserPublic)
def get_me(current_user: User = Depends(get_current_user)):
    return to_public_user(current_user)


@router.put("/me/profile", response_model=UserPublic)
def update_profile(
    profile_data: UpdateProfile,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    new_email = normalize_email(profile_data.email)
    old_email = current_user.email
    existing_user = db.query(User).filter(User.email == new_email).first()

    if new_email != old_email and existing_user:
        raise HTTPException(status_code=409, detail="This email is already registered")

    current_user.fullName = profile_data.fullName.strip()
    current_user.email = new_email
    db.commit()
    db.refresh(current_user)

    return to_public_user(current_user)


@router.put("/me/password")
def change_password(
    password_data: ChangePassword,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    if not verify_password(
        password_data.currentPassword,
        current_user.passwordHash,
    ):
        raise HTTPException(status_code=400, detail="Current password is incorrect")

    current_user.passwordHash = hash_password(password_data.newPassword)
    db.commit()

    return {"message": "Password changed successfully"}

