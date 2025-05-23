from Entidades import Usuarios
from Repositorios.BaseRepositorio import BaseRepositorio
from Utilidades import EncriptarAES, PasswordHash;

class UsuariosRepositorio(BaseRepositorio):
    encriptarAES = EncriptarAES.EncriptarAES();
    passwordHash = PasswordHash.PasswordHash()

    def obtener(self) -> list[Usuarios.Usuarios]:
        query = "{CALL proc_select_usuarios()}"
        rows = self.obtener_todos(query)

        usuarios: list = []
        for elemento in rows:
            entidad: Usuarios = Usuarios.Usuarios()
            entidad.set_id(elemento[0])
            entidad.set_nombre(self.encriptarAES.Decifrar(elemento[1]))
            entidad.set_usuario(elemento[2])
            entidad.set_password(elemento[3])
            entidad.set_id_rol(elemento[4])
            entidad.set_id_estado(elemento[5])
            usuarios.append(entidad)

        return usuarios

    def insertar(self, nombre: str, usuario: str, password: str, id_rol: int, id_estado: int) -> str:
        query = "{CALL proc_insert_usuarios(?, ?, ?, ?, ?, @Respuesta)}"
        nombre = self.encriptarAES.Cifrar(nombre) 
        if(len(password) < 20):            
            password = self.passwordHash.hash_password(password)
        return self.ejecutar_sp(query, (nombre, usuario, password, id_rol, id_estado))

    def actualizar(self, id_usuario: int, nombre: str, usuario: str, password: str, id_rol: int, id_estado: int) -> str:
        query = "{CALL proc_update_usuarios(?, ?, ?, ?, ?, ?, @Respuesta)}"
        nombre = self.encriptarAES.Cifrar(nombre) 
        if(len(password) < 20):            
            password = self.passwordHash.hash_password(password)
        return self.ejecutar_sp(query, (id_usuario, nombre, usuario, password, id_rol, id_estado))

    def eliminar(self, id_usuario: int) -> str:
        query = "{CALL proc_delete_usuarios(?, @Respuesta)}"
        return self.ejecutar_sp(query, (id_usuario,))
    
    def obtener_por_usuario(self, usuario: str) -> Usuarios.Usuarios | None:
        query = "{CALL proc_select_usuario_por_usuario(?)}"
        rows = self.obtener_todos(query, (usuario,))
        
        if not rows:
            return None

        elemento = rows[0]
        entidad = Usuarios.Usuarios()
        entidad.set_id(elemento[0])
        entidad.set_nombre(self.encriptarAES.Decifrar(elemento[1]))
        entidad.set_usuario(elemento[2])
        entidad.set_password(elemento[3])
        entidad.set_id_rol(elemento[4])
        entidad.set_id_estado(elemento[5])
        
        return entidad
