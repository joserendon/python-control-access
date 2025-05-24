from flask import Blueprint, request, jsonify
from Repositorios.TiposDocumentoRepositorio import TiposDocumentoRepositorio

tipos_documento_api = Blueprint('tipos_documento_api', __name__)
repo = TiposDocumentoRepositorio()

@tipos_documento_api.route('/tiposdocumento', methods=['GET'])
def listar():
    tipos = repo.obtener()
    return jsonify([t.to_dict() for t in tipos])

@tipos_documento_api.route('/tiposdocumento', methods=['POST'])
def crear():
    data = request.json

    if not data:
        return jsonify({"error": "Datos son requeridos"}), 400

    resp = repo.insertar(**data)
    return jsonify({"mensaje": resp})

@tipos_documento_api.route('/tiposdocumento', methods=['PUT'])
def actualizar():
    data = request.json

    if not data:
        return jsonify({"error": "Datos son requeridos"}), 400

    resp = repo.actualizar(**data)
    return jsonify({"mensaje": resp})

@tipos_documento_api.route('/tiposdocumento/<int:id>', methods=['DELETE'])
def eliminar(id):
    if not id:
        return jsonify({"error": "ID es requerido"}), 400
    resp = repo.eliminar(id)
    return jsonify({"mensaje": resp})