#La calificación de informatica se encuentra en el intervalo [0,5] y se calcula tomando 4 notas,
#con porcentajes de 15%, 25%, 20% y 40%. Si un estudiante tiene las primeras 2 calificaciones definidas.
#Realice un algoritmo que calcule la nota necesaria de las dos últimas notas para pasar la materia.

nota_1 = int(input("Ingrese su primera nota: "))
nota_2 = int(input("Ingrese su segunda nota: "))

nota_p = nota_1*0.15 + nota_2*0.25  

nota_f1 = (1.8 - nota_p)/0.2
