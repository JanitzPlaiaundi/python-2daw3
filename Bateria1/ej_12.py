x1 = int(input("Primera posicion x: "))
y1 = int(input("Primera posicion y: "))
x2 = int(input("Segunda posicion x: "))
y2 = int(input("Segunda posicion y: "))

v = ((x2 - x1), (y2 - y1))

dist = ((v[0] ** 2) + (v[1]**2))*0.5

print("La distancia es de: " + str(int(dist)))
