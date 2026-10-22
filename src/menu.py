#menu de la caja registradora

from datetime import date

from src.temporada import temporadas
from src.pizzas import mostrarPizzas, mostrarDesglosePizza
from src.bebidas import mostrarBebidas
from src.carrito import agregarProductoCarrito, quitarProductoCarrito, mostrarCarrito, buscarProducto, esPizza
from src.ofertas import mostrarOfertasDisponibles, mostrarDescuentosCarrito
from src.ticket import mostrarTicket

diasSemana = ("lunes", "martes", "miercoles", "jueves", "viernes", "sabado", "domingo")


def mostrarMenu(temporada, dia):
    print("")
    print("----- PIZZERIA PYTHON -----")
    print("Temporada:", temporada, "- Dia:", dia)
    print("1. Ver pizzas")
    print("2. Ver bebidas")
    print("3. Ver ofertas")
    print("4. Añadir producto")
    print("5. Quitar producto")
    print("6. Ver carrito")
    print("7. Pagar y ver ticket")
    print("8. Ver como se calcula el precio de una pizza")
    print("9. Cambiar temporada")
    print("10. Cambiar dia")
    print("0. Salir")


def pedirTemporada():
    temporada = input("Temporada (baja, media o alta): ")
    while temporada not in temporadas:
        print("Esa temporada no existe")
        temporada = input("Temporada (baja, media o alta): ")
    return temporada


def pedirDia():
    dia = input("Que dia es hoy? ").lower() #lower sirve para mantener todo en minus.
    while dia not in diasSemana:
        print("Ese dia no existe")
        dia = input("Que dia es hoy? ").lower()
    return dia


def iniciarCaja():
    carrito = []
    temporada = pedirTemporada()
    #dia de hoy (weekday da 0 el lunes, 1 el martes...)
    dia = diasSemana[date.today().weekday()]

    while True:
        mostrarMenu(temporada, dia)
        opcion = input("Elige una opcion: ")

        if opcion == "1":
            mostrarPizzas(temporada)

        elif opcion == "2":
            mostrarBebidas()

        elif opcion == "3":
            mostrarOfertasDisponibles()
            if len(carrito) > 0:
                print("")
                print("Ofertas de tu pedido:")
                mostrarDescuentosCarrito(carrito, temporada, dia)

        elif opcion == "4":
            producto = input("Que quieres añadir? ")
            cantidad = input("Cuantas? ")
            if cantidad.isascii() and cantidad.isdigit():
                cantidad = int(cantidad)
                if cantidad > 0:
                    agregarProductoCarrito(carrito, producto, cantidad)
                else:
                    print("La cantidad debe ser mayor a 0.")
            else:
                print("Introduce un número entero, no se ha añadido nada")

        elif opcion == "5":
            producto = input("Que quieres quitar? ")
            quitarProductoCarrito(carrito, producto)

        elif opcion == "6":
            mostrarCarrito(carrito, temporada)
            mostrarDescuentosCarrito(carrito, temporada, dia)

        elif opcion == "7":
            total = mostrarTicket(carrito, temporada, dia)
            if total > 0:
                carrito = []

        elif opcion == "8":
            pizza = buscarProducto(input("Que pizza? "))
            if esPizza(pizza):
                mostrarDesglosePizza(pizza, temporada)
            else:
                print("Esa pizza no existe")

        elif opcion == "9":
            temporada = pedirTemporada()

        elif opcion == "10":
            dia = pedirDia()

        elif opcion == "0":
            print("Adios!")
            break

        else:
            print("Opcion incorrecta")
