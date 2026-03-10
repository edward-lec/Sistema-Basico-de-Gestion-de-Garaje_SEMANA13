# Importación de la librería Tkinter para crear interfaces gráficas
import tkinter as tk

# Importación de ttk para usar componentes avanzados como tablas
from tkinter import ttk

# Importamos la clase Vehiculo del módulo modelos
from modelos.vehiculo import Vehiculo

# Importamos el servicio del garaje
from servicios.garaje_servicio import GarajeServicio


# Clase que representa la aplicación gráfica
class AppGaraje:

    # Constructor de la aplicación
    def __init__(self, root):

        # Ventana principal
        self.root = root

        # Título de la ventana
        self.root.title("Sistema Básico de Gestión de Garaje")

        # Instancia del servicio que manejará los vehículos
        self.servicio = GarajeServicio()


        # CREACIÓN DEL FORMULARIO


        # Etiqueta para el campo placa
        tk.Label(root, text="Placa").grid(row=0, column=0)

        # Campo de texto para ingresar la placa
        self.entry_placa = tk.Entry(root)
        self.entry_placa.grid(row=0, column=1)


        # Etiqueta para el campo marca
        tk.Label(root, text="Marca").grid(row=1, column=0)

        # Campo de texto para ingresar la marca
        self.entry_marca = tk.Entry(root)
        self.entry_marca.grid(row=1, column=1)


        # Etiqueta para el campo propietario
        tk.Label(root, text="Propietario").grid(row=2, column=0)

        # Campo de texto para ingresar el propietario
        self.entry_propietario = tk.Entry(root)
        self.entry_propietario.grid(row=2, column=1)



        # BOTONES


        # Botón para agregar un vehículo
        btn_agregar = tk.Button(
            root,
            text="Agregar Vehículo",
            command=self.agregar_vehiculo   # Llama al método agregar_vehiculo
        )
        btn_agregar.grid(row=3, column=0)


        # Botón para limpiar los campos del formulario
        btn_limpiar = tk.Button(
            root,
            text="Limpiar",
            command=self.limpiar_campos
        )
        btn_limpiar.grid(row=3, column=1)



        # TABLA PARA MOSTRAR VEHÍCULOS


        # Creación de una tabla usando Treeview
        self.tabla = ttk.Treeview(
            root,
            columns=("placa", "marca", "propietario"),
            show="headings"
        )

        # Nombre de las columnas
        self.tabla.heading("placa", text="Placa")
        self.tabla.heading("marca", text="Marca")
        self.tabla.heading("propietario", text="Propietario")

        # Posición de la tabla en la ventana
        self.tabla.grid(row=4, column=0, columnspan=2)



    # MÉTODO PARA AGREGAR VEHÍCULOS

    def agregar_vehiculo(self):

        # Obtener los valores ingresados en los campos
        placa = self.entry_placa.get()
        marca = self.entry_marca.get()
        propietario = self.entry_propietario.get()

        # Crear un objeto Vehiculo con los datos ingresados
        vehiculo = Vehiculo(placa, marca, propietario)

        # Enviar el vehículo al servicio para guardarlo
        self.servicio.agregar_vehiculo(vehiculo)

        # Actualizar la tabla para mostrar el nuevo vehículo
        self.actualizar_tabla()

        # Limpiar los campos después de agregar
        self.limpiar_campos()



    # MÉTODO PARA ACTUALIZAR LA TABLA

    def actualizar_tabla(self):

        # Elimina todos los elementos actuales de la tabla
        for item in self.tabla.get_children():
            self.tabla.delete(item)

        # Recorre todos los vehículos almacenados
        for vehiculo in self.servicio.obtener_vehiculos():

            # Inserta cada vehículo como una nueva fila
            self.tabla.insert(
                "",
                "end",
                values=(vehiculo.placa, vehiculo.marca, vehiculo.propietario)
            )



    # MÉTODO PARA LIMPIAR LOS CAMPOS

    def limpiar_campos(self):

        # Borra el contenido del campo placa
        self.entry_placa.delete(0, tk.END)

        # Borra el contenido del campo marca
        self.entry_marca.delete(0, tk.END)

        # Borra el contenido del campo propietario
        self.entry_propietario.delete(0, tk.END)