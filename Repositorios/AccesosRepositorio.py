from Entidades import Accesos
from Repositorios.BaseRepositorio import BaseRepositorio

class AccesosRepositorio(BaseRepositorio):

    def obtener(self) -> list[Accesos.Accesos]:
        query = "{CALL proc_select_accesos()}"
        rows = self.obtener_todos(query)

        accesos: list = []
        for elemento in rows:
            entidad: Accesos = Accesos.Accesos()
            entidad.set_id(elemento[0])
            entidad.set_id_puerta_acceso(elemento[1])
            entidad.set_id_persona(elemento[2])
            entidad.set_id_area(elemento[3])
            entidad.set_id_motivo(elemento[4])
            entidad.set_id_tipo_acceso(elemento[5])
            entidad.set_fecha_hora(elemento[6])
            accesos.append(entidad)

        return accesos

    def insertar(self, id_puerta_acceso: int, id_persona: int, id_area: int, id_motivo: int, id_tipo_acceso: int) -> str:
        query = "{CALL proc_insert_accesos(?, ?, ?, ?, ?, @Respuesta)}"
        return self.ejecutar_sp(query, (id_puerta_acceso, id_persona, id_area, id_motivo, id_tipo_acceso))

    def actualizar(self, id_acceso: int, id_puerta_acceso: int, id_persona: int, id_area: int, id_motivo: int, id_tipo_acceso: int) -> str:
        query = "{CALL proc_update_accesos(?, ?, ?, ?, ?, ?, @Respuesta)}"
        return self.ejecutar_sp(query, (id_acceso, id_puerta_acceso, id_persona, id_area, id_motivo, id_tipo_acceso))

    def eliminar(self, id_acceso: int) -> str:
        query = "{CALL proc_delete_accesos(?, @Respuesta)}"
        return self.ejecutar_sp(query, (id_acceso,))