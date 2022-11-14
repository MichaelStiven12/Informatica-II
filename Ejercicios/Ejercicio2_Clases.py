class Estudiante:
    def __init__(self, codigo, nombre, edad, c1, c2, c3, c4):
        self.codigo = codigo
        self.nombre = nombre
        self.edad = edad
        self.calificaciones = [c1, c2, c3, c4]
    
    def promedio(self, c1, c2, c3, c4):
        promedioEstudiante = sum(self.calificaciones)/4
        return promedioEstudiante


class Curso:
    def __init__(self, nombreDeLaMateria, nombreDelProfesor, listadoDeEstudiantes):
        self.nombreDeLaMateria = nombreDeLaMateria
        self.nombreDelProfesor = nombreDelProfesor
        self.listadoDeEstudiantes = list(listadoDeEstudiantes)
    
    def agregarEstudiantes(self, estudiante):
        self.listadoDeEstudiantes.append(estudiante)
        return self.listadoDeEstudiantes

    def eliminarEstudiante(self, estudianteEliminado):
        self.listadoDeEstudiantes.pop(estudianteEliminado)
        return self.listadoDeEstudiantes
     
    def estudiantesAprovados(self, codigo, nombre, edad, c1, c2, c3, c4):
        estudiante = Estudiante(codigo, nombre, edad, c1, c2, c3, c4)
        if estudiante.promedio(c1, c2, c3, c4) >= 3:
            return print("El estudiante {} pasa la materia.".format(nombre))
        else:
            return print("El estudiante {} no pasa la materia.".format(nombre))


estudiante = Estudiante(1019068, "Michael Stiven Valencia Mora", 21, 3.5, 4.0, 4.5, 4.0)
curso = Curso("Informatica II", "Cristian Pachon", ["Michael Stiven Valencia Mora", "Juan Esteban Salgado Salgado", "Laura Lucia Blandon Ruiz", "Carlos Alberto Lubo Mestanza"])

aprovado = curso.estudiantesAprovados(1019068, "Michael Stiven Valencia Mora", 21, 3.5, 4.0, 4.5, 4.0)

print(aprovado)