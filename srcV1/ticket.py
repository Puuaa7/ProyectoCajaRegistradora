#ticket final

#funciones necesarias para montar el ticket
from src.carrito import contarProductos, obtenerPrecioProducto, esPizza, calcularTotalCarrito
from src.ofertas import aplicarOferta
from src.calculos import separarIva


#imprime el ticket con productos, descuentos e iva y devuelve el total pagado
def mostrarTicket(carrito, temporada, dia):
    if len(carrito) == 0:
        print("El carrito esta vacio")
        return 0

    print("")
    print("PIZZERIA PYTHON")
    print("")

    #productos
    print("Productos:")
    cantidades = contarProductos(carrito)
    for producto in cantidades:
        precio = obtenerPrecioProducto(producto, temporada) * cantidades[producto]
        if esPizza(producto):
            print(f"- Pizza {producto} x{cantidades[producto]}: {round(precio, 2)} €")
        else:
            print(f"- {producto} x{cantidades[producto]}: {round(precio, 2)} €")

    #descuentos
    total = calcularTotalCarrito(carrito, temporada)
    descuentos = aplicarOferta(carrito, temporada, dia)

    if len(descuentos) > 0:
        print("")
        print("Descuentos:")
        for descuento in descuentos:
            print(f"- {descuento[0]}: -{descuento[1]} €")
            total = total - descuento[1]

    #total final y su desglose de iva
    total = round(total, 2)
    base_imponible, importe_iva = separarIva(total)

    print("")
    print("Base imponible:", base_imponible, "€")
    print("IVA:", importe_iva, "€")
    print("Total:", total, "€")
    print("")
    print("Gracias por su compra.")

    return total
