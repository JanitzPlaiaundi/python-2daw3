paises = [
    ["España", "Madrid", 47],
    ["Francia", "París", 67],
    ["Alemania", "Berlín", 83],
    ["Italia", "Roma", 60],
    ["Portugal", "Lisboa", 10],
    ["Reino Unido", "Londres", 67],
    ["Rusia", "Moscú", 144],
    ["China", "Pekín", 1412],
    ["Estados Unidos", "Washington D.C.", 331],
    ["Brasil", "Brasilia", 213]
]

encabezado = f'{"País":20}{"Capital":20}{"Habitantes(mill.)":>20}'
separador = "-" * len(encabezado)

with open("Bateria7/paises.txt", "w", encoding="utf-8") as f:
    f.write(encabezado + "\n")
    f.write(separador + "\n")
    for pais, capital, habitantes in paises:
        f.write(f'{pais:20}{capital:20}{str(habitantes):>20}' + "\n")