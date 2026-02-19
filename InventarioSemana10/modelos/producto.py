
# Clase Producto
# Representa un producto dentro del sistema de inventario
# Autor: Leiber Correa Bravo

class Producto:
    def __init__(self, codigo, nombre, cantidad, precio):
        """
        Constructor de la clase Producto.

        Parámetros:
        codigo   -> Identificador único del producto.
        nombre   -> Nombre del producto.
        cantidad -> Cantidad disponible en inventario.
        precio   -> Precio unitario del producto.
        """

        # Atributos del producto
        self.codigo = codigo
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio


    # MÉTODOS GETTERS


    def get_codigo(self):
        """
        Retorna el código del producto.
        """
        return self.codigo

    def get_nombre(self):
        """
        Retorna el nombre del producto.
        """
        return self.nombre

    def get_cantidad(self):
        """
        Retorna la cantidad disponible del producto.
        """
        return self.cantidad

    def get_precio(self):
        """
        Retorna el precio del producto.
        """
        return self.precio


    # MÉTODOS SETTERS


    def set_codigo(self, codigo):
        """
        Modifica el código del producto.
        """
        self.codigo = codigo

    def set_nombre(self, nombre):
        """
        Modifica el nombre del producto.
        """
        self.nombre = nombre

    def set_cantidad(self, cantidad):
        """
        Modifica la cantidad del producto.
        """
        self.cantidad = cantidad

    def set_precio(self, precio):
        """
        Modifica el precio del producto.
        """
        self.precio = precio


    # MÉTODO ESPECIAL


    def __str__(self):
        """
        Convierte el objeto Producto en una cadena de texto.
        Se utiliza para guardar la información en el archivo.

        Formato:
        codigo,nombre,cantidad,precio
        """
        return f"{self.codigo},{self.nombre},{self.cantidad},{self.precio}"