from flask import Blueprint, jsonify

products_route_bp = Blueprint("products_routes", __name__)


@products_route_bp.route('/products', methods=['POST'])
def insert_product():
    return jsonify({"msg": "produto cadastrado"}), 201


@products_route_bp.route('/products/<product_name>', methods=['GET'])
def search_product(product_name: str):
    return jsonify({"msg": f'produto {product_name}'}), 200
