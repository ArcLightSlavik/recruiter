import pytest
import httpx

from fastapi.testclient import TestClient

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
    return TestClient(main.app)


@pytest.fixture
def async_api():
    return httpx.AsyncClient(app=main.app, base_url="http://test")
