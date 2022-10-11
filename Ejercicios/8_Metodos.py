'''
cadena = "hola mundo cruel"

#Extrae el primer elemento
print(cadena[0])
print(cadena[-14])

#Extrae el ultimo elemento
print(cadena[13])
print(cadena[-1])

#Extrae elementos de la mitad
print(cadena[6]+cadena[7])


#Metodos de las listas 
'''
#Metodos inplace, no se imprime pero si realiza un cambio en la lista

lista = [1, "a", 2, 3, "b"]

lista.append(10)
print(lista)

lista.pop(4)
print(lista)

lista.insert(3,8)
print(lista)

d = lista[0:3:1]
print(d)

