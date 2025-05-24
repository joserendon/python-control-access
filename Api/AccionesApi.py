from flask import Blueprint, request, jsonify
from Repositorios.AccionesRepositorio import AccionesRepositorio
from Utilidades.TokenRequiredDecorator import token_required

acciones_api = Blueprint('acciones_api', __name__)
repo = AccionesRepositorio()

@acciones_api.route('/acciones', methods=['GET'])
@token_required
def listar():
    acciones = repo.obtener()
    return jsonify([a.to_dict() for a in acciones])

@acciones_api.route('/acciones', methods=['POST'])
@token_required
def crear():
    data = request.json
    resp = repo.insertar(**data)
    return jsonify({"mensaje": resp})

@acciones_api.route('/acciones', methods=['PUT'])
@token_required
def actualizar():
    data = request.json
    resp = repo.actualizar(**data)
    return jsonify({"mensaje": resp})

@acciones_api.route('/acciones/<int:id>', methods=['DELETE'])
@token_required
def eliminar(id):
    if not id:
        return jsonify({"error": "ID es requerido"}), 400
    resp = repo.eliminar(id)
    return jsonify({"mensaje": resp})