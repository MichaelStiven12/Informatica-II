import logica
import interfaz

interfaz.explicacionJuego()
tablero  = logica.obtenerTableroLogico()
condicion = False
while condicion != True:
    posicion = int(input("Ingrese una posicion: "))
    numero = int(input("Ingrese un número: "))
    logica.actualizarTableroLogico(tablero, posicion, numero)
    revisar = logica.revisarFilasYColumnas(tablero)
    interfaz.dibujarTablero(tablero)
    if revisar == [True, True, True]:
        break





