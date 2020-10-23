import jwt
from fastapi import APIRouter, Body, HTTPException, status
from pydantic import UUID4, EmailStr

from ..password import get_password_hash
from .common import ErrorCode
from ..utils import JWT_ALGORITHM, generate_jwt
from ...users.models import user_db


reset_password_token_secret = "SECRET"
reset_password_token_lifetime_seconds: int = 3600
RESET_PASSWORD_TOKEN_AUDIENCE = "fastapi-users:reset"


reset_router = APIRouter()


@reset_router.post("/forgot-password", status_code=status.HTTP_202_ACCEPTED)
async def forgot_password(email: EmailStr = Body(..., embed=True)):
    user = await user_db.get_by_email(email)

    if user is not None and user.is_active:
        token_data = {"user_id": str(user.id), "aud": RESET_PASSWORD_TOKEN_AUDIENCE}
        token = generate_jwt(
            token_data,
            reset_password_token_lifetime_seconds,
            reset_password_token_secret,
        )

    return None

@reset_router.post("/reset-password")
async def reset_password(token: str = Body(...), password: str = Body(...)):
    try:
        data = jwt.decode(
            token,
            reset_password_token_secret,
            audience=RESET_PASSWORD_TOKEN_AUDIENCE,
            algorithms=[JWT_ALGORITHM],
        )
        user_id = data.get("user_id")
        if user_id is None:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=ErrorCode.RESET_PASSWORD_BAD_TOKEN,
            )

        try:
            user_uiid = UUID4(user_id)
        except ValueError:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=ErrorCode.RESET_PASSWORD_BAD_TOKEN,
            )

        user = await user_db.get(user_uiid)
        if user is None or not user.is_active:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=ErrorCode.RESET_PASSWORD_BAD_TOKEN,
            )

        user.hashed_password = get_password_hash(password)
        await user_db.update(user)
    except jwt.PyJWTError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=ErrorCode.RESET_PASSWORD_BAD_TOKEN,
        )
