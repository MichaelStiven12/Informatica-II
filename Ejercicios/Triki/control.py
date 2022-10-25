import interfaz
import logica

interfaz.jugadores()
print("\n")
interfaz.inicio()
print("\n")
interfaz.tablero()

for i in range(1,10):
    if i%2 != 0:
        interfaz.turno1()

        logica.accion(interfaz.t1,interfaz.p1)

        if logica.error() == True:
            
            interfaz.errorTurno1()

        interfaz.jugada1(interfaz.p1)

        interfaz.separacion()
    else:
        interfaz.turno2()

        logica.accion(interfaz.t2,interfaz.p2)

        if logica.error() == True:
            
            interfaz.errorTurno2()

        interfaz.jugada2(interfaz.p2)

        interfaz.separacion()

    







