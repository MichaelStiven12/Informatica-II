#La calificación de informatica se encuentra en el intervalo [0,5] y se calcula tomando 4 notas, 
#con porcentajes de 15%, 25%, 20% y 40%. Si un estudiante tiene las primeras 3 calificaciones definidas.
#Realice un algoritmo que calcule la nota necesaria de la última nota para pasar la materia.

nota_1 = int(input("Ingrese su primera nota: "))
nota_2 = int(input("Ingrese su segunda nota: "))
nota_3 = int(input("Ingrese su tercera nota: "))

nota_p = nota_1*0.15 + nota_2*0.25 + nota_3*0.2
nota_f = (3.0 - nota_p)/0.4

print("Usted necesita un ", nota_f, "para pasar la materia en 3.0")
