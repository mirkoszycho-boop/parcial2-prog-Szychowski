from archivos import guardar_alumnos
from validaciones import (
    pedir_dni,
    pedir_edad,
    pedir_entero,
    pedir_nota,
    pedir_texto
)


def alumnos_vacios(alumnos: dict[int, dict]) -> bool:
    """Verifica si el diccionario de alumnos está vacío.

    Args:
        alumnos: Diccionario con el formato {dni: datos_alumno}.

    Returns:
        True si alumnos está vacío, False en caso contrario.
    """
    if len(alumnos) == 0:
        print("\nNo hay alumnos registrados.")
        return True
    return False

def buscar_por_dni(alumnos: dict[int, dict], dni: int) -> int | None:
    """Busca un DNI entre los alumnos registrados.

    Recorre las claves del diccionario (los DNI) y compara cada una con el
    DNI buscado.

    Args:
        alumnos: diccionario {dni: datos_alumno} con los alumnos registrados.
        dni: DNI que se quiere buscar.

    Returns:
        El DNI si existe en el registro, o None si no se encontró. Con ese DNI
        se accede a los datos del alumno mediante alumnos[dni].
    """
    # Recorrer un diccionario devuelve sus claves, que acá son los DNI
    for alumno in alumnos:
        if alumno == dni:
            return alumno

    # Si terminó el bucle sin coincidencias, el DNI no está registrado
    return None


def mostrar_alumno(dni: int, datos: dict) -> None:
    """Muestra por consola los datos de un alumno.

    Imprime DNI, nombre, apellido, edad y nota final, uno por línea.

    Args:
        dni: DNI del alumno, que es la clave en el diccionario de alumnos.
        datos: diccionario con los datos del alumno, con las claves
            'nombre', 'apellido', 'edad' y 'nota'.

    Returns:
        None. Solo imprime por consola.
    """
    print(f"DNI: {dni}")
    print(f"Nombre: {datos['nombre']}")
    print(f"Apellido: {datos['apellido']}")
    print(f"Edad: {datos['edad']}")
    print(f"Nota final: {datos['nota']}")


def registrar_alumnos(alumnos: dict[int, dict]) -> dict[int, dict]:
    """Registra uno o mas alumnos pidiendo los datos por consola.

    Pregunta cuantos alumnos se van a cargar y, por cada uno, pide DNI, nombre,
    apellido, edad y nota final. No permite DNI repetidos.

    Args:
        alumnos: diccionario {dni: datos_alumno} donde se agregan los nuevos.

    Returns:
        El mismo diccionario, con cada alumno nuevo guardado bajo su DNI y con
        las claves 'nombre', 'apellido', 'edad' y 'nota'.
    """
    cantidad = pedir_entero("\nIngrese la cantidad de alumnos a registrar: ")

    for i in range(cantidad):
        print(f"\nRegistro del alumno {i + 1}")

        dni = pedir_dni("\nIngrese el DNI del alumno: ")
        while buscar_por_dni(alumnos, dni) != None:
            print("El DNI ingresado ya existe. Ingrese otro.")
            dni = pedir_dni("\nIngrese el DNI del alumno: ")

        nombre = pedir_texto("\nIngrese el nombre del alumno: ")
        apellido = pedir_texto("\nIngrese el apellido del alumno: ")
        edad = pedir_edad("\nIngrese la edad del alumno: ")
        nota = pedir_nota("\nIngrese la nota final del alumno: ")

        alumnos[dni] = {
            "nombre": nombre,
            "apellido": apellido,
            "edad": edad,
            "nota": nota,
        }
        print("\nSe ha registrado el alumno exitosamente.")

    print("Registro de alumnos completado.")
    print(f"Alumnos registrados: {cantidad}")

    return alumnos


def listar_alumnos(alumnos: dict[int, dict]) -> None:
    """Muestra por consola todos los alumnos registrados.

    Si no hay alumnos registrados, no imprime el listado. En caso contrario
    recorre el diccionario y muestra los datos de cada alumno, separados por
    una línea de guiones.

    Args:
        alumnos: diccionario {dni: datos_alumno} con los alumnos registrados.

    Returns:
        None. Solo imprime por consola.
    """
    if alumnos_vacios(alumnos):
        return None

    # items() devuelve cada par (dni, datos), así tenemos ambos en cada vuelta
    for dni, datos in alumnos.items():
        print("====================================")
        mostrar_alumno(dni, datos)

    # Línea de cierre después del último alumno
    print("====================================")


