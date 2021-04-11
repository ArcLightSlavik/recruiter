import httpx
import pytest
import fastapi.testclient

from . import main


@pytest.fixture
def api():
    with fastapi.testclient.TestClient(main.app) as client:
        yield client


@pytest.fixture
def async_api() -> httpx.AsyncClient:
    return httpx.AsyncClient(app=main.app, base_url="https://test")
