
'''
print("Ejercicio numeros del 1 al 100")
contador = 10
string_num = ""
while contador <= 100:
    string_num = string_num + str(contador) + " - "
    contador = contador + 1

print(string_num)
'''

'''
Mostrar los números del 200 al 100 utilizando el ciclo while

contador = 200
while contador >= 100:
    print(contador)
    contador = contador - 1
'''


'''
Mostrar los números del 200 al 100 utilizando el ciclo while sin saltos de linea

print("200 al 100 sin salto de línea:")
contador = 200
while contador >= 100:
    print(contador, end = " ") #El espacio es un simbolo o caracter
    contador = contador - 1
'''

'''
Mostrar los números del 200 al 100 utilizando el ciclo while pero ahora haga que el salto de línea se haga en cada multiplo de 10


print("200 al 100 con salto de línea en multiplos de 10:")

contador = 200
contador_1 = 0
while contador >= 100:
    if contador_1 < 10:        
        print(contador, end = " - ") #El espacio es un simbolo o caracter
        contador_1 = contador_1 + 1
    elif contador_1 == 10:
        contador_1 = 0
        print(contador, end = " \n ")    
    contador = contador - 1
'''

'''
Pida a un usuario que ingrese un números, en caso de así lo desee.
De los números calcule cual es el mayor de los ingresados.

Si el usuario no desea ingresar más números el ciclo debe terminar.

r = "si"
mayor = -9999999999999
while r == "si":
    r = input("¿Desea ingresar un numero?")
    if r == "si":
        numero = int(input("Ingrese el número: "))
        if numero > mayor:
            mayor = numero
    else:
        r = "no"

print("El numero mayor es: ",mayor)
'''

