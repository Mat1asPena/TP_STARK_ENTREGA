def mostrar_un_elemento_dict(lista: list, mostrar: str):
    """
    Muestra el valor de un campo específico para cada elemento en una lista de diccionarios.

    Args:
        lista (list): La lista que contiene diccionarios.
        mostrar (str): El campo del diccionario que se quiere mostrar.

    Raises:
        ValueError: Si la lista no es válida o está vacía.
    """
    validar_lista(lista)
    
    for personaje in lista:
        print(personaje[mostrar])

def mostrar_dos_elementos_dict(lista: list, mostrar: str, mostrar_dos: str):
    """
    Muestra dos valores de campos específicos para cada elemento en una lista de diccionarios.

    Args:
        lista (list): La lista que contiene diccionarios.
        mostrar (str): El primer campo del diccionario que se quiere mostrar.
        mostrar_dos (str): El segundo campo del diccionario que se quiere mostrar.

    Raises:
        ValueError: Si la lista no es válida o está vacía.
    """
    validar_lista(lista)
    
    for personaje in lista:
        print(personaje[mostrar], personaje[mostrar_dos])

def extraer_nombre(dic: dict, campo: str) -> str:
    """
    Extrae el valor de un campo específico de un diccionario.

    Args:
        dic (dict): El diccionario del cual extraer el valor.
        campo (str): El campo cuyo valor se desea extraer.

    Returns:
        str: El valor del campo solicitado.

    Raises:
        ValueError: Si el argumento no es un diccionario.
    """
    if not isinstance(dic, dict):
        raise ValueError("Eso no es un diccionario")
    return dic.get(campo)

def extraer_campos_diccionario(dic: dict, campo_uno: str, campo_dos: str) -> str:
    """
    Extrae los valores de dos campos específicos de un diccionario.

    Args:
        dic (dict): El diccionario del cual extraer los valores.
        campo_uno (str): El primer campo cuyo valor se desea extraer.
        campo_dos (str): El segundo campo cuyo valor se desea extraer.

    Returns:
        tuple: Una tupla con los valores de los campos solicitados.

    Raises:
        ValueError: Si el argumento no es un diccionario.
    """
    if not isinstance(dic, dict):
        raise ValueError("Eso no es un diccionario")
    
    dato_campo_uno = dic.get(campo_uno)
    dato_campo_dos = dic.get(campo_dos)
    return dato_campo_uno, dato_campo_dos

def encontrar_mayor_por_campo(lista_de_diccios: list, campo: str) -> dict:
    """
    Encuentra el diccionario con el mayor valor en un campo específico de una lista de diccionarios.

    Args:
        lista_de_diccios (list): La lista de diccionarios a recorrer.
        campo (str): El campo con el que se compara el valor.

    Returns:
        dict: El diccionario que tiene el mayor valor en el campo especificado.

    Raises:
        ValueError: Si la lista no es válida o está vacía.
    """
    validar_lista(lista_de_diccios)
    
    maximo = lista_de_diccios[0]
    for diccionarios in lista_de_diccios:
        if float(diccionarios[campo]) > float(maximo[campo]):
            maximo = diccionarios
    return maximo

def encontrar_menor_por_campo(lista_de_diccios: list, campo: str) -> dict:
    """
    Encuentra el diccionario con el menor valor en un campo específico de una lista de diccionarios.

    Args:
        lista_de_diccios (list): La lista de diccionarios a recorrer.
        campo (str): El campo con el que se compara el valor.

    Returns:
        dict: El diccionario que tiene el menor valor en el campo especificado.

    Raises:
        ValueError: Si la lista no es válida o está vacía.
    """
    validar_lista(lista_de_diccios)
    
    maximo = lista_de_diccios[0]
    for diccionarios in lista_de_diccios:
        if float(diccionarios[campo]) < float(maximo[campo]):
            maximo = diccionarios
    return maximo

def encontrar_mas_bajo(lista: list):
    """
    Encuentra el personaje con la menor altura en una lista de diccionarios.

    Args:
        lista (list): Una lista de diccionarios, donde cada diccionario representa a un personaje y contiene un campo "altura".

    Returns:
        tuple: Una tupla con el nombre del personaje con la menor altura y la altura en sí (nombre, altura).

    Raises:
        ValueError: Si la lista no es válida o está vacía.
    """
    validar_lista(lista)
    
    menor_altura = 1000000000000000000000000000
    heroe_menos_alto = None

    for personaje in lista:
        altura = float(personaje["altura"])
        if altura < menor_altura:
            menor_altura = altura
            heroe_menos_alto = personaje["nombre"]

    return heroe_menos_alto, menor_altura

def encontrar_mas_alto(lista: list):
    """
    Encuentra el personaje con la mayor altura en una lista de diccionarios.

    Args:
        lista (list): Una lista de diccionarios, donde cada diccionario representa a un personaje y contiene un campo "altura".

    Returns:
        tuple: Una tupla con el nombre del personaje con la mayor altura y la altura en sí (nombre, altura).

    Raises:
        ValueError: Si la lista no es válida o está vacía.
    """
    validar_lista(lista)
    
    maxima_altura = 0
    heroe_mas_alto = None

    for personaje in lista:
        altura = float(personaje["altura"])
        if altura > maxima_altura:
            maxima_altura = altura
            heroe_mas_alto = personaje["nombre"]

    return heroe_mas_alto, maxima_altura

