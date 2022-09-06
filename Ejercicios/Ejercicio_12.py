#Un proyectil es lanzado verticalmente hacia arriba, calcule la velocidad inicial que debe tener para 
#alcanzar una altura dada.

h = int(input("Ingrese una altura deseada en metros: "))

v_0 = (2*9.8*h)**0.5
print("La velocidad inicial del proyectil debe ser de ",round(v_0,2),"m/s")