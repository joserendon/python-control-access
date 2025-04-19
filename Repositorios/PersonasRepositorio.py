from Entidades import Personas
from Repositorios.BaseRepositorio import BaseRepositorio

class PersonasRepositorio(BaseRepositorio):

    def obtener(self) -> list[Personas.Personas]:
        query = "{CALL proc_select_personas()}"
        rows = self.obtener_todos(query)

        personas: list = []
        for elemento in rows:
            entidad: Personas = Personas.Personas()
            entidad.set_id(elemento[0])
            entidad.set_id_tipo_documento(elemento[1])
            entidad.set_id_tipo_persona(elemento[2])
            entidad.set_documento(elemento[3])
            entidad.set_nombre_completo(elemento[4])
            entidad.set_telefono(elemento[5])
            entidad.set_id_empresa(elemento[6])
            personas.append(entidad)

        return personas

    def insertar(self, id_tipo_documento: int, id_tipo_persona: int, documento: str, nombre_completo: str, telefono: str, id_empresa: int) -> str:
        query = "{CALL proc_insert_personas(?, ?, ?, ?, ?, ?, @Respuesta)}"
        return self.ejecutar_sp(query, (id_tipo_documento, id_tipo_persona, documento, nombre_completo, telefono, id_empresa))

    def actualizar(self, id_persona: int, id_tipo_documento: int, id_tipo_persona: int, documento: str, nombre_completo: str, telefono: str, id_empresa: int) -> str:
        query = "{CALL proc_update_personas(?, ?, ?, ?, ?, ?, ?, @Respuesta)}"
        return self.ejecutar_sp(query, (id_persona, id_tipo_documento, id_tipo_persona, documento, nombre_completo, telefono, id_empresa))

    def eliminar(self, id_persona: int) -> str:
        query = "{CALL proc_delete_personas(?, @Respuesta)}"
        return self.ejecutar_sp(query, (id_persona,))