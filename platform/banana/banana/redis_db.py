import os
import redis
import aredis

from .lazy import Lazy


class Redis:

    @Lazy
    def client(self) -> redis.StrictRedis:
        return redis.StrictRedis(host=os.environ['REDISHOST'], port=int(os.environ['REDISPORT']))


class AsyncRedis:
    _redis_client = None

    def initialize(self) -> None:
        self._redis_client = aredis.StrictRedis(host=os.environ['REDISHOST'], port=int(os.environ['REDISPORT']))

    @property
    def client(self) -> aredis.StrictRedis:
        if not self._redis_client:
            self.initialize()
        return self._redis_client


redis_db = Redis()
async_redis_db = AsyncRedis()
