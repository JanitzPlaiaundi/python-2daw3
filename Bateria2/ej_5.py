usuario_valido = "pepe"
contraseña_valida = "asdasd"

usuario_entrada = input("Escribe el usuario: ")
contraseña_entrada = input("Escribe la contraseña: ")

if usuario_entrada == usuario_valido and contraseña_entrada == contraseña_valida:
    print("Has entrado en el sistema")
else:
    print("Usuario o contraseña incorrectos")