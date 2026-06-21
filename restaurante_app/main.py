from servicios.restaurante import Restaurante
from modelos.producto import Producto
from modelos.cliente import Cliente

def ejecutar_sistema():
    print("----------SISTEMA DE GESTIÓN DE RESTAURANTE YUMIT----------")

    mi_restaurante = Restaurante("El Buen Sabor")

    print("\n--- Cargando Datos del Sistema ---")

    plato1 = Producto(1, "Encebollado Mixto", 3.50, "Plato Fuerte")
    plato2 = Producto(2, "Ceviche de Camarón", 2.00, "Plato Fuerte")
    bebida1 = Producto(3, "Jugos Naturales", 1.50, "Bebida")

    cliente1 = Cliente("210052858545", "Vicky Hernadez", "vickyfernandez@estudiante.com")
    cliente2 = Cliente("210052858545", "Jeick Vera", "jeickvera@estudiante.com")

    mi_restaurante.agregar_producto(plato1)
    mi_restaurante.agregar_producto(plato2)
    mi_restaurante.agregar_producto(bebida1)

    mi_restaurante.registrar_cliente(cliente1)
    mi_restaurante.registrar_cliente(cliente2)

    mi_restaurante.mostrar_menu()
    mi_restaurante.mostrar_clientes()

    print("----------Ejecución Finalizada con Éxito----------")

if __name__ == "__main__":
    ejecutar_sistema()
