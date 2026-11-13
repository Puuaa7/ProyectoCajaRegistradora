#CAJA REGISTRADORA PIZZERIA


#pregunta que version del programa quieres usar hasta que la respuesta sea valida
def elegirVersion():
    print("")
    print("----- CAJA REGISTRADORA PIZZERIA -----")
    print("1. Version 1 (funciones)")
    print("2. Version 2 (clases y objetos)")
    version = input("Que version quieres usar? ").strip()
    while version not in ("1", "2"):
        print("Escribe 1 o 2")
        version = input("Que version quieres usar? ").strip()
    return version


#punto de entrada del programa
def main():
    version = elegirVersion()

    #importamos solo la version elegida
    if version == "1":
        from srcV1.menu import iniciarCaja
    else:
        from srcV2.menu2 import iniciarCaja

    iniciarCaja()


#solo se ejecuta si se lanza este archivo directamente
if __name__ == "__main__":
    main()
