from flask import Blueprint, request, jsonify
from Repositorios.AccesosRepositorio import AccesosRepositorio
from Utilidades.TokenRequiredDecorator import token_required

accesos_api = Blueprint('accesos_api', __name__)
repo = AccesosRepositorio()

@accesos_api.route('/accesos', methods=['GET'])
@token_required
def listar():
    accesos = repo.obtener()
    return jsonify([a.to_dict() for a in accesos])

@accesos_api.route('/accesos', methods=['POST'])
@token_required
def crear():
    data = request.json
    resp = repo.insertar(**data)
    return jsonify({"mensaje": resp})

@accesos_api.route('/accesos', methods=['PUT'])
@token_required
def actualizar():
    data = request.json
    resp = repo.actualizar(**data)
    return jsonify({"mensaje": resp})

@accesos_api.route('/accesos/<int:id>', methods=['DELETE'])
@token_required
def eliminar(id):
    if not id:
        return jsonify({"error": "ID es requerido"}), 400
    resp = repo.eliminar(id)
    return jsonify({"mensaje": resp})