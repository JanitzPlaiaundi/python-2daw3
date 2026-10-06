sueldo_base = float(input("Indica el sueldo base del vendedor: "))
comision_venta1 = float(input("Dinero de la venta 1: ")) * 0.1
comision_venta2 = float(input("Dinero de la venta 2: ")) * 0.1
comision_venta3 = float(input("Dinero de la venta 3: ")) * 0.1

total_sueldo = sueldo_base + comision_venta1 + comision_venta2 + comision_venta3

print("Sueldo total = " + str(round(total_sueldo,2)))