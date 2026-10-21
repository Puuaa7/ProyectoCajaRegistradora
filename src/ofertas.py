#ofertas de la pizzeria

from src.carrito import esPizza, esBebida, obtenerPrecioProducto, calcularTotalCarrito

#pizzas que tienen 2x1 (es un conjunto)
pizzas_2x1 = {"Margarita", "Prosciutto", "Hawaiana"}


#oferta 1: 2x1 en algunas pizzas
#se pueden mezclar (por ejemplo Margarita + Hawaiana), la mas barata sale gratis
def ofertaDosPorUno(carrito, temporada):
    precios = []
    for producto in carrito:
        if producto in pizzas_2x1:
            precios.append(obtenerPrecioProducto(producto, temporada))

    #ordenamos de mas barata a mas cara
    precios.sort()

    pizzasGratis = len(precios) // 2
    descuento = 0
    for i in range(pizzasGratis):
        descuento = descuento + precios[i]

    return round(descuento, 2), pizzasGratis


#oferta 2: menu pizza + bebida, 1 euro de descuento por cada menu
def ofertaMenu(carrito, pizzasGratis):
    numPizzas = 0
    numBebidas = 0

    for producto in carrito:
        if esPizza(producto):
            numPizzas = numPizzas + 1
        if esBebida(producto):
            numBebidas = numBebidas + 1

    #las pizzas gratis del 2x1 no cuentan
    numPizzas = numPizzas - pizzasGratis

    if numPizzas < numBebidas:
        menus = numPizzas
    else:
        menus = numBebidas

    return menus * 1


#oferta 3: los martes 20% de descuento en las pizzas
def ofertaMartes(carrito, temporada, dia, descuento2x1):
    if dia == "martes":
        totalPizzas = 0
        for producto in carrito:
            if esPizza(producto):
                totalPizzas = totalPizzas + obtenerPrecioProducto(producto, temporada)
        totalPizzas = totalPizzas - descuento2x1
        return round(totalPizzas * 0.20, 2)
    return 0


#oferta 4: si el pedido pasa de 30 euros, 10% de descuento
def ofertaMasDe30(total):
    if total > 30:
        return round(total * 0.10, 2)
    return 0


#aplica todas las ofertas y devuelve una lista con los descuentos
#cada descuento es una tupla (nombre de la oferta, dinero)
def aplicarOferta(carrito, temporada, dia):
    descuentos = []

    descuento2x1, pizzasGratis = ofertaDosPorUno(carrito, temporada)
    if descuento2x1 > 0:
        descuentos.append(("2x1", descuento2x1))

    descuentoMenu = ofertaMenu(carrito, pizzasGratis)
    if descuentoMenu > 0:
        descuentos.append(("Menu pizza + bebida", descuentoMenu))

    descuentoMartes = ofertaMartes(carrito, temporada, dia, descuento2x1)
    if descuentoMartes > 0:
        descuentos.append(("Martes 20% pizzas", descuentoMartes))

    #el total despues de las otras ofertas
    total = calcularTotalCarrito(carrito, temporada)
    for descuento in descuentos:
        total = total - descuento[1]

    descuento30 = ofertaMasDe30(total)
    if descuento30 > 0:
        descuentos.append(("Mas de 30 euros 10%", descuento30))

    return descuentos


#muestra los descuentos que tiene el carrito y el total con ofertas
def mostrarDescuentosCarrito(carrito, temporada, dia):
    if len(carrito) == 0:
        return

    total = calcularTotalCarrito(carrito, temporada)
    descuentos = aplicarOferta(carrito, temporada, dia)

    if len(descuentos) == 0:
        print("No hay ofertas para este pedido")
    else:
        print("Descuentos:")
        for descuento in descuentos:
            print(f"- {descuento[0]}: -{descuento[1]} €")
            total = total - descuento[1]

    print("Total con ofertas:", round(total, 2), "€")


def mostrarOfertasDisponibles():
    print("")
    print("--- OFERTAS ---")
    print("- 2x1 en Margarita, Prosciutto y Hawaiana")
    print("- Menu pizza + bebida: 1 euro de descuento")
    print("- Los martes 20% de descuento en pizzas")
    print("- Si el pedido pasa de 30 euros, 10% de descuento")
