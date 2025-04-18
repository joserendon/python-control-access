from Entidades import Roles
from Repositorios.BaseRepositorio import BaseRepositorio

class RolesRepositorio(BaseRepositorio):

    def obtener(self) -> list[Roles.Roles]:
        query = "{CALL proc_select_roles()}"
        rows = self.obtener_todos(query)

        roles: list = []
        for elemento in rows:
            entidad: Roles = Roles.Roles()
            entidad.set_id(elemento[0])
            entidad.set_nombre(elemento[1])
            roles.append(entidad)

        return roles

    def insertar(self, rol: str) -> str:
        query = "{CALL proc_insert_roles(?, @Respuesta)}"
        return self.ejecutar_sp(query, (rol,))

    def actualizar(self, id_rol: int, nuevo_rol: str) -> str:
        query = "{CALL proc_update_roles(?, ?, @Respuesta)}"
        return self.ejecutar_sp(query, (id_rol, nuevo_rol))

    def eliminar(self, id_rol: int) -> str:
        query = "{CALL proc_delete_roles(?, @Respuesta)}"
        return self.ejecutar_sp(query, (id_rol,))