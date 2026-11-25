import json


def cargar_alumnos() -> dict[int, dict]:
    """Lee alumnos.json y devuelve los alumnos registrados.

    Abre el archivo, lo convierte a diccionario y transforma las claves (DNI)
    de texto a entero, porque JSON solo admite claves de tipo string. Si el
    archivo no tiene alumnos, devuelve el diccionario tal cual.

    Returns:
        Diccionario {dni: datos_alumno}, con el DNI como int y cada valor con
        las claves 'nombre', 'apellido', 'edad' y 'nota_final'.
    """

    with open("alumnos.json", "r", encoding="utf-8") as archivo:
        alumnos = json.load(archivo)

    if len(alumnos) == 0:
        return alumnos

    for dni in list(alumnos.keys()):
        alumnos[int(dni)] = alumnos.pop(dni)

    return alumnos   

def guardar_alumnos(alumnos: dict[int, dict]) -> None:
    """Guarda los alumnos registrados en alumnos.json.

    Sobrescribe el archivo con el contenido actual del diccionario. Como JSON
    solo admite claves de texto, los DNI (int) se guardan como string; por eso
    cargar_alumnos los vuelve a convertir a int al leer.

    Args:
        alumnos: diccionario {dni: datos_alumno} con los alumnos a guardar.

    Returns:
        None. El resultado queda escrito en el archivo.
    """
    # Modo "w": abre el archivo para escritura y lo crea si no existe;
    # si ya existe, reemplaza todo su contenido.
    # "with" se encarga de cerrar el archivo al terminar.
    with open("alumnos.json", "w", encoding="utf-8") as archivo:
        # indent=4 deja el JSON ordenado y legible.
        # ensure_ascii=False conserva tildes y ñ en vez de escribirlas como \u00e9.
        json.dump(alumnos, archivo, indent=4, ensure_ascii=False)
