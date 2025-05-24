from flask import Blueprint, request, jsonify
from Repositorios.PuertasAccesosRepositorio import PuertasAccesosRepositorio
from Utilidades.TokenRequiredDecorator import token_required

puertas_accesos_api = Blueprint('puertas_accesos_api', __name__)
repo = PuertasAccesosRepositorio()

@puertas_accesos_api.route('/puertasaccesos', methods=['GET'])
@token_required
def listar():
    puertas = repo.obtener()
    return jsonify([p.to_dict() for p in puertas])

@puertas_accesos_api.route('/puertasaccesos', methods=['POST'])
@token_required
def crear():
    data = request.json
    resp = repo.insertar(**data)
    return jsonify({"mensaje": resp})

@puertas_accesos_api.route('/puertasaccesos', methods=['PUT'])
@token_required
def actualizar():
    data = request.json
    resp = repo.actualizar(**data)
    return jsonify({"mensaje": resp})

@puertas_accesos_api.route('/puertasaccesos/<int:id>', methods=['DELETE'])
@token_required
def eliminar(id):
    if not id:
        return jsonify({"error": "ID es requerido"}), 400
    resp = repo.eliminar(id)
    return jsonify({"mensaje": resp})