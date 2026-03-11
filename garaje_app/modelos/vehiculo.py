# Clase que representa un vehículo dentro del garaje
class Vehiculo:

    # Constructor de la clase
    def __init__(self, placa, marca, propietario):

        # Atributos privados del vehículo
        self.__placa = placa
        self.__marca = marca
        self.__propietario = propietario



    # GETTERS


    # Método para obtener la placa
    def get_placa(self):
        return self.__placa


    # Método para obtener la marca
    def get_marca(self):
        return self.__marca


    # Método para obtener el propietario
    def get_propietario(self):
        return self.__propietario



    # SETTERS


    # Método para modificar la placa
    def set_placa(self, placa):
        self.__placa = placa


    # Método para modificar la marca
    def set_marca(self, marca):
        self.__marca = marca


    # Método para modificar el propietario
    def set_propietario(self, propietario):
        self.__propietario = propietario


    # Método que muestra el vehículo como texto
    def __str__(self):
        return f"{self.__placa} - {self.__marca} - {self.__propietario}"