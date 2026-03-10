# Clase que maneja la lógica del garaje
class GarajeServicio:

    # Constructor de la clase
    def __init__(self):

        # Lista donde se almacenarán los vehículos registrados
        self.vehiculos = []


    # Método para agregar un vehículo al garaje
    def agregar_vehiculo(self, vehiculo):

        # Agrega el objeto vehiculo a la lista
        self.vehiculos.append(vehiculo)


    # Método para obtener todos los vehículos registrados
    def obtener_vehiculos(self):

        # Retorna la lista completa de vehículos
        return self.vehiculos
