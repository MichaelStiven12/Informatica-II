#Funciones de entrada/salida
'''
a = input("Ingrese su nombre: ") #Interrumpir la ejecución del código hasta que se almacene un valor
print("Su nombre es: ",a)

#Solicite la edad y muestre por pantalla si es o no mayor de edad

edad = int(input("Ingrese su edad: "))
print((edad >= 18 and "Usted es mayor de edad") or "Usted es menor de edad")

#Solicite una clave y muestre por pantalla si es correcta o incorrecta. (Clave ==> 9876)

clave = int(input("Ingrese la clave: "))
print((clave == 9876 and "La clave es correcta") or "La clave es incorrecta")
'''
#Funcion format
'''
numero = 192.5693
formato_cientifico = format(numero, "e")
print(formato_cientifico)

formato_cientifico1 = format(numero, ".2e")
print(formato_cientifico1)

numero1 = 12.95637  #Aproxima de manera correcta
formato_flotante = format(numero1, ".2f")
print(formato_flotante)

formato_flotante = format(numero1, ".0f")
print(formato_flotante)

'''
'''
#Ejercicio

numero1 = 0.52941

print(format(numero1, ".0f"))
print(format(numero1, ".2f"))
print(format(numero1, ".5f"))
print(format(numero1, ".1e"))
print(format(numero1, ".2e"))

numero2 = 2.389

print(format(numero2, ".0f"))
print(format(numero2, ".2f"))
print(format(numero2, ".5f"))
print(format(numero2, ".1e"))
print(format(numero2, ".2e"))

cadena = "hola mundo"
formato_centrado = format(cadena, "^50")
formato_derecha = format(cadena, ">50")
formato_izquierda = format(cadena, "<50")

print("formato centrado: \n", formato_centrado)
print("formato derecha: \n", formato_derecha)
print("formato izquierda: \n", formato_izquierda)

'''
'''
#Funciones de conversión

#Convertir a binario, octal y hexadecimal

decimal = 9
conversion_binario = bin(decimal)
conversion_octal = oct(decimal)
conversion_hex = hex(decimal)

print(conversion_binario)
print(conversion_octal)
print(conversion_hex)

#¿Como hacer lo contrario?

bin, oct, hex = "1100110", "146", "0f66"

print("bin a decimal: ", int(bin,2))
print("octal a decimal: ", int(oct,8))
print("hexadecimal a decimal: ", int(hex,16))

#Funciones de ayuda (dir)

cadena = "holamundo"
lista = [1,2,3]
entero = 10

print("Funcionalidades para cadena \n", dir(cadena))
print("Funcionalidades para lista \n", dir(lista))
print("Funcionalidades para entero \n", dir(entero))
'''
'''
#Funciones para secuencias

secuencia = range(1,11,1) #El inicio se toma pero el final no, si no se pone el valor del salto se toma como 1
print(list(secuencia))

#Numeros del 20 al 29

secuencia1 = range(20,30)
print(list(secuencia1))

#Numeros del -10 al 10 con salto 2

secuencia2 = range(-10,11,2)
print(list(secuencia2))

#Numeros multiplos de 3 desde el -10 hasta el 5

secuencia3 = range(-9,5,3)
print(list(secuencia3))

#Numeros del 10 al 0

secuencia4 = range(10,-1,-1)
print(list(secuencia4))

#Numeros multiplos de 3 y 5 del 1 al 1000. Al réves

print(list(range(990,14,-15))) 
'''
'''
#Listas

secuencia5 = range(1,10000,3)
lista = [1,2,3,4,5,8,8,9]

print("Tamaño de secuencia: ", len(secuencia5))
print("Tamaño de lista: ", len(lista))


print("Minimo de secuencia: ", min(secuencia5))
print("Minimo de lista: ", min(lista))

print("Maximo de secuencia: ", max(secuencia5))
print("Maximo de lista: ", max(lista))

print("Revertir secuencia: ", list(reversed(secuencia5)))
print("Revertir lista: ", list(reversed(lista)))

#Repetir el ejercicio anterior usando reversed

'''

