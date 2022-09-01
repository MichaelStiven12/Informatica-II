#Realice un código, que permita la conversión de millas a km y km a millas

v = int(input("Sí desea convertir de km a millas ingrese un 1, si desea vonvertir de millas a km ingrese 2: "))
v1 = int(input("Ingrese el valor que desea convertir: "))
if v == 1:
    kam = v1/1.609
    print("Su valor en millas es: ", kam)
else:
    mak = v1*1.609
    print("Su valor en kilometros es: ", mak)


