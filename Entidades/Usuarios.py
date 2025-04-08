class Usuarios:
    def __init__(self):
        self.id = 0
        self.nombre_completo = None
        self.username = None
        self.password_hash = None
        self.id_rol = 0
        self.id_estado = 0

    def get_id(self): return self.id
    def set_id(self, value): self.id = value
    def get_nombre_completo(self): return self.nombre_completo
    def set_nombre_completo(self, value): self.nombre_completo = value
    def get_username(self): return self.username
    def set_username(self, value): self.username = value
    def get_password_hash(self): return self.password_hash
    def set_password_hash(self, value): self.password_hash = value
    def get_id_rol(self): return self.id_rol
    def set_id_rol(self, value): self.id_rol = value
    def get_id_estado(self): return self.id_estado
    def set_id_estado(self, value): self.id_estado = value