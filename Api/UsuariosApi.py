from flask import Blueprint, request, jsonify
from Repositorios.UsuariosRepositorio import UsuariosRepositorio
from Utilidades import PasswordHash, EncriptarAES;
import jwt
import datetime
from Utilidades.Constantes import SECRET_KEY
from Utilidades.TokenRequiredDecorator import token_required

usuarios_api = Blueprint('usuarios_api', __name__)
repo = UsuariosRepositorio()
passwordHash = PasswordHash.PasswordHash()
encriptarAES = EncriptarAES.EncriptarAES();

# Ruta de autenticación
@usuarios_api.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password") 

    if not username or not password:
        return jsonify({'error': 'Usuario y contraseña son requeridos'}), 400
        
    user = repo.obtener_por_usuario(username)

    if not user:
        return jsonify({'error': 'Credenciales inválidas'}), 401 
 
    if passwordHash.verify_password(password, user.password):
        token = jwt.encode({
            'user': username,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
        }, SECRET_KEY, algorithm="HS256")
        return jsonify({'token': token})

    return jsonify({'error': 'Credenciales inválidas'}), 401


@usuarios_api.route('/usuarios', methods=['GET'])
@token_required
def listar():
    usuarios = repo.obtener()
    return jsonify([u.to_dict() for u in usuarios])

@usuarios_api.route('/usuarios', methods=['POST'])
@token_required
def crear():
    data = request.json

    if not data:
        return jsonify({"error": "Datos son requeridos"}), 400
    
    resp = repo.insertar(**data)
    return jsonify({"mensaje": resp})

@usuarios_api.route('/usuarios', methods=['PUT'])
@token_required
def actualizar():        
    data = request.json

    if not data:
        return jsonify({"error": "Datos son requeridos"}), 400
     
    resp = repo.actualizar(**data)
    return jsonify({"mensaje": resp})

@usuarios_api.route('/usuarios/<int:id>', methods=['DELETE'])
@token_required
def eliminar(id):
    if not id:
        return jsonify({"error": "ID es requerido"}), 400
    resp = repo.eliminar(id)
    return jsonify({"mensaje": resp})