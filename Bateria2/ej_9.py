numeros = []
numeros.append(int(input("Escribe el primer numero: ")))
numeros.append(int(input("Escribe el segundo numero: ")))
numeros.append(int(input("Escribe el tercer numero: ")))

numeros.sort()

for numero in numeros:
    print(str(numero), end=" ")

print()