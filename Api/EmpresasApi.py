from flask import Blueprint, request, jsonify
from Repositorios.EmpresasRepositorio import EmpresasRepositorio

empresas_api = Blueprint('empresas_api', __name__)
repo = EmpresasRepositorio()

@empresas_api.route('/empresas', methods=['GET'])
def listar():
    empresas = repo.obtener()
    return jsonify([e.to_dict() for e in empresas])

@empresas_api.route('/empresas', methods=['POST'])
def crear():
    data = request.json

    if not data:    
        return jsonify({"error": "Datos son requeridos"}), 400

    resp = repo.insertar(**data)
    return jsonify({"mensaje": resp})

@empresas_api.route('/empresas', methods=['PUT'])
def actualizar():
    data = request.json

    if not data:
        return jsonify({"error": "Datos son requeridos"}), 400

    resp = repo.actualizar(**data)
    return jsonify({"mensaje": resp})

@empresas_api.route('/empresas/<int:id>', methods=['DELETE'])
def eliminar(id):
    if not id:
        return jsonify({"error": "ID es requerido"}), 400
    resp = repo.eliminar(id)
    return jsonify({"mensaje": resp})