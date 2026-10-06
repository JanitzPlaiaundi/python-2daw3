
numero = int(input("Escribe tu numero: "))

def potencia(num ,cant):
    resultado = 0
    for i in range(cant):
        if  resultado == 0:
            resultado = num
        else:
            resultado = resultado * num

    return resultado

raiz_cuadrada = potencia(numero, 2)
raiz_cubica = potencia(numero, 3)

print("La raiz cuadrada es: " + str(raiz_cuadrada) + " y la raiz cubica es " + str(raiz_cubica))