from Entidades import PuertasAccesos
from Repositorios.BaseRepositorio import BaseRepositorio

class PuertasAccesosRepositorio(BaseRepositorio):

    def obtener(self) -> list[PuertasAccesos.PuertasAccesos]:
        query = "{CALL proc_select_puertas_acceso()}"
        rows = self.obtener_todos(query)

        puertas: list = []
        for elemento in rows:
            entidad: PuertasAccesos = PuertasAccesos.PuertasAccesos()
            entidad.set_id(elemento[0])
            entidad.set_nombre(elemento[1])
            puertas.append(entidad)

        return puertas

    def insertar(self, nombre: str) -> str:
        query = "{CALL proc_insert_puertas_acceso(?, @Respuesta)}"
        return self.ejecutar_sp(query, (nombre,))

    def actualizar(self, id_puerta: int, nombre: str) -> str:
        query = "{CALL proc_update_puertas_acceso(?, ?, @Respuesta)}"
        return self.ejecutar_sp(query, (id_puerta, nombre))

    def eliminar(self, id_puerta: int) -> str:
        query = "{CALL proc_delete_puertas_acceso(?, @Respuesta)}"
        return self.ejecutar_sp(query, (id_puerta,))
