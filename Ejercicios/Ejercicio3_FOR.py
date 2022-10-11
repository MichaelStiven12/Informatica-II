""" El rendimiento de los empleados de una empresa es el siguiente:
--------------  Emplea_1  Emplea_2  Emplea_3  Emplea_4  Emplea_5  Emplea_6  Emplea_7  Emplea_8  Emplea_9  Emplea_10  Emplea_11  Emplea_12  Emplea_13  Emplea_14  Emplea_15  Emplea_16  Emplea_17  Emplea_18  Emplea_19  Emplea_20  Emplea_21  Emplea_22  Emplea_23  Emplea_24  Emplea_25  Emplea_26  Emplea_27 
Rendimiento --    "C"       "B"      "B"        "B"        "C"      "B"      "A"        "C"       "B"        "A"        "C"       "B"        "B"        "B"         "B"        "A"       "B"        "A"         "A"        "C"       "B"        "B"        "B"         "B"         "C"       "A"       "C"   
Donde "A" es alto, "B" aceptable  y "C"  insuficiente. 
Determine ¿cuales empleados pueden solicitar un aumento salarial y cuáles pueden ser despedidos? """

rendimiento = {
                "Emplea_1 ": "C",
                "Emplea_2 ": "B",
                "Emplea_3 ": "B",
                "Emplea_4 ": "B",
                "Emplea_5 ": "C",
                "Emplea_6 ": "B",
                "Emplea_7 ": "A",
                "Emplea_8 ": "C",
                "Emplea_9 ": "B",
                "Emplea_10": "A", 
                "Emplea_11": "C", 
                "Emplea_12": "B", 
                "Emplea_13": "B", 
                "Emplea_14": "B", 
                "Emplea_15": "B", 
                "Emplea_16": "A", 
                "Emplea_17": "B", 
                "Emplea_18": "A", 
                "Emplea_19": "A", 
                "Emplea_20": "C", 
                "Emplea_21": "B", 
                "Emplea_22": "B", 
                "Emplea_23": "B", 
                "Emplea_24": "B", 
                "Emplea_25": "C", 
                "Emplea_26": "A", 
                "Emplea_27": "C"
}

for valor in rendimiento.items():
    if valor[1] == "A":
        print("El empleado " + valor[0] + " recibirá un aumento")
    elif valor[1] == "C":
        print("El empleado " + valor[0] + " será despedido")
