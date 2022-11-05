'''
Este modulo contiene las funciones logicas del juego

*obtenerTableroLogico() => Retorna tablero lógico lista

*actualizaTableroLogico(tableroLogico, posicion, caracter) => Retorna tablero logico actualizado lista

*determinarGanador(tableroLogico) => Retorna posible ganador "O", "X", None'''

def obtenerTableroLogico():
    tableroLogico = [None, None, None, None, None, None, None, None, None]
    return tableroLogico

def actualizarTableroLogico(tableroLogico, posicion, caracter):
    tableroLogico[posicion] = caracter
    return tableroLogico

def determinarGanador(tableroLogico):
    posicionesParaGanar = [ (0,1,2),
                            (3,4,5),
                            (6,7,8),
                            (0,3,6),
                            (1,4,7),
                            (2,5,8),
                            (0,4,8),
                            (2,4,6),
                            ]
    ganador = None
    for p1, p2, p3 in posicionesParaGanar:
        if (tableroLogico[p1] == tableroLogico[p2] == tableroLogico[p3]):
            if tableroLogico[p1] != None:
                ganador = tableroLogico[p1]
    return ganador

if __name__ == "__main__":
    tablero = obtenerTableroLogico()
    tableroNuevo = actualizarTableroLogico(tablero, 0, "X")
    ganador = determinarGanador(["X","X","X",None,None,None,None,None,None])
    print(ganador)
