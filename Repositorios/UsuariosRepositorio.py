from Entidades import Usuarios
from Repositorios.BaseRepositorio import BaseRepositorio

class UsuariosRepositorio(BaseRepositorio):

    def obtener(self) -> list[Usuarios.Usuarios]:
        query = "{CALL proc_select_usuarios()}"
        rows = self.obtener_todos(query)

        usuarios: list = []
        for elemento in rows:
            entidad: Usuarios = Usuarios.Usuarios()
            entidad.set_id(elemento[0])
            entidad.set_nombre(elemento[1])
            entidad.set_usuario(elemento[2])
            entidad.set_password(elemento[3])
            entidad.set_id_rol(elemento[4])
            entidad.set_id_estado(elemento[5])
            usuarios.append(entidad)

        return usuarios

    def insertar(self, nombre: str, usuario: str, password: str, id_rol: int, id_estado: int) -> str:
        query = "{CALL proc_insert_usuarios(?, ?, ?, ?, ?, @Respuesta)}"
        return self.ejecutar_sp(query, (nombre, usuario, password, id_rol, id_estado))

    def actualizar(self, id_usuario: int, nombre: str, usuario: str, password: str, id_rol: int, id_estado: int) -> str:
        query = "{CALL proc_update_usuarios(?, ?, ?, ?, ?, ?, @Respuesta)}"
        return self.ejecutar_sp(query, (id_usuario, nombre, usuario, password, id_rol, id_estado))

    def eliminar(self, id_usuario: int) -> str:
        query = "{CALL proc_delete_usuarios(?, @Respuesta)}"
        return self.ejecutar_sp(query, (id_usuario,))