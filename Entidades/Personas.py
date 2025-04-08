class Personas:
    def __init__(self):
        self.id = 0
        self.id_tipo_documento = 0
        self.id_tipo_persona = 0
        self.documento = None
        self.nombre_completo = None
        self.telefono = None
        self.id_empresa = None

    def get_id(self): return self.id
    def set_id(self, value): self.id = value
    def get_id_tipo_documento(self): return self.id_tipo_documento
    def set_id_tipo_documento(self, value): self.id_tipo_documento = value
    def get_id_tipo_persona(self): return self.id_tipo_persona
    def set_id_tipo_persona(self, value): self.id_tipo_persona = value
    def get_documento(self): return self.documento
    def set_documento(self, value): self.documento = value
    def get_nombre_completo(self): return self.nombre_completo
    def set_nombre_completo(self, value): self.nombre_completo = value
    def get_telefono(self): return self.telefono
    def set_telefono(self, value): self.telefono = value
    def get_id_empresa(self): return self.id_empresa
    def set_id_empresa(self, value): self.id_empresa = value