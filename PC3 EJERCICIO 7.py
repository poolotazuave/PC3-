#EJERCICIO NUMERO 7 DE PC3
import random

def generar_numeros_aleatorios():
    numeros = [random.randint(0, 100) for _ in range(20)]
    return numeros

def mostrar_lista(lista):
    print("Lista de números:")
    for numero in lista:
        print(numero, end=' ')
    print()

def ordenar_y_mostrar(lista):
    lista_ordenada = sorted(lista)
    print("Lista ordenada:")
    for numero in lista_ordenada:
        print(numero, end=' ')
    print()
import generador_numeros

# Generar números aleatorios
numeros_aleatorios = generador_numeros.generar_numeros_aleatorios()

# Mostrar la lista obtenida
generador_numeros.mostrar_lista(numeros_aleatorios)

# Ordenar y mostrar la lista
generador_numeros.ordenar_y_mostrar(numeros_aleatorios)
