'''
Este modulo contiene las funciones necesarias para imprimir el juego de sudoku'''

def explicacionJuego():
    explicacion = '''
    =========================================
    Este es un juego de Sudoku 4x4

    Es un juego de un jugador, para ganar
    debes llenar el tablero de manera que 
    los numeros en cada fila y columna no se 
    repitan.

    Para ingresar la posicion te puedes guiar 
    del siguiente tablero.

     1  | 2  | 3  | 4     
    ----|----|----|----
     5  | 6  | 7  | 8  
    ----|----|----|----
     9  | 10 | 11 | 12  
    ----|----|----|----
     13 | 14 | 15 | 16       
                    
    =========================================
    '''
    print(explicacion)
    input("---Ingrese enter para iniciar el juego---")


def dibujarTablero(tableroLogico):
    tableroVisual = '''
      {}  | {}  | {}  | {}      
     ----|----|----|----
      {}  | {}  | {}  | {}   
     ----|----|----|----
      {}  | {}  | {}  | {}   
     ----|----|----|----
      {}  | {}  | {}  | {}     
    '''.format(tableroLogico[0],tableroLogico[1],tableroLogico[2],tableroLogico[3],
               tableroLogico[4],tableroLogico[5],tableroLogico[6],tableroLogico[7],
               tableroLogico[8],tableroLogico[9],tableroLogico[10],tableroLogico[11],
               tableroLogico[12],tableroLogico[13],tableroLogico[14],tableroLogico[15], 
                )
    tableroVisual = tableroVisual.replace("None"," ")
    print(tableroVisual)
    
