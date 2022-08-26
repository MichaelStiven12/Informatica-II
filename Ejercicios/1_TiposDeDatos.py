# Crear variables y asignarles los siguientes tipos de datos:
# Enteros: 1, 2, 3, 999
# Luego reste sucesivamente del ultimo al primero y almacenelo en una variable llamada resultado.

a1=1
b1=2
c1=3
d1=999

resultado=d1-c1-b1-a1

print("Resultado1 = ", resultado)

# Flotantes: 15.2, 29.5, 18.28
# Luego divida sucesivamente del primero al ultimo y almacenelo en una variable llamada resultado2.

a2=15.2
b2=29.5
c2=18.28

e2=a2/b2
resultado2=e2/c2

print("Resultado2 = ", resultado2)

# Strings: "123", "Michael"
# Luego sume ambas variables y determine si la operación es posible, si asi es almacenelo en 
# una variable de su elección.

a3="123"
b3="Michael"

c3=a3+ " " +b3

print("La suma de las cadenas es: ",c3)

########## Para pensar ############

# Busque una manera de convertir :
# Entero a flotante
# Flotante a entero
# String a entero y flotante
# Número a string

a4=5

b4=float(a4)

print(b4)

a5="5.9"

b5=int(float(a5))
b6=float(a5)

print(b5)
print(b6)

a7=10

b7=str(a7)

print(b7)

###################################