import pytest


@pytest.mark.asyncio
async def test_root(async_api):
    response = await async_api.get('/')
    response.raise_for_status()
    response_json = response.json()
    assert response_json == {"message": "OK"}


@pytest.mark.asyncio
async def test_health(async_api):
    response = await async_api.get('/health')
    response.raise_for_status()
    response_json = response.json()
    assert response_json == {"message": "OK"}


@pytest.mark.asyncio
async def test_version(async_api):
    response = await async_api.get('/version')
    response.raise_for_status()
    response_json = response.json()
    result = response_json['version'].split(':')[0]
    assert result == 'zeppelin-1912/suzuka'
