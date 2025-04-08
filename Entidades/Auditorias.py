class Auditorias:
    def __init__(self):
        self.id = 0
        self.id_usuario = 0
        self.id_accion = 0
        self.descripcion = None
        self.fecha_hora = None

    def get_id(self): return self.id
    def set_id(self, value): self.id = value
    def get_id_usuario(self): return self.id_usuario
    def set_id_usuario(self, value): self.id_usuario = value
    def get_id_accion(self): return self.id_accion
    def set_id_accion(self, value): self.id_accion = value
    def get_descripcion(self): return self.descripcion
    def set_descripcion(self, value): self.descripcion = value
    def get_fecha_hora(self): return self.fecha_hora
    def set_fecha_hora(self, value): self.fecha_hora = value