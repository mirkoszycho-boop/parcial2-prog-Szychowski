def es_decimal(texto: str) -> bool:
    """Indica si un texto representa un número positivo, entero o decimal.

    Acepta como máximo un punto decimal (por ejemplo "8", "7.5" o "0.5").
    Rechaza textos vacíos, con letras, con signo negativo y con más de un
    punto (por ejemplo "1.2.3").

    Args:
        texto: Cadena a validar. Si el usuario usó coma como separador, debe
            reemplazarse por punto antes de llamar a esta función.

    Returns:
        True si el texto tiene forma de número positivo, False en caso
        contrario.
    """
    # replace(".", "", 1) elimina solo el primer punto: si había un único
    # punto decimal queda un texto de puros dígitos, y si había dos o más
    # todavía queda un punto, por lo que isdigit() da False.
    # isdigit() también rechaza el signo "-" y el texto vacío.
    return texto.replace(".", "", 1).isdigit()

def pedir_texto(mensaje: str) -> str:
    """Solicita una cadena de texto por consola hasta que sea válida.

    Muestra mensaje, lee la entrada del usuario y repite la solicitud
    mientras validar_textos indique que el texto no es válido.

    Args:
        mensaje: Texto que se muestra al usuario al solicitar el dato.

    Returns:
        La cadena ingresada por el usuario una vez validada.
    """
    texto = input(mensaje)
    while not validar_textos(texto):
        print("Error: el texto no puede estar vacío ni contener caracteres inválidos.")
        texto = input(mensaje)
    return texto


def pedir_entero(mensaje: str) -> int:
    """Solicita un número entero no negativo por consola hasta que sea válido.

    Muestra mensaje, lee la entrada sin espacios extremos con strip() y
    repite la solicitud mientras validar_entero_no_negativo retorne False.
    Finalmente convierte la cadena validada a entero.

    Args:
        mensaje: Texto que se muestra al usuario al solicitar el número.

    Returns:
        El número entero no negativo ingresado y validado.
    """
    texto = input(mensaje).strip()
    while not validar_entero_no_negativo(texto):
        texto = input(mensaje).strip()
    return int(texto)


def pedir_decimal(mensaje: str) -> float:
    """Pide un numero decimal por consola hasta que el usuario ingrese uno valido.

    Acepta coma o punto como separador decimal (por ejemplo "7,5" o "7.5").
    Repite la pregunta mientras el texto no tenga forma de numero.

    Args:
        mensaje: texto que se muestra al usuario al pedir el dato.

    Returns:
        El numero ingresado, convertido a float.
    """
    # strip() saca espacios sobrantes y replace() cambia la coma por punto,
    # porque float() solo entiende el punto como separador decimal
    texto = input(mensaje).strip().replace(",", ".")

    # Mientras el texto no sea un numero valido, avisamos y volvemos a pedir.
    # Validamos ANTES de convertir, asi float() nunca recibe algo invalido
    # y no hace falta try/except
    while not es_decimal(texto):
        print("Debe ingresar un numero.")
        texto = input(mensaje).strip().replace(",", ".")

    # Llegados aca el texto ya esta validado, la conversion es segura
    return float(texto)


def pedir_dni(mensaje: str) -> int:
    """Solicita y valida un número de DNI de entre 7 y 8 dígitos por consola.

    Utiliza pedir_entero para obtener un entero no negativo y repite la
    solicitud mientras el valor esté fuera del rango 3000000 a 90000000.

    Args:
        mensaje: Texto que se muestra al usuario al solicitar el DNI.

    Returns:
        El número de DNI validado como entero dentro del rango de 7 u 8 dígitos.
    """
    validar = pedir_entero(mensaje)

    while validar < 3000000 or validar > 90000000:
        print("Error: el DNI debe tener entre 7 y 8 dígitos.")
        validar = pedir_entero(mensaje)
    return validar


def pedir_edad(mensaje: str) -> int:
    """Solicita una edad por consola hasta que esté entre 18 y 100 años.

    Usa pedir_entero para asegurar que lo ingresado sea un número entero y,
    después, verifica que esté dentro del rango permitido. Repite la
    solicitud mientras la edad quede fuera de ese rango.

    Args:
        mensaje: Texto que se muestra al usuario al solicitar la edad.

    Returns:
        La edad ingresada y validada, un entero entre 18 y 100 inclusive.
    """
    # pedir_entero ya garantiza que sea un entero no negativo
    edad = pedir_entero(mensaje)

    # Validación de la regla de negocio: el rango permitido
    while edad < 18 or edad > 100:
        print("La edad debe estar entre 18 y 100 años")
        edad = pedir_entero(mensaje)

    return edad


def pedir_nota(mensaje: str) -> float:
    """Solicita una nota por consola hasta que esté entre 0 y 10.

    Usa pedir_decimal para asegurar que lo ingresado sea un número y, después,
    verifica que esté dentro del rango permitido. Repite la solicitud mientras
    la nota quede fuera de ese rango.

    Args:
        mensaje: Texto que se muestra al usuario al solicitar la nota.

    Returns:
        La nota ingresada y validada, un float entre 0 y 10 inclusive.
    """
    # pedir_decimal ya garantiza que sea un número válido (acepta coma o punto)
    nota = pedir_decimal(mensaje)

    # Validación de la regla de negocio: la nota debe estar entre 0 y 10
    while nota < 0 or nota > 10:
        print("La nota debe estar entre 0 y 10")
        nota = pedir_decimal(mensaje)

    return nota


def validar_textos(texto: str) -> bool:
    """Valida que una cadena de texto no esté vacía y contenga solo letras y espacios.

    Recorre cada carácter de texto para verificar que sea una letra
    minúscula ('a'-'z'), mayúscula ('A'-'Z') o espacio (' '), y
    finalmente verifica con strip() != "" que no esté vacía ni formada solo
    por espacios.

    Args:
        texto: Cadena de texto ingresada por el usuario.

    Returns:
        True si el texto cumple con los caracteres permitidos y no está vacío
        tras eliminar espacios extremos, False en caso contrario.
    """
    for i in range(len(texto)):
        caracter = texto[i]
        es_minuscula = "a" <= caracter <= "z"
        es_mayuscula = "A" <= caracter <= "Z"
        tiene_espacio = caracter == " "

        if not (es_minuscula or es_mayuscula or tiene_espacio):
            return False

    return texto.strip() != ""


def validar_entero_no_negativo(texto: str) -> bool:
    """Valida que una cadena represente un número entero no negativo.

    Verifica que el texto no esté vacío y que todos sus caracteres sean
    dígitos numéricos entre '0' y '9', mostrando un mensaje de error por
    consola si no cumple alguna condición.

    Args:
        texto: Cadena de texto a validar.

    Returns:
        True si la cadena no está vacía y todos sus caracteres están entre
        '0' y '9', o False en caso contrario.
    """
    if texto == "":
        print("\nError, no se puede ingresar un valor vacío.")
        return False

    for i in range(len(texto)):
        if texto[i] < "0" or texto[i] > "9":
            print("\nError, el valor ingresado debe ser un entero positivo.")
            return False

    return True    