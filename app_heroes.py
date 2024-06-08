#import´

from data_stark import lista_personajes
from funciones_heroes_stark00 import *
from funciones_heroes_stark01 import *

# #PROGRAMA

flag_mas_alto = False
flag_mas_bajo = False

flag_m_mayor_altura = False
flag_f_mayor_altura = False
flag_m_menor_altura = False
flag_f_menor_altura = False

while True:
    limpiar_pantalla()
    match menu():
        case "1":
            mostrar_un_elemento_dict(lista_personajes, "nombre")
        case "2":
            mostrar_dos_elementos_dict(lista_personajes, "nombre", "altura")
        case "3":
            heroe_mas_alto, mayor_altura = encontrar_mas_alto(lista_personajes)
            flag_mas_alto = True
            print("Dato cargado con exito!!")
        case "4":
            heroe_con_menor_altura, altura_mas_baja = encontrar_mas_bajo(lista_personajes)
            flag_mas_bajo = True
            print("Dato cargado con exito!!")
        case "5":
            promedio = promedio_altura(lista_personajes, "altura")
            print(round(promedio,2))
        case "6":
            if flag_mas_alto and flag_mas_bajo:
                print(f"""
El superhéroe con mayor altura es: {heroe_mas_alto} con {mayor_altura}
El superhéroe con menor altura es: {heroe_con_menor_altura} con {altura_mas_baja}""")
            else:
                print("Primero carga sus datos en las opciones '3' y '4'!!! ")
        case "7":
            heroe_mas_pesado = encontrar_mayor_por_campo(lista_personajes, "peso")
            heroe_menos_pesado = encontrar_menor_por_campo(lista_personajes,"peso")
            print(f"""
El heroe menos pesado: {heroe_menos_pesado["nombre"]} {heroe_menos_pesado["peso"]}
El heroe mas pesado: {heroe_mas_pesado["nombre"]} {heroe_mas_pesado["peso"]}""")
        case "8":
            print(mapear_lista(lambda nombre : nombre["nombre"], filtrar_lista(lambda heroe: heroe["genero"] == "M", lista_personajes)))
        case "9":
            print(mapear_lista(lambda nombre : nombre["nombre"], filtrar_lista(lambda heroe: heroe["genero"] == "F", lista_personajes)))
        case "10":
            flag_m_mayor_altura = True
            heroes_m_mayor = filtrar_lista(lambda heroe: heroe["genero"] == "M", lista_personajes)
            mayor_altura_m = encontrar_mayor_por_campo(heroes_m_mayor, "altura")
            print("Dato cargado con exito!!")
        case "11":
            flag_f_mayor_altura = True
            heroes_f_mayor = filtrar_lista(lambda heroe: heroe["genero"] == "F", lista_personajes)
            mayor_altura_f = encontrar_mayor_por_campo(heroes_f_mayor, "altura")
            print("Dato cargado con exito!!")
        case "12":
            flag_m_menor_altura = True
            heroes_m_menor = filtrar_lista(lambda heroe: heroe["genero"] == "M", lista_personajes)
            menor_altura_m = encontrar_menor_por_campo(heroes_m_menor, "altura")
            print("Dato cargado con exito!!")
        case "13":
            flag_f_menor_altura = True
            heroes_f_menor = filtrar_lista(lambda heroe: heroe["genero"] == "F", lista_personajes)
            menor_altura_f = encontrar_menor_por_campo(heroes_f_menor, "altura")
            print("Dato cargado con exito!!")
        case "14":
            heroes_m = filtrar_lista(lambda heroe: heroe["genero"] == "M", lista_personajes)
            print(promedio_altura(heroes_m, "altura"))
        case "15":
            heroes_f = filtrar_lista(lambda heroe: heroe["genero"] == "F", lista_personajes)
            print(promedio_altura(heroes_f, "altura"))
        case "16":
            if flag_f_menor_altura and flag_f_mayor_altura and flag_m_mayor_altura and flag_m_menor_altura:
                punto_c = (extraer_campos_diccionario(mayor_altura_m, "nombre", "altura"))
                punto_d = (extraer_campos_diccionario(mayor_altura_f, "nombre", "altura"))
                punto_e = (extraer_campos_diccionario(menor_altura_m, "nombre", "altura"))
                punto_f = (extraer_campos_diccionario(menor_altura_f, "nombre", "altura"))
                print(f""" 
El super heroe masculino de mayor altura es: {punto_c[0]} {punto_c[1]}
El super heroe femenino de mayor altura es: {punto_d[0]} {punto_d[1]}
El super heroe masculino de menor altura es: {punto_e[0]} {punto_e[1]}
El super heroe femenino de menor altura es: {punto_f[0]} {punto_f[1]}
                """)
            else:
                print("Primero carga los datos (10 - 13)")
        case "17":
            punto_j = (contador_lista(mapear_lista(lambda color_ojos: color_ojos ["color_ojos"], lista_personajes), "color_ojos"))
            print(punto_j)
        case "18":
            punto_k = (contador_lista(mapear_lista(lambda color_pelo: color_pelo ["color_pelo"], lista_personajes), "color_pelo"))
            print(punto_k)
        case "19":
            punto_l = (contador_lista(mapear_lista(lambda inteligencia: inteligencia ["inteligencia"] if inteligencia["inteligencia"] else "No Tiene", lista_personajes), "inteligencia"))
            print(punto_l)
        case "20":
            punto_m = agrupar(lista_personajes, "color_ojos", "nombre")
            print(punto_m)
        case "21":
            punto_n = agrupar(lista_personajes, "color_pelo", "nombre")
            print(punto_n)
        case "22":
            punto_o = (agrupar(lista_personajes, "inteligencia", "nombre"))
            print(punto_o)
        case "23":
            print("Gracias por usar nuestra APP, ADIOS!!!")
            break
        case _:
            print("Opcion no valida.")
    pausar()