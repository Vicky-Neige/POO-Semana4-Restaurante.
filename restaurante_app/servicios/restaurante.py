from modelos.producto import Producto
from modelos.cliente import Cliente

class Restaurante:
    def __init__(self, nombre: str):
        self.nombre = nombre
        self.catalogo_productos = []
        self.registro_clientes = []
    
    def agregar_producto(self, producto: Producto):
        self.catalogo_productos.append(producto)
        print(f"Producto '{producto.nombre}' agregado con éxito al catálogo.")

    def registrar_cliente(self, cliente: Cliente):
        self.registro_clientes.append(cliente)
        print(f"Cliente '{cliente.nombre}' registrado con éxito.")

    def mostrar_menu(self):
        print(f'\n--- Menú de {self.nombre} ---')
        if not self.catalogo_productos:
            print("El menú esta vacío por el momento.")
        else:
            for prod in self.catalogo_productos:
                print(prod)
    
    def mostrar_clientes(self):
        print(f"\n--- Clientes Registrados en {self.nombre} ---")
        if not self.registro_clientes:
            print("No hay clientes registrados.")
        else:
            for cli in self.registro_clientes:
                print(cli)