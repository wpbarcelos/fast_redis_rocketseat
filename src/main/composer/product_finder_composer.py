
from src.models.redis.repository.redis_repository import RedisRepository
from src.models.sqlite.repository.products_repository import ProductsRepository

from src.data.product_finder import ProductFinder


def product_finder_composer():
    from src.main.server.server_settings import redis_connection_handle, sqlite_connection_handle
    redis_conn = redis_connection_handle.get_connection()
    sqlite_conn = sqlite_connection_handle.get_connection()

    redis_repo = RedisRepository(redis_conn)
    product_repo = ProductsRepository(sqlite_conn)

    return ProductFinder(redis_repo, product_repo)
