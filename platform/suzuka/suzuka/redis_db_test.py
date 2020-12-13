import pytest


def test_connection(redis_db):
    assert redis_db.set('test', 1) is True
    assert redis_db.incr('test') > 1


@pytest.mark.asyncio
async def test_async_connection(async_redis_db):
    assert await async_redis_db.set('test', 1) is True
    assert await async_redis_db.incr('test') > 1
