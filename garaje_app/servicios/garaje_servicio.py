
# CLASE DE SERVICIO PARA LA GESTIÓN DEL GARAJE

# Este archivo contiene la lógica del sistema relacionada
# con el manejo de los vehículos dentro del garaje.
# Aquí se almacenan, agregan y consultan los vehículos.


class GarajeServicio:

    # CONSTRUCTOR DE LA CLASE

    # Se ejecuta cuando se crea una instancia de
    # la clase GarajeServicio.
    def __init__(self):

        # Lista donde se almacenarán los vehículos registrados
        self.vehiculos = []



    # MÉTODO: AGREGAR VEHÍCULO

    # Este método recibe un objeto de tipo Vehiculo
    # y lo guarda en la lista de vehículos.
    def agregar_vehiculo(self, vehiculo):

        # Se agrega el vehículo a la lista
        self.vehiculos.append(vehiculo)



    # MÉTODO: OBTENER VEHÍCULOS

    # Este método retorna la lista completa de vehículos
    # registrados en el sistema.
    def obtener_vehiculos(self):

        # Retorna la lista de vehículos
        return self.vehiculos
