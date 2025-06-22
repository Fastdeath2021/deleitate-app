from flask import Blueprint, request

products_bp = Blueprint("products", __name__)

@products_bp.route("/", methods=["POST"])
def create_product():
    data = request.get_json()
    return {"message": "Producto creado", "data": data}, 201

@products_bp.route("/", methods=["GET"])
def get_products():
    return {"message": "Lista de productos"}

@products_bp.route("/<int:product_id>", methods=["PUT"])
def update_product(product_id):
    data = request.get_json()
    return {"message": f"Producto {product_id} actualizado", "data": data}

@products_bp.route("/<int:product_id>", methods=["DELETE"])
def delete_product(product_id):
    return {"message": f"Producto {product_id} eliminado"}