euros = int(input("Cuantos euros tienes: "))
centimos = int(input("Cuantos centimos tienes: "))

monedas_2_euros = 0
monedas_1_euro = 0
monedas_50_centimos = 0
monedas_20_centimos = 0
monedas_10_centimos = 0
monedas_5_centimos = 0
monedas_2_centimos = 0
monedas_1_centimo = 0

cantidad_total_centimos = (euros * 100) + centimos

while True:
    if cantidad_total_centimos >= 200:
        monedas_2_euros += 1
        cantidad_total_centimos -= 200
    elif cantidad_total_centimos >= 100:
        monedas_1_euro += 1
        cantidad_total_centimos -= 100
    elif cantidad_total_centimos >= 50:
        monedas_50_centimos += 1
        cantidad_total_centimos -= 50
    elif cantidad_total_centimos >= 20:
        monedas_20_centimos += 1
        cantidad_total_centimos -= 20
    elif cantidad_total_centimos >= 10:
        monedas_10_centimos += 1
        cantidad_total_centimos -= 10
    elif cantidad_total_centimos >= 5:
        monedas_5_centimos += 1
        cantidad_total_centimos -= 5
    elif cantidad_total_centimos >= 2:
        monedas_2_centimos += 1
        cantidad_total_centimos -= 2
    elif cantidad_total_centimos == 1:
        monedas_1_centimo += 1
        cantidad_total_centimos -= 1
    else:
        print("Monedas de 2 euros: " + str(monedas_2_euros))
        print("Monedas de 1 euro: " + str(monedas_1_euro))
        print("Monedas de 50 centimos: " + str(monedas_50_centimos))
        print("Monedas de 20 centimos: " + str(monedas_20_centimos))
        print("Monedas de 10 centimos: " + str(monedas_10_centimos))
        print("Monedas de 5 centimos: " + str(monedas_5_centimos))
        print("Monedas de 2 centimos: " + str(monedas_2_centimos))
        print("Monedas de 1 centimo: " + str(monedas_1_centimo))
        break
    