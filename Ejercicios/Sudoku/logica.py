'''
En este módulo contiene las funciones lógicas del juego

*obtenerTableroLogico() => Retorna tablero lógico lista

*actualizaTableroLogico(tableroLogico, posicion, caracter) => Retorna tablero logico actualizado lista

*revisarFilasYColumnas() => Retorna una posible '''


def obtenerTableroLogico():
    tableroLogico = [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]
    return tableroLogico

def actualizarTableroLogico(tableroLogico, posicion, numero):
    tableroLogico[posicion] = numero
    return tableroLogico
'''
def revisarFilasYColumnas(tableroLogico):
    for numero in tableroLogico:
        if tableroLogico[0] != tableroLogico[1] != tableroLogico[2] != tableroLogico[4]: 
'''