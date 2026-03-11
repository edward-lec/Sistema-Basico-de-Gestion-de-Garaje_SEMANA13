# =====================================================
# IMPORTACIONES
# =====================================================

# Importamos la librería tkinter para crear la interfaz gráfica
import tkinter as tk

# Importamos ttk para usar componentes avanzados como tablas (Treeview)
from tkinter import ttk

# Importamos la clase Vehiculo desde la carpeta modelos
from modelos.vehiculo import Vehiculo


# =====================================================
# CLASE DE LA INTERFAZ GRÁFICA
# =====================================================
# Esta clase se encarga de crear y manejar toda la interfaz
# gráfica del sistema de gestión de garaje.
# Aquí se crean los formularios, botones y la tabla donde
# se muestran los vehículos registrados.

class AppGaraje:

    # -------------------------------------------------
    # CONSTRUCTOR DE LA CLASE
    # -------------------------------------------------
    # El constructor se ejecuta cuando se crea un objeto
    # de la clase AppGaraje. Aquí se inicializa la ventana
    # principal y se crean los componentes de la interfaz.

    def __init__(self, servicio):

        # Guardamos el servicio recibido para poder usar
        # sus métodos (agregar y obtener vehículos)
        self.servicio = servicio

        # Crear la ventana principal de la aplicación
        self.root = tk.Tk()

        # Establecer el título de la ventana
        self.root.title("Sistema Básico de Gestión de Garaje")

        # -------------------------------------------------
        # FORMULARIO DE INGRESO DE DATOS
        # -------------------------------------------------
        # Aquí se crean los campos donde el usuario
        # ingresará la información del vehículo.

        # Etiqueta para el campo placa
        tk.Label(self.root, text="Placa").grid(row=0, column=0)

        # Campo de texto para ingresar la placa
        self.entry_placa = tk.Entry(self.root)
        self.entry_placa.grid(row=0, column=1)

        # Etiqueta para el campo marca
        tk.Label(self.root, text="Marca").grid(row=1, column=0)

        # Campo de texto para ingresar la marca
        self.entry_marca = tk.Entry(self.root)
        self.entry_marca.grid(row=1, column=1)

        # Etiqueta para el campo propietario
        tk.Label(self.root, text="Propietario").grid(row=2, column=0)

        # Campo de texto para ingresar el nombre del propietario
        self.entry_propietario = tk.Entry(self.root)
        self.entry_propietario.grid(row=2, column=1)

        # -------------------------------------------------
        # BOTONES DE ACCIÓN
        # -------------------------------------------------
        # Estos botones permiten interactuar con el sistema.

        # Botón para agregar un vehículo al sistema
        btn_agregar = tk.Button(
            self.root,
            text="Agregar Vehículo",
            command=self.agregar_vehiculo  # Ejecuta el método agregar_vehiculo
        )
        btn_agregar.grid(row=3, column=0)

        # Botón para limpiar los campos del formulario
        btn_limpiar = tk.Button(
            self.root,
            text="Limpiar",
            command=self.limpiar_campos  # Ejecuta el método limpiar_campos
        )
        btn_limpiar.grid(row=3, column=1)

        # -------------------------------------------------
        # TABLA PARA MOSTRAR LOS VEHÍCULOS
        # -------------------------------------------------
        # Se utiliza un Treeview para mostrar la lista de
        # vehículos registrados dentro del garaje.

        self.tabla = ttk.Treeview(
            self.root,
            columns=("placa", "marca", "propietario"),
            show="headings"  # Oculta la columna inicial
        )

        # Definimos los encabezados de cada columna
        self.tabla.heading("placa", text="Placa")
        self.tabla.heading("marca", text="Marca")
        self.tabla.heading("propietario", text="Propietario")

        # Ubicamos la tabla en la ventana
        self.tabla.grid(row=4, column=0, columnspan=2)


    # =====================================================
    # MÉTODO PARA AGREGAR VEHÍCULOS
    # =====================================================
    # Este método se ejecuta cuando el usuario presiona
    # el botón "Agregar Vehículo".

    def agregar_vehiculo(self):

        # Obtener los datos ingresados por el usuario
        placa = self.entry_placa.get()
        marca = self.entry_marca.get()
        propietario = self.entry_propietario.get()

        # Crear un objeto Vehiculo con los datos ingresados
        vehiculo = Vehiculo(placa, marca, propietario)

        # Enviar el vehículo al servicio para almacenarlo
        self.servicio.agregar_vehiculo(vehiculo)

        # Actualizar la tabla para mostrar el nuevo vehículo
        self.actualizar_tabla()

        # Limpiar los campos del formulario
        self.limpiar_campos()


    # =====================================================
    # MÉTODO PARA ACTUALIZAR LA TABLA
    # =====================================================
    # Este método se encarga de refrescar la tabla y
    # mostrar todos los vehículos registrados.

    def actualizar_tabla(self):

        # Eliminar todas las filas actuales de la tabla
        for item in self.tabla.get_children():
            self.tabla.delete(item)

        # Recorrer la lista de vehículos almacenados
        for vehiculo in self.servicio.obtener_vehiculos():

            # Insertar cada vehículo como una nueva fila
            self.tabla.insert(
                "",
                "end",
                values=(
                    vehiculo.get_placa(),
                    vehiculo.get_marca(),
                    vehiculo.get_propietario()
                )
            )


    # =====================================================
    # MÉTODO PARA LIMPIAR LOS CAMPOS
    # =====================================================
    # Este método elimina el contenido de los campos
    # del formulario para permitir ingresar nuevos datos.

    def limpiar_campos(self):

        # Borrar el texto del campo placa
        self.entry_placa.delete(0, tk.END)

        # Borrar el texto del campo marca
        self.entry_marca.delete(0, tk.END)

        # Borrar el texto del campo propietario
        self.entry_propietario.delete(0, tk.END)


    # =====================================================
    # MÉTODO PARA EJECUTAR LA APLICACIÓN
    # =====================================================
    # Este método inicia el bucle principal de Tkinter,
    # lo que permite que la interfaz gráfica se mantenga
    # activa y responda a las acciones del usuario.

    def run(self):

        # Inicia el ciclo de ejecución de la interfaz
        self.root.mainloop()