def buscar_alumno(alumnos: dict[int, dict]) -> bool:
    """Busca un alumno por DNI y muestra sus datos por consola.

    Si no hay alumnos registrados, no pide nada y devuelve False. En caso
    contrario pide un DNI y, si existe, muestra DNI, nombre, apellido, edad y
    nota final del alumno.

    Args:
        alumnos: diccionario {dni: datos_alumno} con los alumnos registrados.

    Returns:
        True si el alumno fue encontrado y mostrado; False si el registro
        estaba vacío o el DNI no se encontró.
    """
    if alumnos_vacios(alumnos):
        return False

    dni = pedir_dni("\nIngrese el DNI del alumno a buscar: ")
    alumno_encontrado = buscar_por_dni(alumnos, dni)

    if alumno_encontrado is None:
        print("\nAlumno no encontrado.")
        return False

    alumno = alumnos[alumno_encontrado]
    print(alumno)
    print("\n====================================")
    print(f"DNI: {alumno_encontrado}")
    print(f"Nombre: {alumno['nombre']}")
    print(f"Apellido: {alumno['apellido']}")
    print(f"Edad: {alumno['edad']}")
    print(f"Nota final: {alumno['nota']}")
    return True 



def mostrar_menu_modificacion() -> None:
    """Muestra por consola el menú de campos que se pueden modificar.

    Imprime las opciones numeradas del 1 al 5: nombre, apellido, edad, nota
    y volver. No lee ninguna opción ni devuelve nada; quien la llama es el
    responsable de pedir y procesar la opción elegida.

    Returns:
        None. Solo imprime el menú.
    """
    print("\n¿Que desea modificar?")
    print("1. Nombre")
    print("2. Apellido")
    print("3. Edad")
    print("4. Nota")
    print("5. Volver")


def modificar_alumno(alumnos: dict[int, dict]) -> dict[int, dict]:
    """Reemplaza los datos de un alumno existente a partir de su DNI.

    Si no hay alumnos registrados, devuelve el registro sin cambios. En caso
    contrario pide un DNI por consola y, si existe, muestra los datos actuales
    y solicita los nuevos valores de nombre, apellido, edad y nota final. El
    DNI no se modifica porque es la clave del diccionario.

    Args:
        alumnos: diccionario {dni: datos_alumno} con los alumnos registrados.

    Returns:
        El mismo diccionario, con los datos del alumno actualizados (o sin
        cambios si el registro estaba vacio o el DNI no se encontro).
    """
    if alumnos_vacios(alumnos):
        return alumnos

    dni = pedir_dni("\nIngrese el DNI del alumno a modificar: ")
    alumno_encontrado = buscar_por_dni(alumnos, dni)

    if alumno_encontrado != None:
        alumno = alumnos[alumno_encontrado]
        print("\nAlumno encontrado:")
        print(f"\nDNI: {alumno_encontrado}")
        print(f"Nombre: {alumno['nombre']}")
        print(f"Apellido: {alumno['apellido']}")
        print(f"Edad: {alumno['edad']}")
        print(f"Nota final: {alumno['nota']}")

        nombre = pedir_texto("\nIngrese el nuevo nombre del alumno: ")
        apellido = pedir_texto("\nIngrese el nuevo apellido del alumno: ")
        edad = pedir_edad("\nIngrese la nueva edad del alumno: ")
        nota = pedir_nota("\nIngrese la nueva nota final del alumno: ")

        alumnos[alumno_encontrado] = {
            "nombre": nombre,
            "apellido": apellido,
            "edad": edad,
            "nota": nota,
        }

        print("\nAlumno modificado exitosamente.")
    else:
        print("\nAlumno no encontrado.")

    return alumnos


def eliminar_alumno(alumnos: dict[int, dict]) -> dict[int, dict]:
    """Elimina un alumno del registro a partir de su DNI.

    Si no hay alumnos cargados, devuelve el registro sin cambios. En caso
    contrario pide un DNI por consola y, si existe, borra al alumno.

    Args:
        alumnos: diccionario {dni: datos_alumno} con los alumnos registrados.

    Returns:
        El mismo diccionario, sin el alumno eliminado (o sin cambios si el
        registro estaba vacio o el DNI no se encontro).
    """
    if alumnos_vacios(alumnos):
        return alumnos

    dni = pedir_dni("\nIngrese el DNI del alumno que quiere eliminar: ")
    alumno_encontrado = buscar_por_dni(alumnos, dni)

    if alumno_encontrado != None:
        del alumnos[alumno_encontrado]
        print("\nAlumno eliminado exitosamente.")
    else:
        print("\nAlumno no encontrado.")

    return alumnos