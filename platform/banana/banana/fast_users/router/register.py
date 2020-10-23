from typing import cast

from fastapi import APIRouter, HTTPException, status

from .. import models
from ..password import get_password_hash
from .common import ErrorCode
from ...users.models import user_db, User, UserCreate, UserDB

register_router = APIRouter()


@register_router.post("/register", response_model=User, status_code=status.HTTP_201_CREATED)
async def register(user: UserCreate):
    user = cast(models.BaseUserCreate, user)
    existing_user = await user_db.get_by_email(user.email)

    if existing_user is not None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=ErrorCode.REGISTER_USER_ALREADY_EXISTS,
        )

    hashed_password = get_password_hash(user.password)
    db_user = UserDB(**user.create_update_dict(), hashed_password=hashed_password)
    created_user = await user_db.create(db_user)

    return created_user
