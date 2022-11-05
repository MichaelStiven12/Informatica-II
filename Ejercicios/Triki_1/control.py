import interfaz
import logica

interfaz.explicarJuego()
tableroJuego = logica.obtenerTableroLogico()

for turno in ["X", "O", "X", "O", "X", "O", "X", "O", "X"]:
    print("\nTurno jugador ", turno)
    posicion = int(input("Ingrese posicion de juego: "))
    tableroJuego = logica.actualizarTableroLogico(tableroJuego, posicion, turno)
    interfaz.dibujarTablero(tableroJuego)
    posibleGanador = logica.determinarGanador(tableroJuego)
    if posibleGanador in ["X", "O"]:
        print("Felicidades ha ganado el juego jugador ", turno)
        break
    