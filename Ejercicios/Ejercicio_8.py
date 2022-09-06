'''Cuatro compañeros, contratan un taxi con el objeto de movilizarse juntos a la universidad. 
El contrato es de lunes a viernes, y deben pagar al taxista $15000 por cada trayecto. El servicio se
prestará solo de ida.
Sin embargo, los cuatro no se movilizan juntos todos los dias. Por tanto, han planteado que la tarifa
debe dividirse entre el numero de compañeros que se movilicen en cada trayecto.En caso, de que ninguno
utilice el servicio. Deben pagar al taxista una tarifa de $10000, repartidos equitativamente entre los cuatro.
A continueación veamos el uso del servicio por parte de los compañeros en la última semana de clases:
            LUNES   MARTES  MIERCOLES   JUEVES  VIERNES
JUAN          Si        Si        No        Si    No
CAMILA        Si        Si        No        No    No
JOSE          Si        No        Si        No    No
MARIA         Si        Si        Si        No    No      
¿Cuanto debe pagar cada estudiante?'''

juan = 15000/4 + 15000/3 + 15000 + 2500
camila = 15000/4 + 15000/3 + 2500
jose = 15000/4 + 15000/2 + 2500
maria = 15000/4 + 15000/3 + 15000/2 + 2500

print("Juan debe pagar ",int(juan),"$, Camila debe pagar ",int(camila),"$, Jose debe pagar ",int(jose),"$, y Maria debe pagar ",int(maria)," $")


