from alumnos import alumnos_vacios 

NOTA_APROBACION = 6


def cantidad_total(alumnos: dict[int, dict]) -> int:
    """Devuelve la cantidad total de alumnos registrados.

    Args:
        alumnos: diccionario {dni: datos_alumno} con los alumnos registrados.

    Returns:
        Cantidad de alumnos como entero (0 si el registro está vacío).
    """
    # len() sobre un diccionario cuenta sus claves, y cada clave es un alumno
    return len(alumnos)


def promedio_notas(alumnos: dict) -> float | None:
    """Calcula el promedio de las notas de todos los alumnos.

    Args:
        alumnos: Diccionario que contiene los alumnos y sus respectivas notas.

    Returns:
        El promedio de las notas o None si no hay alumnos.
    """
    if alumnos_vacios(alumnos):
        return None

    suma = 0
    for alumno in alumnos.values():
        suma += alumno["nota"]

    return suma / len(alumnos)


def alumno_mejor_nota(alumnos: dict) -> None:
    """Busca y muestra el alumno que obtuvo la nota más alta.

    Args:
        alumnos: Diccionario que contiene los nombres de los alumnos y sus notas.

    Returns:
        None: No devuelve ningún valor.
    """
    if alumnos_vacios(alumnos):
        return None

    nota_mejor = 0
    nombre_mejor = ""

    for alumno in alumnos.values():
        if alumno["nota"] > nota_mejor:
            nota_mejor = alumno["nota"]
            nombre_mejor = alumno["nombre"]

    print(f"El alumno con mayor nota es: {nombre_mejor} y su nota es: {nota_mejor}")

    return None



def cantidad_aprobados(alumnos: dict) -> int:
    """Cuenta la cantidad de alumnos que aprobaron.

    Args:
        alumnos: Diccionario que contiene los nombres de los alumnos y sus notas.

    Returns:
        La cantidad total de alumnos que obtuvieron una nota igual o superior a la nota de aprobación.
    """
    contador = 0
    for alumno in alumnos.values():
        if alumno["nota"] >= NOTA_APROBACION:
            contador += 1

    return contador


def cantidad_desaprobados(alumnos: dict) -> int:
    """Cuenta la cantidad de alumnos que desaprobaron.

    Args:
        alumnos: Diccionario que contiene los nombres de los alumnos y sus notas.

    Returns:
        La cantidad total de alumnos que obtuvieron una nota inferior a la nota de aprobación.
    """
    contador = 0
    for alumno in alumnos.values():
        if alumno["nota"] < NOTA_APROBACION:
            contador += 1

    return contador


def mostrar_estadisticas(alumnos: dict) -> None:
    """Muestra las estadísticas generales del curso.

    Args:
        alumnos: Diccionario que contiene los nombres de los alumnos y sus notas.

    Returns:
        None: No devuelve ningún valor, solamente muestra las estadísticas por pantalla.
    """
    if alumnos_vacios(alumnos):
        return None

    print("\n===== ESTADISTICAS =====")
    print(f"Cantidad total de alumnos: {cantidad_total(alumnos)}")
    print(f"Promedio de notas: {promedio_notas(alumnos):.2f}")
    alumno_mejor_nota(alumnos)
    print(f"Aprobados: {cantidad_aprobados(alumnos)}")
    print(f"Desaprobados: {cantidad_desaprobados(alumnos)}")