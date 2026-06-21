class Cliente:
    def __init__(self, cedula: str, nombre: str, correo: str):
        self.cedula = cedula
        self.nombre = nombre
        self.correo = correo
    
    def __str__(self):
        return f"Cliente: {self.nombre} | C.I: {self.cedula} | Correo: {self.correo} "