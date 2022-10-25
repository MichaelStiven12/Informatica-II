def jugadores():
    global j1
    global j2
    j1 = input("Ingrese el nombre del jugador 1 (O): ")
    j2 = input("Ingrese el nombre del jugador 2 (X): ")
    return j1, j2
    
def inicio():
    inicio = " El primero en acertar tres en linea gana "
    print(inicio.center(50, "="))

def separacion():
    separado = " El juego continua "
    print(separado.center(50,"="))

def turno1():
    global t1
    global p1
    print("Es el turno del jugador " + j1 + ":")
    t1 = "O"
    p1 = input("Introduzca una posicion: ")
    return t1, p1

def errorTurno1():
    p1_1 = input("Esta posición ya está ocupada, por favor ingrese otra: ")
    return p1_1
    
def turno2():
    global t2
    global p2
    print("Es el turno del jugador " + j2 + ":")
    t2 = "X"
    p2 = input("Introduzca una posicion: ")
    return t2, p2
    
def errorTurno2():
    p2_1 = input("Esta posición ya está ocupada, por favor ingrese otra: ")
    return p2_1

def tablero():
    global visual
    a = " "
    visual = [" "," "," ","|"," "," "," ","|"," "," "," ","\n",
              " "," "," ","|"," "," "," ","|"," "," "," ","\n",
              " "," "," ","|"," "," "," ","|"," "," "," ","\n",
              "-","-","-","|","-","-","-","|","-","-","-","\n",
              " "," "," ","|"," "," "," ","|"," "," "," ","\n",
              " "," "," ","|"," "," "," ","|"," "," "," ","\n",
              " "," "," ","|"," "," "," ","|"," "," "," ","\n",
              "-","-","-","|","-","-","-","|","-","-","-","\n",
              " "," "," ","|"," "," "," ","|"," "," "," ","\n",
              " "," "," ","|"," "," "," ","|"," "," "," ","\n",
              " "," "," ","|"," "," "," ","|"," "," "," ","\n",
            ]
    for i in visual:
        print(i, end = "")
    return a

def jugada1(posiciont):
    visual1 = [" "," "," ","|"," "," "," ","|"," "," "," ","\n",
               " ","1"," ","|"," ","2"," ","|"," ","3"," ","\n",
               " "," "," ","|"," "," "," ","|"," "," "," ","\n",
               "-","-","-","|","-","-","-","|","-","-","-","\n",
               " "," "," ","|"," "," "," ","|"," "," "," ","\n",
               " ","4"," ","|"," ","5"," ","|"," ","6"," ","\n",
               " "," "," ","|"," "," "," ","|"," "," "," ","\n",
               "-","-","-","|","-","-","-","|","-","-","-","\n",
               " "," "," ","|"," "," "," ","|"," "," "," ","\n",
               " ","7"," ","|"," ","8"," ","|"," ","9"," ","\n",
               " "," "," ","|"," "," "," ","|"," "," "," ","\n",
            ]
    for i in range(1,10):
        if (int(posiciont) == i): 
            visual.pop(visual1.index(str(i)))
            visual.insert(visual1.index(str(i)),t1)
    for i in visual:
        print(i, end = "")

    return visual1

def jugada2(posiciont):
    visual2 = [" "," "," ","|"," "," "," ","|"," "," "," ","\n",
               " ","1"," ","|"," ","2"," ","|"," ","3"," ","\n",
               " "," "," ","|"," "," "," ","|"," "," "," ","\n",
               "-","-","-","|","-","-","-","|","-","-","-","\n",
               " "," "," ","|"," "," "," ","|"," "," "," ","\n",
               " ","4"," ","|"," ","5"," ","|"," ","6"," ","\n",
               " "," "," ","|"," "," "," ","|"," "," "," ","\n",
               "-","-","-","|","-","-","-","|","-","-","-","\n",
               " "," "," ","|"," "," "," ","|"," "," "," ","\n",
               " ","7"," ","|"," ","8"," ","|"," ","9"," ","\n",
               " "," "," ","|"," "," "," ","|"," "," "," ","\n",
            ]
    for i in range(1,10):
        if (int(posiciont) == i):
            visual.pop(visual2.index(str(i)))
            visual.insert(visual2.index(str(i)),t2)
    for i in visual:
        print(i, end = "")
    return visual2