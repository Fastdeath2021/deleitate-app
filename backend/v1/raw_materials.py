from flask import Blueprint, request

raw_materials_bp = Blueprint("raw_materials", __name__)

@raw_materials_bp.route("/", methods=["POST"])
def create_material():
    data = request.get_json()
    return {"message": "Materia prima creada", "data": data}, 201

@raw_materials_bp.route("/", methods=["GET"])
def get_materials():
    return {"message": "Lista de materias primas"}

@raw_materials_bp.route("/<int:material_id>", methods=["PUT"])
def update_material(material_id):
    data = request.get_json()
    return {"message": f"Materia prima {material_id} actualizada", "data": data}

@raw_materials_bp.route("/<int:material_id>", methods=["DELETE"])
def delete_material(material_id):
    return {"message": f"Materia prima {material_id} eliminada"}