import fakeredis

from src.adapters.db.base import BaseCartRepository


class MockRedisCartRepository(BaseCartRepository):
    def create_client(self):
        return fakeredis.FakeStrictRedis()
