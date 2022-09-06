#Operadores de asignación

a=1
b=2
c=3

#Operadores aritméticos
#Realice las siguientes operaciones mentalmente

print(3 + 9,
    3.0 + 9,
    9 ** 0.5,
    2 ** 32,
    19 // 2,
    19 % 3,
    9/3,
    "Hola " + "mundo",
    "Hola " * 3,
    ["A"] + [1,2,3],
    [] + [],
    (1,2,3) + (1,))

#Operadores lógicos
#Realice las siguientes operaciones mentalmente

True and True
False and True
False and False
not True
not False
True or True
False or True

print(1 and 1)
print(0 and 1)
print(1 and 3)
print(1 and "hola") #Se puede utilizar como condicional, ej: si es verdadero imprime "hola"; Todos los strings se toman como verdadero
                    #excepto cuando se pone un string vacío ""
print(1 or 3)
print("Hola" or "Verdadero")
print("" or "Hola")
print("" or False)

#operadores de comparación
#Realizar las siguientes operaciones

print(1 > 2, 1 < 3, 1 == 1, 2 != 1, 3 >= 3, 5 <= 2) #Devuelve valores booleanos independientemente del tipo de variable
print(4 > True, True > False, [] > [1,2,3], "a" > "b") #No se pueden comparar cadenas con booleanos; En el caso de comparar srings
                                                       #funciona distinto, aquí compara el orden en el código ASCII

#Operadores de pertenencia
#Realizar las siguientes operaciones

print("a" in "abcdefg",
    "A" in "ABCDEFG",
    1 in [1, 2, 3],
    1 in ["1", "2", "3"],
    "hola" in "holamundo",
    "Hola" not in "holamundo")
