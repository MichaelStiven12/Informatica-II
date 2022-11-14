import logica
import interfaz

interfaz.explicacionJuego()
tablero  = logica.obtenerTableroLogico()
condicion = False
while condicion != True:
    posicion = int(input("Ingrese una posicion: "))
    numero = int(input("Ingrese un número: "))
    logica.actualizarTableroLogico(tablero, posicion, numero)
    interfaz.dibujarTablero(tablero)
    if (None) not in tablero:
        break

revisar = logica.revisarFilasYColumnas(tablero)
if revisar == [4, 4, 4]:
    print("Ganó, el juego ha terminado")




