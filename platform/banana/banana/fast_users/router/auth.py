from fastapi import APIRouter, Depends, HTTPException, Response, status
from fastapi.security import OAuth2PasswordRequestForm

from ..authentication import Authenticator
from .common import ErrorCode

from ...users.models import user_db
from ...users.jwt import jwt_authentication

authenticator = Authenticator(jwt_authentication, user_db)
auth_router = APIRouter()


@auth_router.post("/login")
async def login(response: Response, credentials: OAuth2PasswordRequestForm = Depends()):
    user = await user_db.authenticate(credentials)

    if user is None or not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=ErrorCode.LOGIN_BAD_CREDENTIALS,
        )

    return await jwt_authentication.get_login_response(user, response)


@auth_router.post("/logout")
async def logout(response: Response, user=Depends(authenticator.get_current_active_user)):
    return await jwt_authentication.get_logout_response(user, response)
