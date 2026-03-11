# Importamos el servicio del garaje
from servicios.garaje_servicio import GarajeServicio

# Importamos la interfaz gráfica
from ui.app_tkinter import AppGaraje


# Función principal del programa
def main():

    # Crear el servicio que manejará los vehículos
    servicio = GarajeServicio()

    # Crear la aplicación y pasar el servicio
    app = AppGaraje(servicio)

    # Ejecutar la aplicación
    app.run()


# Punto de inicio del programa
if __name__ == "__main__":
    main()