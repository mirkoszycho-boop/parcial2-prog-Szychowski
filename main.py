from archivos import guardar_alumnos, cargar_alumnos
from alumnos import (
    buscar_alumno,
    eliminar_alumno,
    listar_alumnos,
    modificar_alumno,
    registrar_alumnos,
)
from estadisticas import mostrar_estadisticas
from validaciones import pedir_entero


menu = False
alumnos = cargar_alumnos()

while not menu:
    print("\n========== GESTION DE ALUMNOS ==========")
    print("1. Registrar alumno")
    print("2. Listar alumnos")
    print("3. Buscar alumno")
    print("4. Modificar alumno")
    print("5. Eliminar alumno")
    print("6. Ver estadisticas")
    print("7. Salir del menu")

    opcion = pedir_entero("\nSeleccione una opción: ")

    match opcion:
        case 1:
            registrar_alumnos(alumnos)
            guardar_alumnos(alumnos)
        case 2:
            listar_alumnos(alumnos)
        case 3:
            buscar_alumno(alumnos)
        case 4:
            modificar_alumno(alumnos)
            guardar_alumnos(alumnos)
        case 5:
            eliminar_alumno(alumnos)
            guardar_alumnos(alumnos)
        case 6:
            mostrar_estadisticas(alumnos)
        case 7:
            print("Saliendo Del Menu")
            menu = True
        case _:
            print("\nOpcion invalida, intente de nuevo.")
