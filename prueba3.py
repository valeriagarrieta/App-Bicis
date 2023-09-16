
usuarios_registrados = []


prestamos = []


class Usuario:
    def __init__(self, username, password):
        self.username = username
        self.password = password


def registrar_usuario(username, password):
    nuevo_usuario = Usuario(username, password)
    usuarios_registrados.append(nuevo_usuario)
    print("Usuario registrado con éxito.")


def iniciar_sesion(username, password):
    for usuario in usuarios_registrados:
        if usuario.username == username and usuario.password == password:
            return True
    return False


def prestar_bicicleta(username, origen, destino):
    codigo_prestamo = len(prestamos) + 1
    prestamo = {
        "codigo_prestamo": codigo_prestamo,
        "username": username,
        "origen": origen,
        "destino": destino
    }
    prestamos.append(prestamo)
    print(f"¡Súper! El préstamo fue un éxito, disfruta tu bici. El código de prestamo es: {codigo_prestamo}")


while True:
    print("\nBienvenido a BiciApp")
    print("1. Registrarse")
    print("2. Iniciar sesión")
    print("3. Realizar préstamo de bici")
    print("4. Salir")
    
    opcion = input("Seleccione una opción: ")
    
    if opcion == "1":
        username = input("Ingrese un nombre de usuario: ")
        password = input("Ingrese una contraseña: ")
        registrar_usuario(username, password)
    elif opcion == "2":
        username = input("Ingrese su nombre de usuario: ")
        password = input("Ingrese su contraseña: ")
        if iniciar_sesion(username, password):
            print("Yeiii! Ya iniciaste sesión.")
        else:
            print("Nombre de usuario o contraseña incorrectos.")
    elif opcion == "3":
        if not usuarios_registrados:
            print("No estás registrado :( ).")
        else:
            if not iniciar_sesion(username, password):
                print("Debes iniciar sesión.")
            else:
                origen = input("Ingrese el origen de salida: ")
                destino = input("Ingrese su destino: ")
                prestar_bicicleta(username, origen, destino)
    elif opcion == "4":
        break
    else:
        print("Opción no válida. Porfi, selecciona una opción válida.")
