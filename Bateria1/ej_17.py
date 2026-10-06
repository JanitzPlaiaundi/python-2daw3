hora = int(input("Hora de salida: "))
minuto = int(input("Minuto de salida: "))
segundo = int(input("Segundo de salida: "))
tiempo_segundos = int(input("Tiempo que tarda en segundos: "))

minutos_añadir = 0
total_segundos = tiempo_segundos + segundo
segundos_final = 0


if total_segundos >= 60:
    minutos_añadir = int((total_segundos)/60)
    
    segundos_final = total_segundos - minutos_añadir * 60
else:
    segundos_final = total_segundos

total_minutos = minuto + minutos_añadir
horas_añadir = 0
minutos_final = 0

if total_minutos >= 60:
    horas_añadir = int((total_minutos)/60)
    minutos_final = total_minutos - horas_añadir * 60
else:
    minutos_final = total_minutos

horas_final = hora + horas_añadir

print(str(horas_final) + ":" + str(minutos_final) + ":" + str(segundos_final))
