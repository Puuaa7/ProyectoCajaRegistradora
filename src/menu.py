from src.pizzas import pizzas
from src.calculos import calcular_precio_venta


def mostrar_menu():
    nombres_pizzas = list(pizzas)
    temporada = "media"
    opcion = -1

    while opcion != 0:
        print("\n--- CAJA REGISTRADORA ---")
        print("1. Ver pizzas y precios")
        print("2. Cambiar temporada")
        print("0. Salir")

        respuesta = input("Elige una opcion: ")

        if respuesta.isdigit():
            opcion = int(respuesta)
        else:
            opcion = -1

        if opcion == 1:
            numero = 1
            for nombre in nombres_pizzas:
                print(numero, "-", nombre)
                numero = numero + 1

            respuesta_pizza = input("Numero de la pizza: ")

            if respuesta_pizza.isdigit():
                numero_pizza = int(respuesta_pizza)

                if numero_pizza >= 1 and numero_pizza <= len(nombres_pizzas):
                    nombre = nombres_pizzas[numero_pizza - 1]
                    resultado = calcular_precio_venta(nombre, temporada)

                    print("Pizza:", nombre)
                    print("Coste ingredientes:", resultado["coste_ingredientes"], "EUR")
                    print("Precio final:", resultado["precio_con_iva"], "EUR")
                else:
                    print("Pizza no valida")
            else:
                print("Introduce un numero")

        elif opcion == 2:
            nueva_temporada = input("Temporada (baja/media/alta): ")

            if nueva_temporada == "baja" or nueva_temporada == "media" or nueva_temporada == "alta":
                temporada = nueva_temporada
                print("Temporada:", temporada)
            else:
                print("Temporada no valida")

        elif opcion == 0:
            print("Hasta pronto")

        else:
            print("Opcion no valida")
