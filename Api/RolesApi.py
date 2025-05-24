from flask import Blueprint, request, jsonify
from Repositorios.RolesRepositorio import RolesRepositorio
from Utilidades.TokenRequiredDecorator import token_required

roles_api = Blueprint('roles_api', __name__)
repo = RolesRepositorio()

@roles_api.route('/roles', methods=['GET'])
@token_required
def listar():
    roles = repo.obtener()
    return jsonify([role.to_dict() for role in roles])

@roles_api.route('/roles', methods=['POST'])
@token_required
def crear():
    data = request.json

    if not data:
        return jsonify({"error": "Datos son requeridos"}), 400
    
    resp = repo.insertar(**data)
    return jsonify({"mensaje": resp})

@roles_api.route('/roles', methods=['PUT'])
@token_required
def actualizar():
    data = request.json

    if not data:
        return jsonify({"error": "Datos son requeridos"}), 400
    
    resp = repo.actualizar(**data)
    return jsonify({"mensaje": resp})

@roles_api.route('/roles/<int:id>', methods=['DELETE'])
@token_required
def eliminar(id):
    if not id:
        return jsonify({"error": "ID es requerido"}), 400
    resp = repo.eliminar(id)
    return jsonify({"mensaje": resp})