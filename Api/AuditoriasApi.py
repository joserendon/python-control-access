from flask import Blueprint, request, jsonify
from Repositorios.AuditoriasRepositorio import AuditoriasRepositorio
from Utilidades.TokenRequiredDecorator import token_required

auditorias_api = Blueprint('auditorias_api', __name__)
repo = AuditoriasRepositorio()

@auditorias_api.route('/auditorias', methods=['GET'])
@token_required
def listar():
    auditorias = repo.obtener()
    return jsonify([a.to_dict() for a in auditorias])

@auditorias_api.route('/auditorias', methods=['POST'])
@token_required
def crear():
    data = request.json
    resp = repo.insertar(**data)
    return jsonify({"mensaje": resp})

@auditorias_api.route('/auditorias', methods=['PUT'])
@token_required
def actualizar():
    data = request.json
    resp = repo.actualizar(**data)
    return jsonify({"mensaje": resp})

@auditorias_api.route('/auditorias/<int:id>', methods=['DELETE'])
@token_required
def eliminar(id):
    if not id:
        return jsonify({"error": "ID es requerido"}), 400
    resp = repo.eliminar(id)
    return jsonify({"mensaje": resp})