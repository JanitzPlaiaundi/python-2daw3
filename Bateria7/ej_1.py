tabla = [
    ["Pan", 1.10],
    ["Leche", 0.95],
    ["Huevos (docena)", 2.40],
    ["Arroz (1kg)", 1.85],
    ["Pasta (500g)", 1.20],
    ["Aceite (1L)", 5.50],
    ["Café (250g)", 3.80],
    ["Azúcar (1kg)", 1.60],
    ["Manzanas (kg)", 2.95],
    ["Pollo (kg)", 6.40]
]

encabezado = f'{"Articulo":<23}{"Sin IVA":7}   {"Con IVA":7}'
separador = "-" * len(encabezado)

with open("Bateria7/articulos.txt", "w", encoding="utf-8") as f:
    f.write(encabezado + "\n")
    f.write(separador + "\n")
    for nombre, precio in tabla:
        f.write(f'{nombre:<23}' + str(f'{precio:>7}') + "   " + str(f'{precio*1.21:>7.2f}') + "\n")