dia = int(input("Escribe el dia: "))
mes = int(input("Escribe el mes: "))
año = int(input("Escribe el año: "))

esBisiesto = False

if(año % 4 == 0 and año % 100 != 0) or año % 400 == 0:
    esBisiesto = True
else:
    esBisiesto = False

dias_maximos = 0

if mes < 1 or mes > 12:
    print("La fecha es incorrecta")
else:
    if mes in [1, 3, 5, 7, 8, 10, 12]:
        dias_maximos = 31
    elif mes in [4, 6, 9, 11]:
        dias_maximos = 30
    elif mes == 2:
        dias_maximos = 29 if esBisiesto else 28


    if dia < 1 or dia > dias_maximos:
        print("La fecha es incorrecta")
    else:
        print("La fecha es correcta")