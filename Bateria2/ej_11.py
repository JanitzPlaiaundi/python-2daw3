lado1 = int(input("Escribe la distancia del primer lado: "))
lado2 = int(input("Escribe la distancia del segundo lado: "))
lado3 = int(input("Escribe la distancia del tercer lado: "))

def comprobarPitagoras(hipotenusa, cateto1, cateto2):
    return hipotenusa **2 == (cateto1**2 + cateto2**2)
    
rectangulo = False
equilatero = False
if lado1 == lado2 == lado3:
    equilatero = True
elif lado1 > lado2:
    if lado1 > lado3:
        rectangulo = comprobarPitagoras(lado1, lado2, lado3)
    else:
        rectangulo = comprobarPitagoras(lado3, lado1, lado2)
elif lado2 > lado1:
    if lado2 > lado3:
        rectangulo = comprobarPitagoras(lado2, lado1, lado3)
    else:
        rectangulo = comprobarPitagoras(lado3, lado2, lado1)

if equilatero:
    print("Es un triangulo equilatero")
elif rectangulo:
    print("Es un triangulo rectangulo")
    if lado1 == lado2 or lado2 == lado3 or lado1 == lado3:
        print("Es un triangulo isosceles")
else:
    print("Es un triangulo escaleno")
    