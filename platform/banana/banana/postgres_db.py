from __future__ import annotations

from typing import Generator

from pydantic import Field
from pydantic import BaseSettings

from sqlalchemy.orm import declarative_base
from sqlalchemy.ext.asyncio import engine
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine


SQLALCHEMY_DATABASE_URL = "postgresql+asyncpg://{postgres_user}:{postgres_password}@{postgres_host}:{postgres_port}/{postgres_db}"


class PostgresSettings(BaseSettings):
    postgres_user: str = Field(env="POSTGRES_USER")
    postgres_password: str = Field(env="POSTGRES_PASSWORD")
    postgres_db: str = Field(env="POSTGRES_DB")
    postgres_port: str = Field(env="POSTGRES_PORT")
    postgres_host: str = Field(env="POSTGRES_HOST")


class AlchemySettings:

    def __init__(self):
        self.db_url = None
        self._alchemy_base = None
        self._alchemy_engine = None

        self.generate()

    def generate(self) -> None:
        postgres = PostgresSettings()
        self.db_url = SQLALCHEMY_DATABASE_URL.format(**postgres.dict())
        self._alchemy_base = declarative_base()
        self._alchemy_engine = create_async_engine(self.db_url)

    def get_base(self) -> declarative_base:
        if self._alchemy_base is None:
            self.generate()
        return self._alchemy_base

    def get_engine(self) -> engine:
        if self._alchemy_engine is None:
            self.generate()
        return self._alchemy_engine


alchemy_settings = AlchemySettings()


# Dependency
async def get_db() -> Generator[AsyncSession, None, None]:
    session = AsyncSession(alchemy_settings.get_engine())
    try:
        yield session
    finally:
        await session.close()
