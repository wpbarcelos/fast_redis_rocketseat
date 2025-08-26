from redis import Redis


class RedisConnectionHandle:

    def __init__(self) -> None:
        self.__redis_conn = None

    def connect(self) -> None:
        redis_conn = Redis(
            host="localhost",
            port=6379,
            db=0
        )
        self.__redis_conn = redis_conn
        return redis_conn

    def get_connection(self) -> Redis:
        return self.__redis_conn
