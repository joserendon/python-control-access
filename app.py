from flask import Flask
from Api.UsuariosApi import usuarios_api
from Api.RolesApi import roles_api
from Api.EstadosApi import estados_api
from Api.AreasApi import areas_api
from Api.MotivosApi import motivos_api
# from Api.EmpresasApi import empresas_api
# from Api.TiposDocumentoApi import tipos_documento_api
# from Api.TiposPersonasApi import tipos_personas_api
# from Api.AccesosApi import accesos_api
# from Api.PuertasAccesosApi import puertas_accesos_api
# from Api.AccionesApi import acciones_api
# from Api.AuditoriasApi import auditorias_api
# from Api.PersonasApi import personas_api
# from Api.TiposAccesosApi import tipos_accesos_api

app = Flask(__name__)

app.register_blueprint(usuarios_api)
app.register_blueprint(roles_api)
app.register_blueprint(estados_api)
app.register_blueprint(areas_api)
app.register_blueprint(motivos_api)
# app.register_blueprint(empresas_api)
# app.register_blueprint(tipos_documento_api)
# app.register_blueprint(tipos_personas_api)
# app.register_blueprint(accesos_api)
# app.register_blueprint(puertas_accesos_api)
# app.register_blueprint(acciones_api)
# app.register_blueprint(auditorias_api)
# app.register_blueprint(personas_api)
# app.register_blueprint(tipos_accesos_api)

if __name__ == "__main__":
    app.run(debug=True)