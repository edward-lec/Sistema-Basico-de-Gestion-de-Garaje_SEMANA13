# Clase que representa un vehículo dentro del garaje
class Vehiculo:

    # Constructor de la clase
    # Se ejecuta cuando se crea un nuevo objeto Vehiculo
    def __init__(self, placa, marca, propietario):

        # Atributo que guarda la placa del vehículo
        self.placa = placa

        # Atributo que guarda la marca del vehículo
        self.marca = marca

        # Atributo que guarda el nombre del propietario
        self.propietario = propietario


    # Método especial que define cómo se mostrará el objeto como texto
    def __str__(self):

        # Retorna una representación en texto del vehículo
        return f"{self.placa} - {self.marca} - {self.propietario}"