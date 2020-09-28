from typing import List

from fastapi import Depends
from fastapi import APIRouter
from fastapi import HTTPException

from . import user_crud
from .jwt import get_current_user
from .jwt import create_access_token
from .user import User
from .user import UserIn
from .exceptions import CredentialsException

user_router = APIRouter()


@user_router.post("/user/create", response_model=User)
async def create_user(user: UserIn):
    db_user = await user_crud.create_user(user)
    if not db_user:
        raise HTTPException(status_code=400, detail="Choose different data")
    return db_user


@user_router.post("/user/authenticate")
async def authenticate_user(user: UserIn):
    db_user = await user_crud.get_user_by_username(user.username)
    if not db_user:
        raise CredentialsException

    correct_password = await user_crud.check_user_password(user)
    if correct_password is False:
        raise CredentialsException

    access_token = create_access_token(dict(sub=user.username))
    return dict(access_token=access_token, token_type="Bearer")


@user_router.get("/user/all_users", response_model=List[User])
async def get_all_users():
    return await user_crud.get_all_users()


@user_router.get("/user/info", response_model=User)
async def get_user_by_id(current_user: User = Depends(get_current_user)):
    db_user = await user_crud.get_user_by_id(current_user.id)
    if not db_user:
        raise HTTPException(status_code=404, detail=f'User not found')
    return db_user


@user_router.put("/user/update", response_model=User)
async def update_user(updated_user: UserIn, current_user: User = Depends(get_current_user)):
    db_user = await user_crud.update_user(current_user.id, updated_user)
    if not db_user:
        raise HTTPException(status_code=404, detail=f'User not found')
    return db_user


@user_router.delete("/user/delete")
async def delete_user(current_user: User = Depends(get_current_user)):
    deleted_count = await user_crud.delete_user(current_user.id)
    if not deleted_count:
        raise HTTPException(status_code=404, detail=f"User not found")
    return dict(message=f"Deleted user")
