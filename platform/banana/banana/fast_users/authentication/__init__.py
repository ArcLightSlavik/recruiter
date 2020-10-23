import re
from typing import Optional

from fastapi import HTTPException, status

from .jwt import JWTAuthentication
from ..db.tortoise import TortoiseUserDatabase
from ..models import BaseUserDB

INVALID_CHARS_PATTERN = re.compile(r"[^0-9a-zA-Z_]")
INVALID_LEADING_CHARS_PATTERN = re.compile(r"^[^a-zA-Z_]+")


def name_to_variable_name(name: str) -> str:
    """Transform a backend name string into a string safe to use as variable name."""
    name = re.sub(INVALID_CHARS_PATTERN, "", name)
    name = re.sub(INVALID_LEADING_CHARS_PATTERN, "", name)
    return name


class Authenticator:
    backends: JWTAuthentication
    user_db: TortoiseUserDatabase

    def __init__(self, backends: JWTAuthentication, user_db: TortoiseUserDatabase):
        self.backends = backends
        self.user_db = user_db

        async def get_optional_current_user(*args, **kwargs):
            return await self._authenticate(*args, **kwargs)

        async def get_optional_current_active_user(*args, **kwargs):
            user = await get_optional_current_user(*args, **kwargs)
            if not user or not user.is_active:
                return None
            return user

        async def get_optional_current_superuser(*args, **kwargs):
            user = await get_optional_current_active_user(*args, **kwargs)
            if not user or not user.is_superuser:
                return None
            return user

        async def get_current_user(*args, **kwargs):
            user = await get_optional_current_user(*args, **kwargs)
            if user is None:
                raise HTTPException(status.HTTP_401_UNAUTHORIZED)
            return user

        async def get_current_active_user(*args, **kwargs):
            user = await get_optional_current_active_user(*args, **kwargs)
            if user is None:
                raise HTTPException(status.HTTP_401_UNAUTHORIZED)
            return user

        async def get_current_superuser(*args, **kwargs):
            user = await get_optional_current_active_user(*args, **kwargs)
            if user is None:
                raise HTTPException(status.HTTP_401_UNAUTHORIZED)
            if not user.is_superuser:
                raise HTTPException(status.HTTP_403_FORBIDDEN)
            return user

        self.get_current_user = get_current_user
        self.get_current_active_user = get_current_active_user
        self.get_current_superuser = get_current_superuser
        self.get_optional_current_user = get_optional_current_user
        self.get_optional_current_active_user = get_optional_current_active_user
        self.get_optional_current_superuser = get_optional_current_superuser

    async def _authenticate(self, *args, **kwargs) -> Optional[BaseUserDB]:
        token: str = kwargs[name_to_variable_name(self.backends.name)]
        if token:
            user = await self.backends(token, self.user_db)
            if user is not None:
                return user
        return None
