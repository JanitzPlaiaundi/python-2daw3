cateto_1 = float(input("Escribe el primer cateto: "))
cateto_2 = float(input("Escribe el segundo cateto: "))

hipotenusa = (cateto_1**2 + cateto_2**2)**0.5

print("La hipotenusa es " + str(round(hipotenusa,2) ))