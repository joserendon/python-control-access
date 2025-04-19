from Entidades import TiposAccesos
from Repositorios.BaseRepositorio import BaseRepositorio

class TiposAccesosRepositorio(BaseRepositorio):

    def obtener(self) -> list[TiposAccesos.TiposAccesos]:
        query = "{CALL proc_select_tipos_acceso()}"
        rows = self.obtener_todos(query)

        tipos_acceso: list = []
        for elemento in rows:
            entidad: TiposAccesos = TiposAccesos.TiposAccesos()
            entidad.set_id(elemento[0])
            entidad.set_nombre(elemento[1])
            tipos_acceso.append(entidad)

        return tipos_acceso

    def insertar(self, nombre: str) -> str:
        query = "{CALL proc_insert_tipos_acceso(?, @Respuesta)}"
        return self.ejecutar_sp(query, (nombre,))

    def actualizar(self, id_tipo: int, nombre: str) -> str:
        query = "{CALL proc_update_tipos_acceso(?, ?, @Respuesta)}"
        return self.ejecutar_sp(query, (id_tipo, nombre))

    def eliminar(self, id_tipo: int) -> str:
        query = "{CALL proc_delete_tipos_acceso(?, @Respuesta)}"
        return self.ejecutar_sp(query, (id_tipo,))