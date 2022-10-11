""" El rendimiento deportivo de un grupo de atletas es el siguiente:
-------------- Deportista_1  Deportista_2  Deportista_3  Deportista_4  Deportista_5  Deportista_6  Deportista_7  Deportista_8  Deportista_9  Deportista_10  Deportista_11  Deportista_12  Deportista_13  Deportista_14  Deportista_15  Deportista_16  Deportista_17  Deportista_18  Deportista_19  Deportista_20  Deportista_21  Deportista_22  Deportista_23  Deportista_24  Deportista_25  Deportista_26  Deportista_27 
Rendimiento --    "A"           "B"           "C"            "B"            "B"           "B"          "C"           "B"             "A"           "C"          "B"          "A"             "C"             "B"          "B"              "B"           "B"             "A"           "B"            "A"           "A"             "C"             "B"             "B"          "B"            "B"            "C"             
Edad ---------     42            60            18             20             35            25           60            30              19            42           21           17              39              30           28               34            27              23            23             20            25             "40"             31             32            45             26             17             
Donde "A" es alto, "B" aceptable  y "C"  insuficiente. Determine:
  => ¿Cuántos atletas tienen un rendimiento alto, aceptable e insuficiente?
  => ¿Cuántos atletas mayores de 40 años, tienen rendimiento alto?
  => ¿Cuantos atletas menores de 25, tienen un rendimiento insuficiente?
  => ¿Cuales deportistas entre 30 y 40 años tienen rendimiento aceptable?
  => ¿Cuales deportistas menores de 30 tienen rendimiento alto
  => ¿Cuales deportistas mayores de 35 tienen rendimiento insuficiente?
(Intente utilizar un solo ciclo para resolver las preguntas) """

deportistas = {
                "Deportista_1 ": ["A", 42], 
                "Deportista_2 ": ["B", 60], 
                "Deportista_3 ": ["C", 18], 
                "Deportista_4 ": ["B", 20], 
                "Deportista_5 ": ["B", 35], 
                "Deportista_6 ": ["B", 25], 
                "Deportista_7 ": ["C", 60], 
                "Deportista_8 ": ["B", 30], 
                "Deportista_9 ": ["A", 19], 
                "Deportista_10": ["C", 42], 
                "Deportista_11": ["B", 21],  
                "Deportista_12": ["A", 17],  
                "Deportista_13": ["C", 39],  
                "Deportista_14": ["B", 30],  
                "Deportista_15": ["B", 28],  
                "Deportista_16": ["B", 34],  
                "Deportista_17": ["B", 27],  
                "Deportista_18": ["A", 23],  
                "Deportista_19": ["B", 23],  
                "Deportista_20": ["A", 20],  
                "Deportista_21": ["A", 25],  
                "Deportista_22": ["C", 40],  
                "Deportista_23": ["B", 31],  
                "Deportista_24": ["B", 32],  
                "Deportista_25": ["B", 45],  
                "Deportista_26": ["B", 26],  
                "Deportista_27": ["C", 17]
}

alto = []
aceptable = []
insuficiente = []
mayores40 = []
menores25 = []
alto30 = []
insuficiente35 = []
aceptable30_40 = []
for rendimiento in deportistas.values():
    if rendimiento[0] == "A":
        alto.append(rendimiento[0])
    elif rendimiento[0] == "B":
        aceptable.append(rendimiento[0])
    elif rendimiento[0] == "C":
        insuficiente.append(rendimiento[0])
    elif rendimiento[1] > 40 and rendimiento[0] == "A":
        mayores40.append(rendimiento[1])
    elif rendimiento[1] < 25 and rendimiento[0] == "C":
        menores25.append(rendimiento[0])
    
    
for rendimiento in deportistas.items():    
    if 30 <= rendimiento[1] <= 40 and rendimiento[0] == "B":
        aceptable30_40.append(deportistas.get(rendimiento))
        print("El deportista " + " está entre los 30 y 40 años y presenta un rendimiento aceptable. ")
    elif rendimiento[1] < 30 and rendimiento[0] == "A":
        alto30.append(deportistas.get(rendimiento))
        print("El deportista " + "  es menor de 30 años y presenta un rendimiento alto. ")
    elif rendimiento[1] > 35 and rendimiento[0] == "C":
        insuficiente35.append(deportistas.get(rendimiento))
        print("El deportista " + " es mayor de 35 años y presenta un rendimiento insuficiente. ")
    
print("De los 27 deportistas " + str(len(alto)) + " tienen alto rendimiento, " + str(len(aceptable)) + " tienen rendimiento aceptable y " + str(len(insuficiente)) + " tienen rendimiento insuficiente. ")
print("De los 27 deportistas " + str(len(mayores40)) + " son mayores de 40 años y tienen un rendimiento alto, mientras que " + str(len(menores25)) + " son menores de 25 y tienen un rendimiento insuficiente. ")

 
