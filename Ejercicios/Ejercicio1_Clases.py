class Automoviles:
    def __init__(self, color, personasSentadas, uso):
        self.color = color
        self.personasSentadas = personasSentadas
        self.uso = uso
    
    def acelerar(self, aceleracion, tiempo):
        velocidadAlcanzada = aceleracion*tiempo
        return velocidadAlcanzada

    def frenar(self, velocidad, aceleracion):
        tiempoDetencion = -(velocidad/aceleracion)
        return tiempoDetencion
    

ferrari_458 = Automoviles("Rojo", 2, "Deportivo")
mclaren_720s = Automoviles("Negro", 4, "Deportivo")
autolegal = Automoviles("Blanco", 20, "Publico")

colormclaren_720s = mclaren_720s.color
personasSentadasmclaren_720s = mclaren_720s.personasSentadas
usomclaren_720s = mclaren_720s.uso

print("Los atributos del objeto MCLAREN_720S son: {}, {}, {}".format(colormclaren_720s, personasSentadasmclaren_720s, usomclaren_720s))

personasSentadasmclaren_720s = 2

print("Los atributos del objeto MCLAREN_720S son: {}, {}, {}".format(colormclaren_720s, personasSentadasmclaren_720s, usomclaren_720s))

aceleracionFerrari_458 = ferrari_458.acelerar(10, 5)
print("La aceleracion alcanzada por el FERRARI_458 es {} m/s^2".format(aceleracionFerrari_458))

frenoAutolegal = autolegal.frenar(30, -4)
print("El tiempo de frenado del AUTOLEGAL es {} s".format(frenoAutolegal))
