# 08 - 11 - 2022

'''
Crear una clase llamada ComidaColombiana
atributos: componente1, componente2, componente3
metodos: nutrir y provocar
'''

class ComidaColombiana:
    def __init__(self,ingrediente1, ingrediente2, ingrediente3):
        self.ingrediente1 = ingrediente1
        self.ingrediente2 = ingrediente2
        self.ingrediente3 = ingrediente3

    def provocar(self, opcion):
        if opcion in ["Huele bien", "Se ve bien", "Tengo hambre"]:
            return "Este alimento me provoca"
        else:
            return "Este alimento no me provoca"

    def nutrir(self, opcion):
        if opcion in ["Tengo nauseas", "Estoy enfermo", "El doctor me lo prohibio"]:
            return "Este alimento no me puede nutrir"
        else:
            return "Este alimento me puede nutrir"
        

#¿Como creo el objeto? (Instanciar)

bandejapaisa = ComidaColombiana("Arroz", "Chicharron", "Frijoles")
sancochoDeGallina = ComidaColombiana("Gallina", "Papa", "Caldo")
ajiacoSantafereño = ComidaColombiana("Pollo", "Papa", "Aguacate")

print("¿Es instancia? ==> ", isinstance(bandejapaisa, ComidaColombiana))

#¿Como accedo a los atributos de un objeto?

atributoA = bandejapaisa.ingrediente1
atributoB = sancochoDeGallina.ingrediente2
atributoC = ajiacoSantafereño.ingrediente1

print("Atributos ==> ", atributoA, atributoB, atributoC)


#¿Como acceder a los métodos de un objeto?

salida1 = bandejapaisa.provocar("tengo hambre")
salida2 = ajiacoSantafereño.nutrir("Muero de hambre")
salida3 = sancochoDeGallina.provocar("huele mal")
print("salidas =>", salida1, salida2, salida3, sep=" -- ")


"""
Ejercicio:
    1. Crear una clase llamada Profesores
        con los atributos: nombre, edad, salario
        con los metodos: enseñar, calificar
    2. Crear una clase llamada Decimal
       con un unico atributo: valorNumerico
       con los metodos convertirABinario, conventirAOctal, convertirAHexadecimal,  
"""

