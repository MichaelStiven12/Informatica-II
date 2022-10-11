#04-10-22

#Diccionarios y sus metodos

#Son elementos compuestos por clave: valor

diccionario = {
                "Michael Valencia": 3.0, 
                "Daniel Quintero": 4.0, 
                "Esteban Chavez": 5.0, 
                "Margarita Maria": 3.0
                }

#Acceder a un valor a traves de su clave

print(diccionario["Michael Valencia"])
print(diccionario["Daniel Quintero"])
print(diccionario.get("Juan David Gonzalez","no existe"))
try:
    print(diccionario ["Juan David Gonzalez"])
except:
    print("Esto es un error, el programa continua")


#Acceder a todas las claves 

print(diccionario.keys())

#Extraer todos los valores del diccionario 

print(diccionario.values())

#Ejercicio: Recorrer mediante un ciclo for todas las claves del diccionario

for i in diccionario.keys():
    print(i)

#Ejercicio: Recorrer mediante un ciclo for todos l0s valores del diccionario

for j in diccionario.values():
    print(j)

#Ejercicio: Imprimir todas las parejas clave: valor del diccionario utilizando un ciclo for

for i in diccionario.keys():
    print(i + "-" + str(j))


for pareja in diccionario.items():
    print(pareja[0] + "-" + str(pareja[1]))

for i,j in diccionario.items(): #Desempaquetado
    print(i + "-" + str(j))


#Como cambiar los elementos del diccionario

diccionario["Michael Valencia"] = 5.0
print(diccionario)

#Ejercicio: Cambiar todos los valores del diccionario a 5.0

for i in diccionario:
    diccionario[i] = 0.0

print(diccionario)

#Ejercicio: Cambiar los valores del diccionario de la siguiente manera: Si es hombre 0.0, si es mujer 5.0

for i in diccionario.keys():
    if i[-1] == "a":
        diccionario[i] = 5.0
    else:
        diccionario[i] = 0.0

print(diccionario)


#Haga ina copia de diccionario y cambie las calificaciones a 5.0

diccionariocopia = diccionario.copy()

for i in diccionariocopia.keys():
    diccionariocopia[i] = 5.0

print(diccionario)
print(diccionariocopia)


#Como eliminar un par clave: valor del diccionario

del diccionario["Esteban Chavez"]

print(diccionario)


#Ejercicio: Con lo visto anteriormente cambie la clave Margarita Maria a Maragarita Rosa

valor = diccionario["Margarita Maria"]
del diccionario["Margarita Maria"]
diccionario["Margarita Rosa"] = valor
print(diccionario)


""" 
                               Materias
    Nombre          Cuantica Etica Deportes Lenguas
Juan Gutierrez        2.0     5.0     1.3     3.2
Maria Snowden         3.1     4.9     2.2     1.1
Pedro Gonzalez        5.0     3.8     3.1     4.1
Angelica Lozano       2.1     2.7     4.1     3.2
Pablo Iglesias        3.2     1.6     5.0     1.2
Mariana Pajon         2.2     2.5     4.9     3.3
Esteban Loaiza        2.1     3.4     3.8     4.3
Daniela Pineda        5.0     4.3     2.7     1.2
Esteban Vazco         3.1     5.0     1.6     3.2
Enilse Lopez          5.0     2.2     2.5     5.0
Cristian Playonero    0.5     1.1     3.4     3.2
 
"""

