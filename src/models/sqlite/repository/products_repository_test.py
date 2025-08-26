import pytest

from src.models.sqlite.settings.connection import SqliteConnectionHandle
from .products_repository import ProductsRepository


conn_handle = SqliteConnectionHandle()
conn = conn_handle.connect()


@pytest.mark.skip(reason="interaction with database")
def test_insert_product():
    repo = ProductsRepository(conn)

    repo.insert_product(name="power notebook", price=199.99, quantity=100)

    id, name, price, quantity = repo.find_product_by_name(
        product_name="power notebook")

    assert name == 'power notebook'
    assert price == 199.99
    assert quantity == 100

    repo.delete_product(id)

    response = repo.find_product_by_name(product_name="power notebook")

    assert response is None
    # assert product['name'] == 'power notebook'
