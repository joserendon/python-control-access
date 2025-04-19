from Entidades import TiposPersonas
from Repositorios.BaseRepositorio import BaseRepositorio

class TiposPersonasRepositorio(BaseRepositorio):

    def obtener(self) -> list[TiposPersonas.TiposPersonas]:
        query = "{CALL proc_select_tipos_persona()}"
        rows = self.obtener_todos(query)

        tipos_persona: list = []
        for elemento in rows:
            entidad: TiposPersonas = TiposPersonas.TiposPersonas()
            entidad.set_id(elemento[0])
            entidad.set_nombre(elemento[1])
            tipos_persona.append(entidad)

        return tipos_persona

    def insertar(self, nombre: str) -> str:
        query = "{CALL proc_insert_tipos_persona(?, @Respuesta)}"
        return self.ejecutar_sp(query, (nombre,))

    def actualizar(self, id_tipo: int, nombre: str) -> str:
        query = "{CALL proc_update_tipos_persona(?, ?, @Respuesta)}"
        return self.ejecutar_sp(query, (id_tipo, nombre))

    def eliminar(self, id_tipo: int) -> str:
        query = "{CALL proc_delete_tipos_persona(?, @Respuesta)}"
        return self.ejecutar_sp(query, (id_tipo,))