import pyodbc 
from Utilidades import Configuracion

class BaseRepositorio:
    def __init__(self):
        self.connection_string = Configuracion.Configuracion.strConnection
 
    def obtener_conexion(self): 
        return pyodbc.connect(self.connection_string)

    def obtener_todos(self, query: str, params: tuple = ()):
        try:            
            with self.obtener_conexion() as conn:
                cursor = conn.cursor()
                cursor.execute(query, params)

                rows = cursor.fetchall()
                
                while cursor.nextset(): pass

                return rows            
        except Exception as ex: print(str(ex));

    def ejecutar_sp(self, query: str, params: tuple = ()):
        try:
            with self.obtener_conexion() as conn:
                cursor = conn.cursor()
                cursor.execute(query, params) 

                consulta = "SELECT @Respuesta;";
                cursor.execute(consulta);
                respuesta = cursor.fetchone()[0]
                # print(respuesta);
                cursor.commit();
        
                return respuesta;
        except Exception as ex: print(str(ex));
