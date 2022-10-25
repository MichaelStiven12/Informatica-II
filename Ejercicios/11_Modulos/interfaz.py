'''
Este módulo se llama interfaz, mediante el cual se imprime un separador,
un nombre y unas variables de manera mas presentable utilizando funciones.

También se almacena 1 variable.
'''

cantidadDeFunciones = 3

def separador(caracter):
    sep = caracter*50
    print(sep)

def imprimirNombre(nombre):
    saludo = "Hola, mi nombre es interfaz y el tuyo es " + nombre
    print(saludo)

def imprimirVariable(nombreVariable, variable):
    print(nombreVariable + " ==> " + str(variable))


