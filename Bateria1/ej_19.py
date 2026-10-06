puntos_correctas = 5
puntos_incorrectas = 1

res_correctas = int(input("Cuantas respuestas correctas tiene: "))
res_incorrectas =  int(input("Cuantas respuestas incorrectas tiene: "))
res_blanco = int(input("Cuantas respuestas en blanco tiene: "))

sumaDeTodo = 0

for i in range(res_correctas):
    sumaDeTodo += puntos_correctas
for i in range(res_incorrectas):
    sumaDeTodo -= puntos_incorrectas

puntos_maximos = (res_correctas + res_incorrectas + res_blanco) * puntos_correctas
resutado = sumaDeTodo / puntos_maximos * 10

print("El resultado es: " + str(resutado))