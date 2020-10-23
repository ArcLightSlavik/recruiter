from typing import Any, Optional, TypeVar, Generic

import jwt
from fastapi import Response
from fastapi.security import OAuth2PasswordBearer
from pydantic import UUID4

from ..db.tortoise import TortoiseUserDatabase
from ..models import BaseUserDB
from ..utils import JWT_ALGORITHM, generate_jwt

T = TypeVar("T")


class JWTAuthentication(Generic[T]):
    scheme: OAuth2PasswordBearer
    token_audience: str = "fastapi-users:auth"
    secret: str
    lifetime_seconds: int
    name: str
    logout: bool

    def __init__(self, secret: str, lifetime_seconds: int, tokenUrl: str = "/login", name: str = "jwt"):
        self.scheme = OAuth2PasswordBearer(tokenUrl, auto_error=False)
        self.secret = secret
        self.lifetime_seconds = lifetime_seconds
        self.name = name
        self.logout = False

    async def __call__(self, credentials: Optional[str], user_db: TortoiseUserDatabase) -> Optional[BaseUserDB]:
        if credentials is None:
            return None

        try:
            data = jwt.decode(
                credentials,
                self.secret,
                audience=self.token_audience,
                algorithms=[JWT_ALGORITHM],
            )
            user_id = data.get("user_id")
            if user_id is None:
                return None
        except jwt.PyJWTError:
            return None

        try:
            user_uiid = UUID4(user_id)
            return await user_db.get(user_uiid)
        except ValueError:
            return None

    async def get_login_response(self, user: BaseUserDB, response: Response) -> Any:
        token = await self._generate_token(user)
        return {"access_token": token, "token_type": "bearer"}

    async def _generate_token(self, user: BaseUserDB) -> str:
        data = {"user_id": str(user.id), "aud": self.token_audience}
        return generate_jwt(data, self.lifetime_seconds, self.secret, JWT_ALGORITHM)
