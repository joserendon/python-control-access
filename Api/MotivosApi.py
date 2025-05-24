from flask import Blueprint, request, jsonify
from Repositorios.MotivosRepositorio import MotivosRepositorio

motivos_api = Blueprint('motivos_api', __name__)
repo = MotivosRepositorio()

@motivos_api.route('/motivos', methods=['GET'])
def listar():
    motivos = repo.obtener()
    return jsonify([m.to_dict() for m in motivos])

@motivos_api.route('/motivos', methods=['POST'])
def crear():
    data = request.json

    if not data:    
        return jsonify({"error": "Datos son requeridos"}), 400

    resp = repo.insertar(**data)
    return jsonify({"mensaje": resp})

@motivos_api.route('/motivos', methods=['PUT'])
def actualizar():
    data = request.json

    if not data:    
        return jsonify({"error": "Datos son requeridos"}), 400

    resp = repo.actualizar(**data)
    return jsonify({"mensaje": resp})

@motivos_api.route('/motivos/<int:id>', methods=['DELETE'])
def eliminar(id):
    if not id:
        return jsonify({"error": "ID es requerido"}), 400
    resp = repo.eliminar(id)
    return jsonify({"mensaje": resp})