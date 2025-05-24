from flask import Blueprint, request, jsonify
from Repositorios.TiposAccesosRepositorio import TiposAccesosRepositorio

tipos_accesos_api = Blueprint('tipos_accesos_api', __name__)
repo = TiposAccesosRepositorio()

@tipos_accesos_api.route('/tiposaccesos', methods=['GET'])
def listar():
    tipos = repo.obtener()
    return jsonify([t.to_dict() for t in tipos])

@tipos_accesos_api.route('/tiposaccesos', methods=['POST'])
def crear():
    data = request.json
    resp = repo.insertar(**data)
    return jsonify({"mensaje": resp})

@tipos_accesos_api.route('/tiposaccesos', methods=['PUT'])
def actualizar():
    data = request.json
    resp = repo.actualizar(**data)
    return jsonify({"mensaje": resp})

@tipos_accesos_api.route('/tiposaccesos/<int:id>', methods=['DELETE'])
def eliminar(id):
    if not id:
        return jsonify({"error": "ID es requerido"}), 400
    resp = repo.eliminar(id)
    return jsonify({"mensaje": resp})