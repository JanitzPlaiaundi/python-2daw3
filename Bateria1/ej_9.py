precio_total = 0
while True:
    producto = float(input("Precio del producto:"))
    precio_total += producto

    comprando = input("Quieres seguir comprando? y/n \n")

    if(comprando == "n"):
        break

precio_final = precio_total - precio_total*0.15

print("El precio final es " + str(round(precio_final,2)))