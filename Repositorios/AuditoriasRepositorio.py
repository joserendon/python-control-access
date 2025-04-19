from Entidades import Auditorias
from Repositorios.BaseRepositorio import BaseRepositorio

class AuditoriasRepositorio(BaseRepositorio):

    def obtener(self) -> list[Auditorias.Auditorias]:
        query = "{CALL proc_select_auditorias()}"
        rows = self.obtener_todos(query)

        auditorias: list = []
        for elemento in rows:
            entidad: Auditorias = Auditorias.Auditorias()
            entidad.set_id(elemento[0])
            entidad.set_id_usuario(elemento[1])
            entidad.set_id_accion(elemento[2])
            entidad.set_descripcion(elemento[3])
            entidad.set_fecha_hora(elemento[4])
            auditorias.append(entidad)

        return auditorias

    def insertar(self, id_usuario: int, id_accion: int, descripcion: str) -> str:
        query = "{CALL proc_insert_auditorias(?, ?, ?, @Respuesta)}"
        return self.ejecutar_sp(query, (id_usuario, id_accion, descripcion))

    def actualizar(self, id_auditoria: int, id_usuario: int, id_accion: int, descripcion: str) -> str:
        query = "{CALL proc_update_auditorias(?, ?, ?, ?, @Respuesta)}"
        return self.ejecutar_sp(query, (id_auditoria, id_usuario, id_accion, descripcion))

    def eliminar(self, id_auditoria: int) -> str:
        query = "{CALL proc_delete_auditorias(?, @Respuesta)}"
        return self.ejecutar_sp(query, (id_auditoria,))
