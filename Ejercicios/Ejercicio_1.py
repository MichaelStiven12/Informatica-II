# Dada una cantidad de segundos, realice un algoritmo que los convierta a unidades horas,minutos
#mostrando en pantalla en formato "horas:minutos"


s = int(input("Ingrese un tiempo en segundos: "))
h = s / 3600
m = (h)*60 - int(h)*60

print("El tiempo en horas es: ",int(h),":",int(m)) 
