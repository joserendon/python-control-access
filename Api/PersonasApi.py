from flask import Blueprint, request, jsonify
from Repositorios.PersonasRepositorio import PersonasRepositorio
from Utilidades.TokenRequiredDecorator import token_required

personas_api = Blueprint('personas_api', __name__)
repo = PersonasRepositorio()

@personas_api.route('/personas', methods=['GET'])
@token_required
def listar():
    personas = repo.obtener()
    return jsonify([p.to_dict() for p in personas])

@personas_api.route('/personas', methods=['POST'])
@token_required
def crear():
    data = request.json
    resp = repo.insertar(**data)
    return jsonify({"mensaje": resp})

@personas_api.route('/personas', methods=['PUT'])
@token_required
def actualizar():
    data = request.json
    resp = repo.actualizar(**data)
    return jsonify({"mensaje": resp})

@personas_api.route('/personas/<int:id>', methods=['DELETE'])
@token_required
def eliminar(id):
    if not id:
        return jsonify({"error": "ID es requerido"}), 400
    resp = repo.eliminar(id)
    return jsonify({"mensaje": resp})