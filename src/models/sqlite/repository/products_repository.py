from sqlite3 import Connection as SqliteConnection

from .interfaces.products_interface import ProductsRepositoryInterface


class ProductsRepository(ProductsRepositoryInterface):

    def __init__(self, conn: SqliteConnection) -> None:
        self.__conn = conn

    def find_product_by_name(self, product_name) -> tuple:
        cursor = self.__conn.cursor()
        cursor.execute(
            "SELECT * FROM products WHERE name = ?",
            (product_name,)
        )
        product = cursor.fetchone()
        return product

    def insert_product(self, name, price, quantity) -> None:
        cursor = self.__conn.cursor()
        cursor.execute(
            """
            INSERT INTO products 
                (name, price, quantity)
            VALUES
                (?, ?, ?)
            """,
            (name,
             price,
             quantity,
             )
        )
        self.__conn.commit()

    def delete_product(self, id) -> None:
        cursor = self.__conn.cursor()
        cursor.execute(
            """
            DELETE FROM products where id = ? 
            """,
            (id,)
        )
        self.__conn.commit()
