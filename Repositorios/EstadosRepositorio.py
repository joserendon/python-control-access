from Entidades import Estados
from Repositorios.BaseRepositorio import BaseRepositorio

class EstadosRepositorio(BaseRepositorio):

    def obtener(self) -> list[Estados.Estados]:
        query = "{CALL proc_select_estados()}"
        rows = self.obtener_todos(query)

        estados: list = [];
        for elemento in rows:
            entidad: Estados = Estados.Estados();
            entidad.set_id(elemento[0]);
            entidad.set_nombre(elemento[1]);
            estados.append(entidad);

        return estados   
   
    def insertar(self, estado: str) -> str:
        query = "{CALL proc_insert_estados(?, @Respuesta)}"
        return self.ejecutar_sp(query, (estado,))

    def actualizar(self, id_estado: int, nuevo_estado: str) -> str:
        query = "{CALL proc_update_estados(?,?, @Respuesta)}"
        return self.ejecutar_sp(query, (id_estado, nuevo_estado))

    def eliminar(self, id_estado: int) -> str:
        query = "{CALL proc_delete_estados(?, @Respuesta)}"
        return self.ejecutar_sp(query, (id_estado,)) 