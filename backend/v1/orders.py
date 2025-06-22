from flask import Blueprint, request

orders_bp = Blueprint("orders", __name__)

@orders_bp.route("/", methods=["POST"])
def create_order():
    data = request.get_json()
    return {"message": "Pedido creado", "data": data}, 201

@orders_bp.route("/", methods=["GET"])
def get_orders():
    return {"message": "Lista de pedidos"}

@orders_bp.route("/<int:order_id>", methods=["PUT"])
def update_order(order_id):
    data = request.get_json()
    return {"message": f"Pedido {order_id} actualizado", "data": data}

@orders_bp.route("/<int:order_id>", methods=["DELETE"])
def delete_order(order_id):
    return {"message": f"Pedido {order_id} eliminado"}