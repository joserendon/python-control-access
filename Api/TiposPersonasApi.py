from flask import Blueprint, request, jsonify
from Repositorios.TiposPersonasRepositorio import TiposPersonasRepositorio
from Utilidades.TokenRequiredDecorator import token_required

tipos_personas_api = Blueprint('tipos_personas_api', __name__)
repo = TiposPersonasRepositorio()

@tipos_personas_api.route('/tipospersonas', methods=['GET'])
@token_required
def listar():
    tipos = repo.obtener()
    return jsonify([t.to_dict() for t in tipos])

@tipos_personas_api.route('/tipospersonas', methods=['POST'])
@token_required
def crear():
    data = request.json
    resp = repo.insertar(**data)
    return jsonify({"mensaje": resp})

@tipos_personas_api.route('/tipospersonas', methods=['PUT'])
@token_required
def actualizar():
    data = request.json
    resp = repo.actualizar(**data)
    return jsonify({"mensaje": resp})

@tipos_personas_api.route('/tipospersonas/<int:id>', methods=['DELETE'])
@token_required
def eliminar(id):
    if not id:
        return jsonify({"error": "ID es requerido"}), 400
    resp = repo.eliminar(id)
    return jsonify({"mensaje": resp})