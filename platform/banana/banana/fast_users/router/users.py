from typing import Any, Dict, cast

from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import UUID4

from .. import models
from ..authentication import Authenticator
from ..password import get_password_hash

from ...users.models import user_db, User, UserUpdate, UserDB
from ...users.jwt import jwt_authentication

authenticator = Authenticator(jwt_authentication, user_db)
users_router = APIRouter()


async def _get_or_404(id: UUID4) -> models.BaseUserDB:
    user = await user_db.get(id)
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return user


async def _update_user(user: models.BaseUserDB, update_dict: Dict[str, Any]):
    for field in update_dict:
        if field == "password":
            hashed_password = get_password_hash(update_dict[field])
            user.hashed_password = hashed_password
        else:
            setattr(user, field, update_dict[field])
    updated_user = await user_db.update(user)
    return updated_user


@users_router.get("/me", response_model=User)
async def me(user: UserDB = Depends(authenticator.get_current_active_user)):
    return user


@users_router.patch("/me", response_model=User)
async def update_me(updated_user: UserUpdate, user: UserDB = Depends(authenticator.get_current_active_user)):
    updated_user = cast(models.BaseUserUpdate, updated_user)
    updated_user_data = updated_user.create_update_dict()
    updated_user = await _update_user(user, updated_user_data)

    return updated_user


@users_router.get("/{id}", response_model=User, dependencies=[Depends(authenticator.get_current_superuser)])
async def get_user(id: UUID4):
    return await _get_or_404(id)


@users_router.patch("/{id}", response_model=User, dependencies=[Depends(authenticator.get_current_superuser)])
async def update_user(id: UUID4, updated_user: UserUpdate):
    updated_user = cast(models.BaseUserUpdate, updated_user)
    user = await _get_or_404(id)
    updated_user_data = updated_user.create_update_dict_superuser()
    return await _update_user(user, updated_user_data)


@users_router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT, dependencies=[Depends(authenticator.get_current_superuser)])
async def delete_user(id: UUID4):
    user = await _get_or_404(id)
    await user_db.delete(user)
    return None
