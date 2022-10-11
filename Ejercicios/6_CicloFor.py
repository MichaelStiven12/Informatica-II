
#Recorrer los siguientes iterables:

cadena = "HolaMundoCruel"
lista = [1,2,30,100,50,-20]
tupla = (1,2,3,1,2,3,1,2,3)
rango = range(1,100)

for letra in cadena:
    print(letra, end = "--")

print("\n")

for numero in lista:
    print(numero, end = " ")

print("\n")

for numero in tupla:
    print(numero, end = " ")

print("\n")

for numero in rango:
    print(numero, end = " ")



'''
Recorrer un iterable con los números del 1 al 10 utilizando diferentes iterables
(por lo menos 4) sin necesidad de definirlos en una variable

#Forma 1
for i in range(1,11):
    print(i, end = " - ")

#Forma 2
for i in [1,2,3,4,5,6,7,8,9,10]:
    print(i, end = " - ")

#Forma 3
for i in (1,2,3,4,5,6,7,8,9,10):
    print(i, end = " - ")

#Forma 4
for i in "12345678910":
    print(i, end = " - ")
'''

'''
Imprimir los números del 1 al 20, solo los pares:

for i in range(0,21,2):
    print(i, end = " ")
'''

'''
Imprimir los números multiplos de 4 desde el 5 hasta el 30:
'''
'''
for i in range(8,30,4):
    print(i, end = "  ")

'''

