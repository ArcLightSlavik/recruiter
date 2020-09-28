import jwt

from datetime import datetime
from datetime import timedelta

from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer

from . import user_crud
from .exceptions import CredentialsException

secret_key = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9"
algorithm = "HS256"

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/user/authenticate")


def create_access_token(data: dict, expires_delta: timedelta = None):
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=90)
    data.update(dict(exp=expire))
    encoded_jwt = jwt.encode(data, secret_key, algorithm=algorithm)
    return encoded_jwt


def decode_access_token(data: str):
    return jwt.decode(data, secret_key, algorithm=algorithm)


async def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = decode_access_token(data=token)
        username: str = payload.get("sub")
        if username is None:
            raise CredentialsException
    except jwt.PyJWTError:
        raise CredentialsException
    user = await user_crud.get_user_by_username(username)
    if user is None:
        raise CredentialsException
    return user
