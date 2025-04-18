from Entidades import Areas
from Repositorios.BaseRepositorio import BaseRepositorio

class AreasRepositorio(BaseRepositorio):

    def obtener(self) -> list[Areas.Areas]:
        query = "{CALL proc_select_areas()}"
        rows = self.obtener_todos(query)

        areas: list = []
        for elemento in rows:
            entidad: Areas = Areas.Areas()
            entidad.set_id(elemento[0])
            entidad.set_nombre(elemento[1])
            areas.append(entidad)

        return areas

    def insertar(self, area: str) -> str:
        query = "{CALL proc_insert_areas(?, @Respuesta)}"
        return self.ejecutar_sp(query, (area,))

    def actualizar(self, id_area: int, nueva_area: str) -> str:
        query = "{CALL proc_update_areas(?, ?, @Respuesta)}"
        return self.ejecutar_sp(query, (id_area, nueva_area))

    def eliminar(self, id_area: int) -> str:
        query = "{CALL proc_delete_areas(?, @Respuesta)}"
        return self.ejecutar_sp(query, (id_area,))