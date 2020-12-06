import httpx
import pytest
import fastapi.testclient

from . import main

from .redis_db import redis_db as redis
from .redis_db import async_redis_db as async_redis


@pytest.fixture
def redis_db():
    return redis.client


@pytest.fixture
def async_redis_db():
    async_redis.initialize()
    return async_redis.client


@pytest.fixture
def api():
    with fastapi.testclient.TestClient(main.app) as client:
        yield client


@pytest.fixture
def async_api() -> httpx.AsyncClient:
    return httpx.AsyncClient(app=main.app, base_url="http://test")
