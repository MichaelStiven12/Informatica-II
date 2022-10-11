""" Realice los siguientes programas:
      a) Programa que calcule los primeros 100 terminos de la serie de fibonacci
      b) Programa que determine todos los divisores de un numero n
      c) Programa que determine si un número n es primo
      d) Programa que sume los digitos de un numero cualquiera. Ejemplo: numero=> 8791, rta=> 25 
      e) Programa que sume los digitos pares de un numero cualquiera """

secuencia = [1,1]
for i in range(0,99):
    if i>=1:  
        fibonacci = secuencia[i] + secuencia[i-1]
        secuencia.append(fibonacci)

print(secuencia)


n = int(input("Introduzca un número: "))

for i in range(1,n+1):
    if n%i == 0:
        print(i)


n1 = int(input("Ingrese un número: "))

np = []
p = []
for i in range(2,n1):
    residuo = n1%i
    if residuo == 0:
        np.append(residuo)
    elif n1%1 == 0 and n1%n1 == 0:
        p.append(n1%1)
        p.append(n1%n1)

if len(np) != 0:
    print("El número " + str(n1) + " no es primo")
else:
    print("El número " + str(n1) + " es primo")


n2 = input("Ingrese un número: ")

lista = []

for i in n2:
    i = int(i)
    lista.append(i)

suma = sum(lista)

print("La suma de los digitos del número ingresado es: ", suma)

n3 = input("Ingrese un número: ")

lista1 = []

for i in n3:
    i = int(i)
    if i%2 == 0:
        lista1.append(i)

suma1 = sum(lista1)

print("La suma de los digitos del número ingresado es: ", suma1)