#Ejemplo

def saludarEstudiante(nombre): #Definición de la función, si no se pone un return, devuelve un None
    saludo = "Hola" + " " + nombre #Esto no es un return, simplemente es una impresión por pantalla
    return saludo #Esto si es un return, y se almacena en una variable

saludoRecibido = saludarEstudiante("Michael")
print(saludoRecibido)


'''
Desarrollar una función que reciba dos números y devuelva la suma de ambos
'''

def sumaNumeros(numero1,numero2):
    suma = numero1 + numero2
    return suma

numeros = sumaNumeros(5,3)
print(numeros)

'''
Desarrollar una función que reciba dos listas y devuelva una nueva lista, que sume elemento a elemento
'''

def sumaListas(lista1,lista2):
    listasSumadas = []
    for i in lista1:
        suma = i + lista2[lista1.index(i)]
        listasSumadas.append(suma)
    return listasSumadas

resultado = sumaListas([1,2,3,4],[5,6,7,8])
print(resultado)

'''
Desarrollar una función que no reciba parametros y que no retorne valores, peros sirva para imprimir un mensaje de 3 lineas
'''

def funcionVacia():
    print("Hola \nHola \nHola")
    return " "
vacio = funcionVacia()
print(vacio)

'''
Desarrollar una funcion, que reciba un diccionario de calificaciones (nombre - calificacion) y retorne el promedio
'''
notas = {
                "Michael Valencia": 3.0, 
                "Daniel Quintero": 4.0, 
                "Esteban Chavez": 5.0, 
                "Margarita Maria": 3.0
                }

def promedios(diccionario):
    for calificacion in diccionario:
        promedio = (sum(diccionario.values()))/len(diccionario)
    return promedio

promedioDiccionario = promedios(notas)
print("El promedio del diccionario es: ", promedioDiccionario)

