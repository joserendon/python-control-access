from flask import Blueprint, request, jsonify
from Repositorios.EstadosRepositorio import EstadosRepositorio

estados_api = Blueprint('estados_api', __name__)
repo = EstadosRepositorio()

@estados_api.route('/estados', methods=['GET'])
def listar():
    estados = repo.obtener()
    return jsonify([e.to_dict() for e in estados])

@estados_api.route('/estados', methods=['POST'])
def crear():
    data = request.json

    if not data:
        return jsonify({"error": "Datos son requeridos"}), 400

    resp = repo.insertar(**data)
    return jsonify({"mensaje": resp})

@estados_api.route('/estados', methods=['PUT'])
def actualizar():
    data = request.json
    
    if not data:
        return jsonify({"error": "Datos son requeridos"}), 400
    
    resp = repo.actualizar(**data)
    return jsonify({"mensaje": resp})

@estados_api.route('/estados/<int:id>', methods=['DELETE'])
def eliminar(id):
    if not id:
        return jsonify({"error": "ID es requerido"}), 400
    resp = repo.eliminar(id)
    return jsonify({"mensaje": resp})