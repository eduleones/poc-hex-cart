import redis

from src.adapters.db.base import BaseCartRepository
from src.settings import settings


class RedisCartRepository(BaseCartRepository):
    def create_client(self):
        return redis.Redis(
            host=settings.REDIS_HOST, port=settings.REDIS_PORT, db=self.db
        )
