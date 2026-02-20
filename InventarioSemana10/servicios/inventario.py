# Clase Inventario
# Maneja la lógica principal del sistema de inventario
# y la manipulación del archivo inventario.txt
# Autor: Leiber Correa Bravo

import os
from modelos.producto import Producto


class Inventario:
    def __init__(self, archivo="inventario.txt"):
        """
        Constructor de la clase Inventario.

        Parámetro:
        archivo -> nombre del archivo donde se almacenarán los productos.

        Se define una ruta base para asegurar que el archivo
        se guarde correctamente dentro del proyecto.
        """

        # Obtiene la ruta absoluta del archivo actual (directorio base)
        base_dir = os.path.dirname(os.path.abspath(__file__))

        # Construye la ruta completa del archivo inventario.txt
        self.archivo = os.path.join(base_dir, archivo)

        # Diccionario que almacena los productos en memoria
        # Clave: código del producto
        # Valor: objeto Producto
        self.productos = {}

        # Al iniciar el sistema, se cargan los productos guardados previamente
        self.cargar_desde_archivo()


    # MÉTODO: CARGAR DESDE ARCHIVO


    def cargar_desde_archivo(self):
        """
        Lee el archivo inventario.txt y reconstruye
        los objetos Producto almacenados previamente.
        """

        try:
            # Se abre el archivo en modo lectura
            with open(self.archivo, "r") as file:
                for linea in file:
                    # Se eliminan espacios y saltos de línea
                    datos = linea.strip().split(",")

                    # Validación: debe tener exactamente 4 datos
                    if len(datos) == 4:
                        codigo, nombre, cantidad, precio = datos

                        # Se crea el objeto Producto
                        producto = Producto(
                            codigo,
                            nombre,
                            int(cantidad),
                            float(precio)
                        )

                        # Se guarda en el diccionario usando el getter
                        self.productos[producto.get_codigo()] = producto

        except FileNotFoundError:
            # Si el archivo no existe, se crea automáticamente vacío
            with open(self.archivo, "w") as _file_:
                pass

        except PermissionError:
            print("Error: No tienes permisos para leer el archivo.")

        except Exception as e:
            print("Error inesperado al cargar archivo:", e)


    # MÉTODO: GUARDAR EN ARCHIVO


    def guardar_en_archivo(self):
        """
        Guarda todos los productos almacenados en memoria
        dentro del archivo inventario.txt.

        Se utiliza el modo 'w' (sobrescritura),
        por lo que el archivo se actualiza completamente.
        """

        try:
            with open(self.archivo, "w") as file:
                for producto in self.productos.values():
                    file.write(str(producto) + "\n")

        except PermissionError:
            print("Error: No tienes permisos para escribir en el archivo.")

        except Exception as e:
            print("Error inesperado al guardar archivo:", e)


    # MÉTODO: AGREGAR PRODUCTO


    def agregar_producto(self, producto):
        """
        Agrega un nuevo producto al inventario.
        Si el código ya existe, no se permite duplicación.
        """

        if producto.get_codigo() in self.productos:
            print("El producto ya existe.")
        else:
            self.productos[producto.get_codigo()] = producto
            self.guardar_en_archivo()
            print("Producto agregado y guardado correctamente.")


    # MÉTODO: ACTUALIZAR PRODUCTO

    def actualizar_producto(self, codigo, cantidad, precio):
        """
        Actualiza la cantidad y el precio de un producto existente.
        """

        if codigo in self.productos:
            self.productos[codigo].set_cantidad(cantidad)
            self.productos[codigo].set_precio(precio)
            self.guardar_en_archivo()
            print("Producto actualizado correctamente.")
        else:
            print("Producto no encontrado.")


    # MÉTODO: ELIMINAR PRODUCTO


    def eliminar_producto(self, codigo):
        """
        Elimina un producto del inventario usando su código.
        """

        if codigo in self.productos:
            del self.productos[codigo]
            self.guardar_en_archivo()
            print("Producto eliminado correctamente.")
        else:
            print("Producto no encontrado.")


    # MÉTODO: MOSTRAR PRODUCTOS


    def mostrar_productos(self):
        """
        Muestra en pantalla todos los productos
        actualmente almacenados en el sistema.
        """

        if not self.productos:
            print("Inventario vacío.")
        else:
            for producto in self.productos.values():
                print(producto)
