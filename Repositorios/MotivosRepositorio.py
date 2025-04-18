from Entidades import Motivos
from Repositorios.BaseRepositorio import BaseRepositorio

class MotivosRepositorio(BaseRepositorio):

    def obtener(self) -> list[Motivos.Motivos]:
        query = "{CALL proc_select_motivos()}"
        rows = self.obtener_todos(query)

        motivos: list = []
        for elemento in rows:
            entidad: Motivos = Motivos.Motivos()
            entidad.set_id(elemento[0])
            entidad.set_nombre(elemento[1])
            motivos.append(entidad)

        return motivos

    def insertar(self, motivo: str) -> str:
        query = "{CALL proc_insert_motivos(?, @Respuesta)}"
        return self.ejecutar_sp(query, (motivo,))

    def actualizar(self, id_motivo: int, nuevo_motivo: str) -> str:
        query = "{CALL proc_update_motivos(?, ?, @Respuesta)}"
        return self.ejecutar_sp(query, (id_motivo, nuevo_motivo))

    def eliminar(self, id_motivo: int) -> str:
        query = "{CALL proc_delete_motivos(?, @Respuesta)}"
        return self.ejecutar_sp(query, (id_motivo,))