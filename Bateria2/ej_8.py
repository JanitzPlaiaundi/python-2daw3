nota = float(input("Escribe la nota: "))
edad = int(input("Escribe la edad: "))
sexo = input("Escribe el sexo M/F: ")

if nota >= 5 and edad >= 18:
    if  sexo == "F":
        print("ACEPTADA")
    elif sexo == "M":
        print("POSIBLE")
else:
    print("NO ACEPTADA")