def filtrar_lista(procesadora, lista: list) -> list:
    """
    Filtra una lista de elementos usando una función procesadora.

    Args:
        procesadora (function): Una función que toma un elemento de la lista y retorna un valor booleano.
        lista (list): La lista de elementos a filtrar.

    Returns:
        list: Una nueva lista que contiene solo los elementos para los cuales la función procesadora retorna True.

    Raises:
        ValueError: Si la lista no es válida o está vacía.
    """
    validar_lista(lista)
    
    lista_retorno = []
    for el in lista:
        if procesadora(el):
            lista_retorno.append(el)
    return lista_retorno

def mapear_lista(procesadora, lista: list) -> list:
    """
    Aplica una función a cada elemento de una lista y retorna una nueva lista con los resultados.

    Args:
        procesadora (function): Una función que toma un elemento de la lista y retorna un nuevo valor.
        lista (list): La lista de elementos a procesar.

    Returns:
        list: Una nueva lista con los resultados de aplicar la función procesadora a cada elemento de la lista original.

    Raises:
        ValueError: Si la lista no es válida o está vacía.
    """
    validar_lista(lista)
    
    lista_retorno = []
    for el in lista:
        lista_retorno.append(procesadora(el))
    return lista_retorno

def promedio_altura(lista:list, campo:str):
    """
    Calcula el promedio de los valores en el campo especificado para una lista de diccionarios.

    Args:
        lista (list): La lista de diccionarios.
        campo (str): El campo cuyo promedio se desea calcular.

    Returns:
        float: El promedio de los valores en el campo especificado.

    Raises:
        ValueError: Si el campo no existe en los diccionarios de la lista.
    """
    
    validar_lista(lista)
    
    suma_total = 0
    tam = len(lista)
    if tam == 0:
        raise ValueError("No se puede dividir por 0")
    for i in lista:
        suma = float(i[campo])
        suma_total += suma
    retorno = suma_total / tam
    return retorno

#funciones menu

def pausar():
    """
    pausa
    """
    from os import system
    system ("pause")

def limpiar_pantalla():
    """limpia la pantalla de la consola
    """
    from os import system
    system ("cls")

# def validar_opcion_menu(opcion):
#     """
#     Valida la opcion ingresada por el usuario.

#     Args:
#         opcion (str): La opción ingresada por el usuario.

#     Returns:
#         bool: True si la opción es válida, False en caso contrario.
#     """
#     if opcion in ["1", "2", "3", "4", "5", "6", "7", "8"]:
#         return True
#     else:
#         print("Opción no válida. Por favor, elija una opción entre 1 y 8.")
#         return False

def menu():
    """
    Despliega el menu de la app STARK
    """
    print("Bienvenido a la APP de STARK")

    print("1. Muestra el nombre de todos los super heroes")
    print("2. Muestra el nombre y altura de todos los super heroes")
    print("3. Determina cual es el super heroe mas alto")
    print("4. Determina cual es el super heroe mas bajo")
    print("5. Muestra el promedio de altura de los super heroes")
    print("6. Muestra el super heroe mas alto y el mas bajo (se requiere 3 y 4)")
    print("7. Muestra el heroe menos pesado y el mas pesado")
    print("8. Recorre la lista e imprime por consola el nombre de cada superhéroe de género M")
    print("9. Recorre la lista e imprime por consola el nombre de cada superhéroe de género F")
    print("10. Recorrer la lista y determinar cuál es el superhéroe más alto de género M")
    print("11. Recorrer la lista y determinar cuál es el superhéroe más alto de género F")
    print("12. Recorrer la lista y determinar cuál es el superhéroe más bajo de género M")
    print("13. Recorrer la lista y determinar cuál es el superhéroe más bajo de género F")
    print("14. Recorrer la lista y determinar la altura promedio de los superhéroes de género M")
    print("15. Recorrer la lista y determinar la altura promedio de los superhéroes de género F")
    print("16. muestra cual es el Nombre del superhéroe asociado a cada uno de los indicadores anteriores (mas altos [m, f] y mas bajos [m, f])")
    print("17. Determinar cuántos superhéroes tienen cada tipo de color de ojos.")
    print("18. Determinar cuántos superhéroes tienen cada tipo de color de pelo.")
    print("19. Determinar cuántos superhéroes tienen cada tipo de inteligencia")
    print("20. Listar todos los superhéroes agrupados por color de ojos.")
    print("21. Listar todos los superhéroes agrupados por color de pelo.")
    print("22. Listar todos los superhéroes agrupados por tipo de inteligencia ")
    print("23. Salir")

    eleccion = input("Ingrese su eleccion: ")

    # while not validar_opcion_menu(eleccion):
    #     eleccion = input("Ingrese su eleccion: ")

    return eleccion

#validaciones

def validar_lista(lista):
    """
    Valida que el argumento sea una lista y que no esté vacía.

    Args:
        lista (list): La lista a validar.

    Raises:
        ValueError: Si el argumento no es una lista o está vacía.
    """
    if not isinstance(lista, list):
        raise ValueError("El argumento debe ser una lista.")
    if len(lista) == 0:
        raise ValueError("La lista no puede estar vacía.")