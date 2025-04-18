class Usuarios:
    def __init__(self):
        self.id = 0
        self.nombre = None
        self.usuario = None
        self.password = None
        self.id_rol = 0
        self.id_estado = 0

    def get_id(self): return self.id
    def set_id(self, value): self.id = value

    def get_nombre(self): return self.nombre
    def set_nombre(self, value): self.nombre = value

    def get_usuario(self): return self.usuario
    def set_usuario(self, value): self.usuario = value

    def get_password(self): return self.password
    def set_password(self, value): self.password = value

    def get_id_rol(self): return self.id_rol
    def set_id_rol(self, value): self.id_rol = value

    def get_id_estado(self): return self.id_estado
    def set_id_estado(self, value): self.id_estado = value