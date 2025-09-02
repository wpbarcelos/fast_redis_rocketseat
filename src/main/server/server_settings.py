from flask import Flask
from src.main.routes.products_routes import products_route_bp

from src.models.sqlite.settings.connection import SqliteConnectionHandle
from src.models.redis.settings.connection import RedisConnectionHandle

redis_connection_handle = RedisConnectionHandle()
sqlite_connection_handle = SqliteConnectionHandle()

redis_connection_handle.connect()
sqlite_connection_handle.connect()

app = Flask(__name__)

app.register_blueprint(products_route_bp)
