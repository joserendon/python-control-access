from Entidades import Acciones
from Repositorios.BaseRepositorio import BaseRepositorio

class AccionesRepositorio(BaseRepositorio):

    def obtener(self) -> list[Acciones.Acciones]:
        query = "{CALL proc_select_acciones()}"
        rows = self.obtener_todos(query)

        acciones: list = []
        for elemento in rows:
            entidad: Acciones = Acciones.Acciones()
            entidad.set_id(elemento[0])
            entidad.set_nombre(elemento[1])
            acciones.append(entidad)

        return acciones

    def insertar(self, nombre: str) -> str:
        query = "{CALL proc_insert_acciones(?, @Respuesta)}"
        return self.ejecutar_sp(query, (nombre,))

    def actualizar(self, id_accion: int, nombre: str) -> str:
        query = "{CALL proc_update_acciones(?, ?, @Respuesta)}"
        return self.ejecutar_sp(query, (id_accion, nombre))

    def eliminar(self, id_accion: int) -> str:
        query = "{CALL proc_delete_acciones(?, @Respuesta)}"
        return self.ejecutar_sp(query, (id_accion,))