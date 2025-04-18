from Entidades import Empresas
from Repositorios.BaseRepositorio import BaseRepositorio

class EmpresasRepositorio(BaseRepositorio):

    def obtener(self) -> list[Empresas.Empresas]:
        query = "{CALL proc_select_empresas()}"
        rows = self.obtener_todos(query)

        empresas: list = []
        for elemento in rows:
            entidad: Empresas = Empresas.Empresas()
            entidad.set_id(elemento[0])
            entidad.set_nombre(elemento[1])
            empresas.append(entidad)

        return empresas

    def insertar(self, empresa: str) -> str:
        query = "{CALL proc_insert_empresas(?, @Respuesta)}"
        return self.ejecutar_sp(query, (empresa,))

    def actualizar(self, id_empresa: int, nueva_empresa: str) -> str:
        query = "{CALL proc_update_empresas(?, ?, @Respuesta)}"
        return self.ejecutar_sp(query, (id_empresa, nueva_empresa))

    def eliminar(self, id_empresa: int) -> str:
        query = "{CALL proc_delete_empresas(?, @Respuesta)}"
        return self.ejecutar_sp(query, (id_empresa,))