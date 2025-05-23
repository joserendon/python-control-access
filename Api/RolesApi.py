from flask import Blueprint, request, jsonify
from Repositorios.RolesRepositorio import RolesRepositorio
from Utilidades.TokenRequiredDecorator import token_required

roles_api = Blueprint('roles_api', __name__)
repo = RolesRepositorio()

@roles_api.route('/roles', methods=['GET'])
@token_required
def listar_roles():
    roles = repo.obtener()
    return jsonify([role.to_dict() for role in roles])

@roles_api.route('/roles', methods=['POST'])
@token_required
def crear_rol():
    data = request.get_json()
    nombre  = data.get("nombre")
    resp = repo.insertar(nombre)
    return jsonify({"mensaje": resp})

@roles_api.route('/roles/<int:id>', methods=['PUT'])
@token_required
def actualizar_rol(id):
    if not id:
        return jsonify({"error": "ID es requerido"}), 400
    
    data = request.get_json() 
    nombre  = data.get("nombre")
    id_nuevo  = data.get("id")
    
    if id != id_nuevo:
        return jsonify({"error": "ID no coincide con el rol"}), 400

    resp = repo.actualizar(id, nombre)
    return jsonify({"mensaje": resp})

@roles_api.route('/roles/<int:id>', methods=['DELETE'])
@token_required
def eliminar_rol(id):
    resp = repo.eliminar(id)
    return jsonify({"mensaje": resp})