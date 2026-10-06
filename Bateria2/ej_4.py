num1 = int(input("Escribe el primer numero: "))
num2 = int(input("Escribe el segundo numero: "))

if num2 == 0:
    print("No se puede dividir entre 0")
else:
    print("El resultado es " + str(num1/num2))