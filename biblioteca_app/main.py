# main.py

"""
Punto de entrada del programa.

Responsabilidad:
- Mostrar menú.
- Capturar entradas del usuario.
- Llamar a los métodos del servicio.

NO contiene lógica de negocio.
"""

from servicios.biblioteca_servicio import BibliotecaServicio


def mostrar_menu():
    print("SISTEMA DE BIBLIOTECA DIGITAL")
    print("1. Agregar libro")
    print("2. Quitar libro")
    print("3. Registrar usuario")
    print("4. Dar de baja usuario")
    print("5. Prestar libro")
    print("6. Devolver libro")
    print("7. Buscar por título")
    print("8. Buscar por autor")
    print("9. Buscar por categoría")
    print("10. Listar libros de usuario")
    print("0. Salir")


def main():
    biblioteca = BibliotecaServicio()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            biblioteca.agregar_libro(
                input("Título: "),
                input("Autor: "),
                input("Categoría: "),
                input("ISBN: ")
            )

        elif opcion == "2":
            biblioteca.quitar_libro(input("ISBN: "))

        elif opcion == "3":
            biblioteca.registrar_usuario(
                input("Nombre: "),
                input("ID: ")
            )

        elif opcion == "4":
            biblioteca.dar_baja_usuario(input("ID: "))

        elif opcion == "5":
            biblioteca.prestar_libro(
                input("ID usuario: "),
                input("ISBN libro: ")
            )

        elif opcion == "6":
            biblioteca.devolver_libro(
                input("ID usuario: "),
                input("ISBN libro: ")
            )

        elif opcion == "7":
            biblioteca.buscar_por_titulo(input("Título: "))

        elif opcion == "8":
            biblioteca.buscar_por_autor(input("Autor: "))

        elif opcion == "9":
            biblioteca.buscar_por_categoria(input("Categoría: "))

        elif opcion == "10":
            biblioteca.listar_libros_usuario(input("ID usuario: "))

        elif opcion == "0":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción inválida.")


if __name__ == "__main__":
    main()