""" El salario mensual de un empleado se calcula teniendo en cuenta el numero de seguros vendidos,
    en donde el precio de cada seguro es de $120000. 
    Para los primeros 20 seguros, la comisión es del 20%.
    Para los siguientes 100 seguros las comisión es del 30%.
    Para los siguientes seguros vendidos. La comisión es de 10%.
    a) Si un empleado vende 435 seguros, ¿cual será su salario?
    b) Para un salario de $10'000.000. ¿Cuántos seguros debe vender?
    c) Si un empleado devenga $15'000.000. ¿Cuantos salarios vendió en promedio al dia? 
       Teniendo en cuenta que solo trabajaba de lunes a jueves """

ps = 120000

a = 20*120000*0.2 + 100*120000*0.3 + (435 - 120)*120000*0.1
b = (10000000 - 20*120000*0.2 - 100*120000*0.3)/(120000*0.1)
c = ((15000000 - 20*120000*0.2 - 100*120000*0.3)/(120000*0.1))/18

print("El salario de un empleado que vende 435 seguros es de: ",int(a)," $")
print("Para que un empleado gane 10'000.000 $ debe vender ",int(b)," seguros")
print("Para que un empleado gane 15'000.000 $ debe vender un promedio de ",int(c)," seguros al día")