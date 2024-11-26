
# Sistema de Gestión de Biblioteca

## Descripción

El **Sistema de Gestión de Biblioteca** es una aplicación desarrollada en Python que permite gestionar libros, préstamos y usuarios. Los clientes pueden registrar libros, solicitar préstamos, devolver libros y consultar reportes. Los administradores tienen acceso a funciones adicionales como agregar o eliminar libros, gestionar préstamos y generar reportes de libros solicitados y usuarios activos.

Este sistema cuenta con una interfaz gráfica basada en **Tkinter**, lo que facilita la interacción con el usuario.

## Tabla de Contenidos

- [Descripción](#descripción)
- [Características Principales](#características-principales)
- [Instalación y Ejecución](#instalación-y-ejecución)
- [Ejemplos](#ejemplos)
- [Cómo lo Creé](#cómo-lo-creé)
- [Recursos Útiles](#recursos-útiles)
- [Licencia](#licencia)

## Características Principales

### Para Clientes:
- **Registrar un Usuario:** Los clientes pueden registrarse en el sistema.
- **Solicitar Préstamo de Libros:** Los usuarios pueden tomar libros prestados, hasta un límite de 3 libros.
- **Devolver Libros:** Los clientes pueden devolver los libros prestados.
- **Ver Reportes:** Los clientes pueden ver los libros más solicitados y los usuarios activos.

### Para Administradores:
- **Gestionar Inventario de Libros:** Los administradores pueden agregar y eliminar libros del inventario.
- **Gestionar Préstamos:** Los administradores pueden gestionar los préstamos y devoluciones de libros.
- **Generar Reportes:** Los administradores pueden generar reportes sobre los libros más solicitados y los usuarios activos en el sistema.

## Instalación y Ejecución

### 1. Clonar el Repositorio

2. Instalación de Dependencias
No es necesario instalar dependencias adicionales, ya que el proyecto está basado en bibliotecas estándar de Python.

3. Ejecutar el Proyecto
Para ejecutar el sistema, abre una terminal en el directorio donde se encuentra el archivo main.py y ejecuta el siguiente comando:

bash
python main.py

4. Ejecutar las Pruebas Unitarias
Si deseas ejecutar las pruebas unitarias, usa el siguiente comando:

bash
python -m unittest test_biblioteca.py

Ejemplos

Ejemplo de Solicitar un Préstamo
Cliente:

El cliente ingresa su ID y nombre.
El cliente selecciona un libro disponible.
El cliente solicita el préstamo, y el libro es marcado como no disponible.
Administrador:

El administrador ingresa el ID de un libro que desea eliminar.
Si el libro no ha sido prestado, el administrador puede eliminarlo del inventario.
Ejemplo de Reporte de Libros Más Solicitados
Reporte Generado:

ejemplo:

Libros más solicitados:
1. "Python para Todos": 10 préstamos
2. "La Ciencia de Datos": 8 préstamos



Cómo lo Creé
Este sistema fue desarrollado en Python utilizando las bibliotecas estándar de Python como Tkinter para la interfaz gráfica, y las clases y funciones necesarias para la gestión de libros, usuarios y préstamos. Utilicé un enfoque basado en la programación orientada a objetos (OOP), lo que facilita la escalabilidad y el mantenimiento del código.

Pasos Clave:
Definición de Clases: Se crearon clases para manejar libros, usuarios y préstamos.
Interfaz Gráfica: Implementé una interfaz con Tkinter que permite a los usuarios interactuar con el sistema de manera visual.
Gestión de Reportes: Desarrollé funciones para generar reportes sobre los libros más solicitados y los usuarios activos.

Recursos Útiles
-Python Documentation
-Tkinter Documentation
-Unittest Module

Licencia:
Este proyecto está bajo la Licencia MIT. Consulta el archivo LICENSE para más detalles
Este proyecto está bajo la Licencia MIT. Consulta el archivo LICENSE para más detalles.



