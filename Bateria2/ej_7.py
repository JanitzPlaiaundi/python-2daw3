base = int(input("Escribe la base: "))
exponente = int(input("Escribe el exponente: "))

if exponente == 0:
    print("El resultado es 1")
elif exponente > 0:
    print(str(base**exponente))
else :
    print("Resultado: " + str(base ** exponente))