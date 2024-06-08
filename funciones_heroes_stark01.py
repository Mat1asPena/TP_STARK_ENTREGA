"""
Agregar al código elaborado para cumplir el desafío #00 los siguientes puntos,
utilizando un menú que permita acceder a cada uno de los puntos por separado.
-------------------------------------------------------------------------------
A. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de      8
género M
B. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de      9
género F
C. Recorrer la lista y determinar cuál es el superhéroe más alto de género M      10
D. Recorrer la lista y determinar cuál es el superhéroe más alto de género F      11
E. Recorrer la lista y determinar cuál es el superhéroe más bajo de género M      12
F. Recorrer la lista y determinar cuál es el superhéroe más bajo de género F      13
G. Recorrer la lista y determinar la altura promedio de los superhéroes de        14
género M
H. Recorrer la lista y determinar la altura promedio de los superhéroes de        15
género F
I. Informar cual es el Nombre del superhéroe asociado a cada uno de los           16
indicadores anteriores (ítems C a F)
J. Determinar cuántos superhéroes tienen cada tipo de color de ojos.              17
K. Determinar cuántos superhéroes tienen cada tipo de color de pelo.              18
L. Determinar cuántos superhéroes tienen cada tipo de inteligencia (En caso de    19
no tener, Inicializarlo con 'No Tiene').
M. Listar todos los superhéroes agrupados por color de ojos.                      20
N. Listar todos los superhéroes agrupados por color de pelo.                      21
O. Listar todos los superhéroes agrupados por tipo de inteligencia                22
"""

#import´s
from data_stark import *
from funciones_heroes_stark00 import *

def contador_lista(lista:list ,campo: str)-> dict:
    """
    Args:
        lista (list): lista a iterar/recorrer
        campo (str): campo que  se itera/recorre

    Returns:
        dict: Diccionario con la cantidad de datos que hay en un campo
    """
    validar_lista(lista)

    campo = {}

    for el in lista:
        campo[el] = 0

    for el in lista:
        for i in campo:
            if el == i:
                campo[el] += 1

    for i in campo:
        if i == "":
            i = "No tiene"

    return campo

def agrupar(lista, campo, campo_agrupar):
    """
    enlista todos los "campo_agrupar" por "campo"

    Args:
        lista (list): lista con un dict 
        campo (str): campo por el que se agrupa
        campo_agrupar (str): campo el cual se agrupa dentro de "campo"

    Returns:
        dict: agrupacion solicitada
    """
    
    campo_retorno = {}
    
    # Reemplazar valores vacíos con "No tiene"
    for heroe in lista:
        if heroe[campo] == "":
            heroe[campo] = "No tiene"
    
    for el in mapear_lista(lambda heroe: heroe[campo], lista):
        campo_retorno[el] = ""
    
    for i in lista:
        for j in campo_retorno.keys():
            if i[campo] == j:
                campo_retorno[j] += f" {i[campo_agrupar]},"
    
    return campo_retorno