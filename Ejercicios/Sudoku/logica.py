'''
En este módulo contiene las funciones lógicas del juego

*obtenerTableroLogico() => Retorna tablero lógico lista

*actualizaTableroLogico(tableroLogico, posicion, caracter) => Retorna tablero logico actualizado lista

*revisarFilasYColumnas() => Retorna una posible jugada'''


def obtenerTableroLogico():
    tableroLogico = [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]
    return tableroLogico

def actualizarTableroLogico(tableroLogico, posicion, numero):
    tableroLogico[posicion] = numero
    return tableroLogico

def revisarFilasYColumnas(tableroLogico):
    fila = []
    columna = []
    region = []
    for numero in [0,4,8,12]:
        if tableroLogico[numero] != tableroLogico[numero + 1] != tableroLogico[numero + 2] != tableroLogico[numero + 3]:
            fila.append(numero)
    for numero in [0,1,2,3]:
        if tableroLogico[numero] != tableroLogico[numero + 4] != tableroLogico[numero + 8] != tableroLogico[numero + 12]:
            columna.append(numero)
    for numero in [0,2,8,10]:
        if tableroLogico[numero] != tableroLogico[numero + 1] != tableroLogico[numero + 4] != tableroLogico[numero + 5]:
            region.append(numero)
    return [len(fila), len(columna), len(region)]

