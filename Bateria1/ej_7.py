minutos = int(input("Escribe los minutos: "))

horas = int(minutos/60)
minutos_sobrantes = minutos - horas * 60

if minutos_sobrantes == 0:
    print("La cantidad de minutos es equivalente a " + str(horas) + " horas")
else:
    print("La cantidad de minutos es equivalente a " + str(horas) + " horas y " + str(minutos_sobrantes) + " minutos")