from Entidades import Estados
from Repositorios.BaseRepositorio import BaseRepositorio

class EstadosRepositorio(BaseRepositorio):

    def obtener_estados(self) -> list[Estados.Estados]:
        query = "{CALL proc_select_estados()}"
        rows = self.obtener_todos(query)

        estados: list = [];
        for elemento in rows:
            entidad: Estados = Estados.Estados();
            entidad.set_id(elemento[0]);
            entidad.set_estado(elemento[1]);
            estados.append(entidad);

        return estados   
   
    def insertar_estado(self, estado: str) -> str:
        query = "{CALL proc_insert_estados(?, @Respuesta)}"
        return self.ejecutar_sp(query, (estado,))

    def actualizar_estado(self, id_estado: int, nuevo_estado: str) -> str:
        query = "{CALL proc_update_estados(?,?, @Respuesta)}"
        return self.ejecutar_sp(query, (id_estado, nuevo_estado))

    def eliminar_estado(self, id_estado: int) -> str:
        query = "{CALL proc_delete_estados(?, @Respuesta)}"
        return self.ejecutar_sp(query, (id_estado,)) 