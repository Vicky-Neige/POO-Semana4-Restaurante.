# Evaluación Semana 4: Programación Orientada a Objetos

## Datos del Estudiante
* **Nombre Completo:** Mayerli Melania Granda Quispe
* **Asignatura:** Programación Orientada a Objetos
* **Carrera:** Tecnologías de la Información
* **Nivel:** Segundo Semestre (Nivel II)
* **Paralelo:** Paralelo F
* **Docente:** Mgs. Kevin Bolívar Lascano Sánchez

## Contexto y Objetivo de la Tarea
La presente actividad consiste en aplicar las características fundamentales de la Programación Orientada a Objetos (POO) en un proyecto Python organizado en módulos. El objetivo es demostrar la correcta separación de responsabilidades entre modelos, servicios y el archivo principal de ejecución, utilizando un contexto de un Restaurante mediante importaciones de archivos.

## Sistema Desarrollado: Restaurante "YUMIT"
El sistema representa la gestión básica interna del restaurante. Se encarga de administrar un catálogo de productos y un registro de clientes mediante las siguientes entidades implementadas:

* **Producto:** Representa un plato o bebida disponible en el restaurante (atributos: id, nombre, precio, categoría).
* **Cliente:** Representa a la persona que consume en el restaurante (atributos: cédula, nombre, correo).
* **Restaurante:** Administra las listas dinámicas de productos y clientes registrados, además de imprimir los reportes correspondientes.

## Estructura Obligatoria del Proyecto
El proyecto se encuentra organizado respetando estrictamente la estructura modular solicitada por el docente:

restaurante_app/
├── modelos/
│   ├── cliente.py
│   └── producto.py
├── servicios/
│   └── restaurante.py
└── main.py

## Responsabilidad de cada Carpeta y Archivo
* **modelos/producto.py:** Contiene la clase `Producto`. Define sus atributos esenciales mediante el constructor `__init__()` y aplica el método especial `__str__()` para representar el objeto como texto limpio.
* **modelos/cliente.py:** Contiene la clase `Cliente`. Define el molde de datos de los clientes con sus atributos de contacto.
* **servicios/restaurante.py:** Contiene la clase `Restaurante`. Maneja la lógica del negocio mediante listas dinámicas (`catalogo_productos` y `registro_clientes`) para agregar elementos y mostrar la información organizada.
* **main.py:** Es el punto de arranque principal del programa. Se encarga de importar los módulos necesarios, instanciar los objetos de prueba (platos y clientes), agregarlos al servicio del restaurante y ejecutar las funciones de visualización en la consola.

## Reflexión sobre la Modularización y Separación de Responsabilidades
Modularizar el software y aplicar la separación de responsabilidades es fundamental en el desarrollo de aplicaciones porque transforma un código monolítico y complejo en componentes pequeños, independientes y estructurados. 

Al delegar una sola tarea a cada archivo (donde los modelos únicamente definen la estructura de los datos y los servicios controlan el comportamiento del negocio), se logra que el sistema sea altamente escalable y fácil de mantener. Si en el futuro el restaurante requiere modificar los datos de facturación o cambiar las propiedades de un producto, solo se debe alterar el módulo específico involucrado. Esto reduce drásticamente el riesgo de dañar otras partes funcionales del software, mejora la legibilidad del código y facilita enormemente el desarrollo colaborativo dentro de un equipo de TI.                   