v1_vel = int(input("Escribe la velocidad del vechiculo 1 en km/h: "))
v2_vel = int(input("Escribe la velocidad del vechiculo 2 en km/h: "))

while True:
    if(v1_vel < v2_vel):
        break
    v2_vel = int(input("La velocidad del segundo vehiculo debe de ser mayor que el del vehiculo 1, elige otra velocidad: "))


d = int(input("Distancia entre los dos vehiculos en km: "))

t = d/(v2_vel-v1_vel)*60

print("El tiempo que tardan es de " + str(t) + " minutos")