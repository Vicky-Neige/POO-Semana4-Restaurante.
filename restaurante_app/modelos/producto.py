class Producto:
    def __init__(self, id_producto: int, nombre: str, precio: float, categoria: str):
        self.id_producto = id_producto
        self.nombre = nombre
        self.precio = precio
        self.categoria = categoria
    def __str__(self) :
        return f"[{self.id_producto}] {self.nombre} ({self.categoria}) - ${self.precio:.2f}"