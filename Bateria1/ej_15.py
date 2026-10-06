a = int(input("Escribe un numero para la variable a: "))
b = int(input("Escribe un numero para la variable b: "))

c = a
a = b
b = c

print("Ahora la variable a es: " + str(a) + ", y la variable b es: " + str(b))