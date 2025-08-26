from src.models.sqlite.repository.interfaces.products_interface import ProductsRepositoryInterface
from src.models.redis.repository.interfaces.redis_repository import RedisRepositoryInterface


class ProductFinder:

    def __init__(self, redis_repo: RedisRepositoryInterface, product_repo: ProductsRepositoryInterface):

        self.__redis_repo = redis_repo
        self.__product_repo = product_repo

        pass
