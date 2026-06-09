import base64
import hashlib
import hmac
import json
import secrets
from datetime import datetime, timedelta, timezone

from fastapi import Depends, HTTPException
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from sqlalchemy.orm import Session

from app.core.config import ACCESS_TOKEN_EXPIRE_MINUTES, SECRET_KEY
from app.database import get_db
from app.db_models.user import User

security = HTTPBearer()


def _base64url_encode(data: bytes) -> str:
    return base64.urlsafe_b64encode(data).rstrip(b"=").decode("utf-8")


def _base64url_decode(data: str) -> bytes:
    padding = "=" * (-len(data) % 4)
    return base64.urlsafe_b64decode(data + padding)


def hash_password(password: str) -> str:
    salt = secrets.token_hex(16)
    password_hash = hashlib.pbkdf2_hmac(
        "sha256",
        password.encode("utf-8"),
        salt.encode("utf-8"),
        100_000,
    ).hex()

    return f"{salt}${password_hash}"


def verify_password(password: str, stored_hash: str) -> bool:
    try:
        salt, expected_hash = stored_hash.split("$", 1)
    except ValueError:
        return False

    password_hash = hashlib.pbkdf2_hmac(
        "sha256",
        password.encode("utf-8"),
        salt.encode("utf-8"),
        100_000,
    ).hex()

    return hmac.compare_digest(password_hash, expected_hash)


def create_access_token(user_id: int) -> str:
    header = {"alg": "HS256", "typ": "JWT"}

    payload = {
        "sub": str(user_id),
        "exp": int(
            (
                datetime.now(timezone.utc)
                + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
            ).timestamp()
        ),
    }

    header_encoded = _base64url_encode(
        json.dumps(header, separators=(",", ":")).encode()
    )
    payload_encoded = _base64url_encode(
        json.dumps(payload, separators=(",", ":")).encode()
    )

    signing_input = f"{header_encoded}.{payload_encoded}".encode("utf-8")

    signature = hmac.new(
        SECRET_KEY.encode("utf-8"),
        signing_input,
        hashlib.sha256,
    ).digest()

    return (
        f"{signing_input.decode('utf-8')}."
        f"{_base64url_encode(signature)}"
    )


def decode_access_token(token: str) -> dict:
    try:
        header_encoded, payload_encoded, signature_encoded = token.split(".")
        signing_input = f"{header_encoded}.{payload_encoded}".encode("utf-8")
        expected_signature = hmac.new(
            SECRET_KEY.encode("utf-8"),
            signing_input,
            hashlib.sha256,
        ).digest()
        actual_signature = _base64url_decode(signature_encoded)

        if not hmac.compare_digest(actual_signature, expected_signature):
            raise HTTPException(status_code=401, detail="Invalid token")

        payload = json.loads(_base64url_decode(payload_encoded))

        if payload.get("exp", 0) < int(datetime.now(timezone.utc).timestamp()):
            raise HTTPException(status_code=401, detail="Token expired")

        return payload

    except HTTPException:
        raise
    except Exception:
        raise HTTPException(status_code=401, detail="Invalid token")


def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security),
    db: Session = Depends(get_db),
) -> User:
    payload = decode_access_token(credentials.credentials)
    subject = payload.get("sub")

    try:
        user_id = int(subject)
    except (TypeError, ValueError):
        raise HTTPException(
            status_code=401,
            detail="Invalid token subject",
        )

    user = db.query(User).filter(User.id == user_id).first()

    if not user:
        raise HTTPException(
            status_code=401,
            detail="User not found",
        )

    return user


def normalize_email(email: str) -> str:
    normalized = email.lower().strip()

    if "@" not in normalized or "." not in normalized.split("@")[-1]:
        raise HTTPException(status_code=422, detail="Please enter a valid email address")

    return normalized


def to_public_user(user: User) -> dict:
    return {
        "id": user.id,
        "fullName": user.fullName,
        "email": user.email,
    }
