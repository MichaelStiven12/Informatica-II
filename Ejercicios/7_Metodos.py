#Buscar metodos que hagan las siguientes operaciones

from operator import invert


cadena = "sdlksdfjk"
#Retornar los caracteres en mayuscula
print(cadena.upper()) #estos metodos retornan otra cadena o entero, no cambian la original

#Retornar los caracteres en minuscula
print(cadena.lower())

#Retornar si el número de veces que se repote un caracter 
print(cadena.count("s"))

#Retornar si la cadena es alfabetica
print(cadena.isalpha())

#Retornar si la cadena es alfanumerica
print(cadena.isalnum())

#Retornar si la cadena contiene números
print(cadena.isnumeric())

#Reemplazar una letra por otra letra
print(cadena.replace("s","t"))

print(cadena)

'''
Las cadenas son inmutables, ningun metodo las puede alterar
por mucho puede generar otra cadena, pero no afecta la original
'''


#Indexacón de cadenas

cadena1 = "Mundo UnalA"
print(cadena1[0:len(cadena1):2]) #Se debe pensar en indices, no en posiciones

#Cadena al revés

print(cadena1[-1::-1])

# Elementos ubicados en las posiciones 3, 5 y 7

print(cadena1[2:8:3])

#Elementos hasta la mitad de la cadena

print(cadena1[0:(len(cadena1)//2)])

#Elementos hasta la mitad de adelante de la cadena

print(cadena1[len(cadena1)//2:len(cadena1)])

#Elementos de la mitad de la cadena hasta el primer elemento

print(cadena1[len(cadena1)//2::-1])