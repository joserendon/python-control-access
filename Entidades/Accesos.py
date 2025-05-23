class Accesos:
    def __init__(self):
        self.id = 0
        self.id_puerta_acceso = 0
        self.id_persona = 0
        self.id_area = 0
        self.id_motivo = 0
        self.id_tipo_acceso = 0
        self.fecha_hora = None

    def get_id(self): return self.id
    def set_id(self, value): self.id = value
    def get_id_puerta_acceso(self): return self.id_puerta_acceso
    def set_id_puerta_acceso(self, value): self.id_puerta_acceso = value
    def get_id_persona(self): return self.id_persona
    def set_id_persona(self, value): self.id_persona = value
    def get_id_area(self): return self.id_area
    def set_id_area(self, value): self.id_area = value
    def get_id_motivo(self): return self.id_motivo
    def set_id_motivo(self, value): self.id_motivo = value
    def get_id_tipo_acceso(self): return self.id_tipo_acceso
    def set_id_tipo_acceso(self, value): self.id_tipo_acceso = value
    def get_fecha_hora(self): return self.fecha_hora
    def set_fecha_hora(self, value): self.fecha_hora = value

    def to_dict(self):
        return {
            'id': self.id,
            'id_puerta_acceso': self.id_puerta_acceso,
            'id_persona': self.id_persona,
            'id_area': self.id_area,
            'id_motivo': self.id_motivo,
            'id_tipo_acceso': self.id_tipo_acceso,
            'fecha_hora': self.fecha_hora
        }