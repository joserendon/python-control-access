from Entidades import TiposDocumento
from Repositorios.BaseRepositorio import BaseRepositorio

class TiposDocumentoRepositorio(BaseRepositorio):

    def obtener(self) -> list[TiposDocumento.TiposDocumento]:
        query = "{CALL proc_select_tipos_documento()}"
        rows = self.obtener_todos(query)

        tipos: list = []
        for elemento in rows:
            entidad: TiposDocumento = TiposDocumento.TiposDocumento()
            entidad.set_id(elemento[0])
            entidad.set_nombre(elemento[1])
            tipos.append(entidad)

        return tipos

    def insertar(self, tipo_documento: str) -> str:
        query = "{CALL proc_insert_tipos_documento(?, @Respuesta)}"
        return self.ejecutar_sp(query, (tipo_documento,))

    def actualizar(self, id_tipo: int, nuevo_tipo: str) -> str:
        query = "{CALL proc_update_tipos_documento(?, ?, @Respuesta)}"
        return self.ejecutar_sp(query, (id_tipo, nuevo_tipo))

    def eliminar(self, id_tipo: int) -> str:
        query = "{CALL proc_delete_tipos_documento(?, @Respuesta)}"
        return self.ejecutar_sp(query, (id_tipo,))