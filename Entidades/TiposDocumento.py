class TiposDocumento:
    def __init__(self):
        self.id = 0
        self.nombre = None

    def get_id(self): return self.id
    def set_id(self, value): self.id = value
    def get_nombre(self): return self.nombre
    def set_nombre(self, value): self.nombre = value

    def to_dict(self):
        return {
            'id': self.id,
            'nombre': self.nombre
        }