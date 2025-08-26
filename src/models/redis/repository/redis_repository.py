from redis import Redis

from .interfaces.redis_repository import RedisRepositoryInterface


class RedisRepository(RedisRepositoryInterface):

    def __init__(self, redis_conn: Redis) -> None:
        self.__redis_conn = redis_conn

    def insert(self, key, value):
        self.__redis_conn.set(key, value)

    def get_key(self, key):
        value = self.__redis_conn.get(key)
        if value:
            return value.decode('utf-8')
        return None

    def insert_hash(self, key, field, value):
        self.__redis_conn.hset(key, field, value)

    def get_hash(self, key, field):
        value = self.__redis_conn.hget(key, field)
        if value:
            return value.decode('utf-8')
        return None

    def insert_ex(self, key, value, ex):
        self.__redis_conn.set(key, value, ex=ex)

    def insert_hash_ex(self, key, field, value, ex):
        self.__redis_conn.hset(key, field, value)
        self.__redis_conn.expire(key, ex)
