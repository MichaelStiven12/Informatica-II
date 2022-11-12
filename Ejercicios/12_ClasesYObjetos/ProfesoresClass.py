#10 - 11 -
class Profesores:
    def __init__(self,nombre, edad, salario):
        self.nombre = nombre
        self.edad = edad
        self.salario = salario

    def enseñar(self, calidad):
        return "Estoy enseñando al {}% ".format(calidad)
            

    def calificar(self, estadoAnimo):
        if estadoAnimo == "Feliz":
            return "Su nota es 5.0"
        elif estadoAnimo == "Triste":
            return "Su nota es 0.0"

        
if __name__ == "__main__":
    profesor1 = Profesores("Elisabeth Restrepo", 20, 15000000)
    profesor2 = Profesores("Luis Mulcue", 50, 50000000)

    print(profesor1.nombre)
    print(profesor2.salario)
    print(profesor1.enseñar(20))
    print(profesor2.calificar("Triste"))