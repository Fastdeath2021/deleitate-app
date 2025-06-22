from flask import Blueprint, request

users_bp = Blueprint("users", __name__)

# CREATE
@users_bp.route("/", methods=["POST"])
def create_user():
    data = request.get_json()
    return {"message": "Usuario creado", "data": data}, 201

# READ
@users_bp.route("/", methods=["GET"])
def get_users():
    return {"message": "Lista de usuarios"}

# UPDATE
@users_bp.route("/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    data = request.get_json()
    return {"message": f"Usuario {user_id} actualizado", "data": data}

# DELETE
@users_bp.route("/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    return {"message": f"Usuario {user_id} eliminado"}