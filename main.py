from Repositorios import (
    AuditoriasRepositorio,
    AccionesRepositorio,
    AccesosRepositorio,
    PuertasAccesosRepositorio,
    TiposAccesosRepositorio,
    PersonasRepositorio,
    TiposPersonasRepositorio,
    UsuariosRepositorio,
    RolesRepositorio,
    EstadosRepositorio,
    AreasRepositorio,
    MotivosRepositorio,
    TiposDocumentoRepositorio,
    EmpresasRepositorio
    )

def probar_tipos_persona():
    repo = TiposPersonasRepositorio.TiposPersonasRepositorio()
    print(repo.insertar("Empleado"))
    for item in repo.obtener():
        print(f"{item.get_id()} - Nombre: {item.get_nombre()}")
    #print(repo.actualizar(1, "Empleado Modificado"))
    #print(repo.eliminar(1))

def probar_personas():
    repo = PersonasRepositorio.PersonasRepositorio()
    #print(repo.insertar(1, 1, "1010101", "Andres Albanes", "3000000000", 1))
    for item in repo.obtener():
        print(f"{item.get_id()} - {item.get_nombre_completo()} - Doc: {item.get_documento()} - Tel: {item.get_telefono()}")
    #print(repo.actualizar(8, 1, 1, "1010101", "Andres Albanes Modificado", "3101234567", 1))
    #print(repo.eliminar(3))

def probar_tipos_acceso():
    repo = TiposAccesosRepositorio.TiposAccesosRepositorio()
    print(repo.insertar("Entrada"))
    for item in repo.obtener():
        print(f"{item.get_id()} - Nombre: {item.get_nombre()}")
    #print(repo.actualizar(1, "Entrada Modificada"))
    #print(repo.eliminar(1))

def probar_puertas_acceso():
    repo = PuertasAccesosRepositorio.PuertasAccesosRepositorio()
    print(repo.insertar("Puerta Principal"))
    for item in repo.obtener():
        print(f"{item.get_id()} - Nombre: {item.get_nombre()}")
    #print(repo.update(1, "Puerta Principal Modificada"))
    #print(repo.delete(1))

def probar_accesos():
    repo = AccesosRepositorio.AccesosRepositorio()
    print(repo.insertar(1, 1, 1, 1, 1))
    for item in repo.obtener():
        print(f"{item.get_id()} - Puerta: {item.get_id_puerta_acceso()} - Persona: {item.get_id_persona()} - Área: {item.get_id_area()} - Motivo: {item.get_id_motivo()} - Tipo: {item.get_id_tipo_acceso()} - Fecha: {item.get_fecha_hora()}")
    #print(repo.actualizar(1, 1, 1, 1, 1, 1))
    #print(repo.eliminar(1))

def probar_acciones():
    repo = AccionesRepositorio.AccionesRepositorio()
    print(repo.insertar("Inicio de sesión"))
    for item in repo.obtener():
        print(f"{item.get_id()} - Nombre: {item.get_nombre()}")
    #print(repo.actualizar(1, "Inicio de sesión modificado"))
    #print(repo.eliminar(1))

def probar_auditorias():
    repo = AuditoriasRepositorio.AuditoriasRepositorio()
    print(repo.insertar(1, 1, "Inicio de sesión correcto"))
    for item in repo.obtener():
        print(f"{item.get_id()} - Usuario: {item.get_id_usuario()} - Acción: {item.get_id_accion()} - Desc: {item.get_descripcion()} - Fecha: {item.get_fecha_hora()}")
    #print(repo.actualizar(1, 1, 1, "Auditoría modificada"))
    #print(repo.eliminar(1))

def probar_usuarios():
    repo = UsuariosRepositorio.UsuariosRepositorio()
    print(repo.insertar("Ana Martínez","amartinez","clave123",1,1))
    for item in repo.obtener():
        print(f"{item.get_id()} - {item.get_nombre()} - Usuario: {item.get_usuario()} - Rol: {item.get_id_rol()} - Estado: {item.get_id_estado()}")
    #print(repo.actualizar(2,"Ana M. Modificada","amartinez","clave456",1,1))
    #print(repo.eliminar(2))

def probar_roles():
    repo = RolesRepositorio.RolesRepositorio()
    print(repo.insertar("Administrador"))
    for item in repo.obtener():
        print(f"{item.get_id()} - Nombre: {item.get_nombre()}")
    #print(repo.actualizar(1, "Administrador Modificado"))
    #print(repo.eliminar(1))

def probar_estados():
    repo = EstadosRepositorio.EstadosRepositorio()
    print(repo.insertar("Activo"))
    for item in repo.obtener():
        print(f"{item.get_id()} - Nombre: {item.get_nombre()}")
    #print(repo.actualizar(1, "Activo Modificado"))
    #print(repo.eliminar(1))

def probar_areas():
    repo = AreasRepositorio.AreasRepositorio()
    print(repo.insertar("Administración"))
    for item in repo.obtener():
        print(f"{item.get_id()} - Nombre: {item.get_nombre()}")
    #print(repo.actualizar(2, "Administración Modificada"))
    #print(repo.eliminar(2))

def probar_motivos():
    repo = MotivosRepositorio.MotivosRepositorio()
    print(repo.insertar("Visita"))
    for item in repo.obtener():
        print(f"{item.get_id()} - Nombre: {item.get_nombre()}")
    #print(repo.actualizar(1, "Visita Modificada"))
    #print(repo.eliminar(1))

def probar_tipos_documento():
    repo = TiposDocumentoRepositorio.TiposDocumentoRepositorio()
    print(repo.insertar("Cédula de ciudadanía"))
    for item in repo.obtener():
        print(f"{item.get_id()} - Nombre: {item.get_nombre()}")
    #print(repo.actualizar(1, "Cédula de ciudadanía Modificada"))
    #print(repo.eliminar(1))

def probar_empresas():
    repo = EmpresasRepositorio.EmpresasRepositorio()
    print(repo.insertar("Empresa GANA"))
    for item in repo.obtener():
        print(f"{item.get_id()} - Nombre: {item.get_nombre()}")
    #print(repo.actualizar(1, "Empresa GANA Modificada"))
    #print(repo.eliminar(1))

if __name__ == "__main__":
    #probar_tipos_persona()
    #probar_personas()
    #probar_tipos_acceso()
    #probar_puertas_acceso()
    #probar_accesos()
    #probar_acciones()
    #probar_auditorias()
    #probar_usuarios()
    #probar_roles()
    #probar_estados()
    #probar_areas()
    #probar_motivos()
    #probar_tipos_documento()
    #probar_empresas()
    pass