nombres = {
            "Juan Gutierrez": {"Cuantica": 2.0, "Etica": 5.0, "Deportes": 1.3, "Lenguas": 3.2},      
            "Maria Snowden": {"Cuantica": 3.1, "Etica": 4.9, "Deportes": 2.2, "Lenguas": 1.1},
            "Pedro Gonzalez": {"Cuantica": 5.0, "Etica": 3.8, "Deportes": 3.1, "Lenguas": 4.1},
            "Angelica Lozano": {"Cuantica": 2.1, "Etica": 2.7, "Deportes": 4.1, "Lenguas": 3.2},
            "Pablo Iglesias": {"Cuantica": 3.2, "Etica": 1.6, "Deportes": 5.0, "Lenguas": 1.2},
            "Mariana Pajon": {"Cuantica": 2.2, "Etica": 2.5, "Deportes": 4.9, "Lenguas": 3.3},
            "Esteban Loaiza": {"Cuantica": 2.1, "Etica": 3.4, "Deportes": 3.8, "Lenguas": 4.3},
            "Daniela Pineda": {"Cuantica": 5.0, "Etica": 4.3, "Deportes": 2.7, "Lenguas": 1.2},
            "Esteban Vazco": {"Cuantica": 3.1, "Etica": 5.0, "Deportes": 1.6, "Lenguas": 3.2},
            "Enilse Lopez": {"Cuantica": 5.0, "Etica": 2.2, "Deportes": 2.5, "Lenguas": 5.0},
            "Cristian Playonero": {"Cuantica": 0.5, "Etica": 1.1, "Deportes": 3.4, "Lenguas": 3.2}
 }

     
print(nombres["Angelica Lozano"]["Deportes"])


data = [
["Juan Gutierrez",    2.0,     5.0,     1.3,     3.2],
["Maria Snowden",    3.1,     4.9,     2.2,     1.1],
["Pedro Gonzalez",    5.0,     3.8,     3.1,     4.1],
["Angelica Lozano",    2.1,     2.7,     4.1,     3.2],
["Pablo Iglesias",    3.2,     1.6,     5.0,     1.2],
["Mariana Pajon",    2.2,     2.5,     4.9,     3.3],
["Esteban Loaiza",    2.1,     3.4,     3.8,     4.3],
["Daniela Pineda",    5.0,     4.3,     2.7,     1.2],
["Esteban Vazco",    3.1,     5.0,     1.6,     3.2],
["Enilse Lopez",    5.0,     2.2,     2.5,     5.0],
["Cristian Playonero",    0.5,     1.1,     3.4,     3.2]
]

diccionarioCalificaciones = {}
for estudiante in data:
    diccionarioCalificaciones[estudiante[0]] = {"Cuantica": estudiante[1], "Etica": estudiante[2], 
                                                "Deportes": estudiante[3], "Lenguas": estudiante[4]}

print(diccionarioCalificaciones)


'''
Calcular el promedio de las calificaciones de cada estudiante usando diccionarioCalificaciones, determinar los 3 estudiantes
con mejor y peor promedio, calcular el promedio de las cuatro materias
'''
promedios = []
for estudiante in diccionarioCalificaciones:
    valores = diccionarioCalificaciones[estudiante].values()
    promedio = round((sum(valores))/4,2)
    promedios.append(promedio)

print(promedios)

diccionarioPromedios = {}
for estudiante in diccionarioCalificaciones.keys():
    diccionarioPromedios[estudiante] = promedios.index(estudiante)

print(diccionarioPromedios)

mejor = []
peor = []
for promedio in promedios:
    if promedios.index(promedio) <= 2:
        m = max(promedios)
        p = min(promedios)
        mejor.append(m)
        peor.append(p)
        promedios.pop(promedios.index(m))
        promedios.pop(promedios.index(p))

print(mejor, peor)

cuantica = []
etica = []
deportes = []
lenguas = []
for estudiante in diccionarioCalificaciones.values():
    cuantica.append(estudiante["Cuantica"])
    etica.append(estudiante["Etica"])
    deportes.append(estudiante["Deportes"])
    lenguas.append(estudiante["Lenguas"])
    promcuantica = round(sum(cuantica)/11,2)
    prometica = round(sum(etica)/11,2)
    promdeportes = round(sum(deportes)/11,2)
    promlenguas = round(sum(lenguas)/11,2)







