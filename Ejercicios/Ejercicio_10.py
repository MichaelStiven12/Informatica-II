""" El salario de un empleado de una empresa se calcula, utilizando como base el 
salario minimo, más un apoyo del 10% en transporte, y uno de 5% por gastos varios.
Además se paga una comisión de acuerdo al numero de ventas de los siguientes productos:
           
            precio_unidad  comisión
* Zapatos:    $ 50 000        5%
* Tenis:      $ 70 000        4%  
* Camizas:    $ 40 000        6%
* Corbatas:   $ 25 000        7%
* Pantalon:   $ 35 000        5%
* Blusas:     $ 80 000        3%
* Vestidos:   $ 95 000        2%
* Medias:     $ 10 000        8%
a) Realice un algoritmo que calcule el salario del empleado teniendo en cuenta el numero de ventas realizadas 
b) Uno de los directivos, quiere que la comisión de cada uno de los productos no supere los $2000
   ¿Qué productos deben cambiar en su porcentaje de comision?
c) Otro directivo desea que la comisión de cada producto se fije en $1900, 
   ¿en cuanto se deben fijar las comisiones de los productos"""

z = int(input("Ingrese el número de zapatos vendidos: "))
t = int(input("Ingrese el número de pares de tenis vendidos: "))
c = int(input("Ingrese el número de camisas vendidas: "))
co = int(input("Ingrese el número de corbatas vendidas: "))
p = int(input("Ingrese el número de pantalones vendidos: "))
b = int(input("Ingrese el número de blusas vendidas: "))
v = int(input("Ingrese el número de vestidos vendidos: "))
m = int(input("Ingrese el número de pares de medias vendidos: "))

salario_base = 1117174*1.15

salario = salario_base + z*50000*0.05 + t*70000*0.04 + c*40000*0.06 + co*25000*0.07 + p*35000*0.05 + b*80000*0.03 + v*95000*0.02 + m*10000*0.08

print("Su salario es de: ",int(salario)," $")

print("Para que las comisiones de los productos no superen los 2000 $ los productos que deben cambiar su porcentaje de comisión son: ")
print((50000*0.05 <= 2000 and "Zapatos") or " ")
print((70000*0.04 <= 2000 and "Tenis") or " ") 
print((40000*0.06 <= 2000 and "Camizas") or " ")
print((25000*0.07 <= 2000 and "Corbatas") or " ")
print((3500*0.05 <= 2000 and "Pantalon") or " ")
print((80000*0.03 <= 2000 and "Blusas") or " ")
print((95000*0.02 <= 2000 and "Vestidos") or " ")
print((10000*0.08 <= 2000 and "Medias \n") or " ")


print("Para que las comisiones de los productos se fijen en 1900 $ las comisiones de los productos deben ser de: ")
print("Zapatos: ",1900/50000," %")
print("Tenis: ",1900/70000," %") 
print("Camizas: ",1900/40000," %")
print("Corbatas: ",1900/25000," %")
print("Pantalon: ",1900/35000," %")
print("Blusas: ",1900/80000," %") 
print("Vestidos: ",1900/95000," %")
print("Medias: ",1900/10000," %")

