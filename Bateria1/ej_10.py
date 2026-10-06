cal_parcial1 = float(input("Primera calificacion parcial: "))
cal_parcial2 = float(input("Segunda calificacion parcial: "))
cal_parcial3 = float(input("Tercera calificacion parcial: "))

cal_parcial = (cal_parcial1 + cal_parcial2 + cal_parcial3)/3

ex_final = float(input("Calificacion del examen final: "))
trabajo_final = float(input("Calificacion del trabajo final: "))

nota_final = (cal_parcial * 0.55 + ex_final * 0.3 + trabajo_final * 0.15)

print("La nota final es: " + str(nota_final))