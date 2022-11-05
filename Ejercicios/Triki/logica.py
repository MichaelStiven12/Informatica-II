def accion(figura, posicion):
     global m
     m = [0,0,0,
          0,0,0,
          0,0,0]
     matriz_jugada = m.insert(int(posicion) - 1,figura)
     return m

def error():
     espacio = False
     for i in m:
          if i == "X" or i == "O":
               espacio = True
     return espacio

