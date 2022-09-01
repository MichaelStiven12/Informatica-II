#Dadas las coordenadas P1(5,4,5) y P2(0,10,9).
#Realice un codigo que determine la distancia entre ambos puntos

p1 = [5,4,5]
p2 = [0,10,9]

d = (((p2[0]-p1[0])**2)+((p2[1]-p1[1])**2)+((p2[2]-p1[2])**2))**0.5

print(d)