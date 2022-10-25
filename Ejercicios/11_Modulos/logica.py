'''
Este módulo se llama lógica, mediante el cual se suman tres numeros, se suman n numeros y se suman dos listas elemento a elemento.'''


def sumaDeTresNumeros(numero1,numero2,numero3): #Entrada de la función
    suma = numero1 + numero2 + numero3
    return suma #Sálida de la función

def sumaDeNNumeros(*numero):
    #suman = 0
    #for i in numero:
    #    suman = suman + i
    suman = sum(numero) 
    return suman

def sumaDeDosListas(lista1,lista2): #Notación camel - case
    listasSumadas = []
    for i in range(0,len(lista1)):
        sumal = lista1[i] + lista2[i]
        listasSumadas.append(sumal)
    return listasSumadas

