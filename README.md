**Sistema Básico de Gestión de Garaje**
**Autor**

Leiber Correa Bravo

**Descripción**

El Sistema Básico de Gestión de Garaje es una aplicación desarrollada en Python que permite registrar y visualizar vehículos dentro de un garaje mediante una interfaz gráfica construida con Tkinter.

El programa está diseñado siguiendo los principios de Programación Orientada a Objetos y una arquitectura modular, separando el sistema en diferentes capas para mejorar la organización, mantenibilidad y comprensión del código.

**Objetivo del Proyecto**

Desarrollar una aplicación que permita:

Registrar vehículos dentro de un sistema.

Mostrar los vehículos registrados en una tabla.

Aplicar conceptos de programación orientada a objetos.

Implementar una arquitectura con separación lógica entre modelo, servicio e interfaz gráfica.

Estructura del Proyecto

El sistema se encuentra organizado en módulos para mantener una separación lógica entre las diferentes responsabilidades del programa.

garaje_app
│
├── modelos
│   └── vehiculo.py
│
├── servicios
│   └── garaje_servicio.py
│
├── ui
│   └── app_tkinter.py
│
└── main.py
**Descripción de cada módulo**

modelos

Contiene las clases que representan las entidades del sistema. En este caso, la clase Vehiculo que almacena los datos de cada vehículo registrado.

servicios

Contiene la lógica del sistema. La clase GarajeServicio se encarga de gestionar los vehículos registrados, permitiendo agregarlos y consultarlos.

ui

Contiene la interfaz gráfica del programa. La clase AppGaraje crea la ventana, los formularios, los botones y la tabla donde se visualizan los vehículos.

main

Es el punto de inicio del programa. Se encarga de crear las instancias necesarias del servicio y de la interfaz gráfica para iniciar la aplicación.

**Funcionamiento del Sistema**

El usuario ingresa los datos del vehículo:

Placa

Marca

Propietario

Al presionar el botón Agregar Vehículo, el sistema:

Obtiene los datos del formulario.

Crea un objeto de tipo Vehiculo.

Envía el objeto al servicio GarajeServicio.

El servicio almacena el vehículo en una lista.

Posteriormente la interfaz actualiza la tabla mostrando todos los vehículos registrados.

El botón Limpiar permite borrar los campos del formulario para registrar un nuevo vehículo.


**Conclusión**

Este proyecto demuestra la aplicación práctica de los principios fundamentales de la programación orientada a objetos, así como la importancia de estructurar adecuadamente un sistema mediante la separación lógica de sus componentes. Esto facilita el mantenimiento, escalabilidad y comprensión del software desarrollado.
