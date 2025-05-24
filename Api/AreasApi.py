from flask import Blueprint, request, jsonify
from Repositorios.AreasRepositorio import AreasRepositorio

areas_api = Blueprint('areas_api', __name__)
repo = AreasRepositorio()

@areas_api.route('/areas', methods=['GET'])
def listar():
    areas = repo.obtener()
    return jsonify([a.to_dict() for a in areas])

@areas_api.route('/areas', methods=['POST'])
def crear():
    data = request.json

    if not data:
        return jsonify({"error": "Datos son requeridos"}), 400

    resp = repo.insertar(**data)
    return jsonify({"mensaje": resp})

@areas_api.route('/areas', methods=['PUT'])
def actualizar():
    data = request.json

    if not data:
        return jsonify({"error": "Datos son requeridos"}), 400

    resp = repo.actualizar(**data)
    return jsonify({"mensaje": resp})

@areas_api.route('/areas/<int:id>', methods=['DELETE'])
def eliminar(id):
    if not id:
        return jsonify({"error": "ID es requerido"}), 400
    resp = repo.eliminar(id)
    return jsonify({"mensaje": resp})