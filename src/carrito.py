#carrito de la compra
#es una lista con los nombres de los productos, por ejemplo ["Margarita", "cola"]

from src.pizzas import pizzas, calcularPrecioPizza
from src.bebidas import bebidas


#busca el producto aunque lo escribas en minusculas
#si no lo encuentra devuelve ""
def buscarProducto(texto):
    texto = texto.lower().strip()

    for nombre in pizzas:
        if nombre.lower() == texto:
            return nombre

    for nombre in bebidas:
        if nombre.lower() == texto:
            return nombre

    return ""


def esPizza(producto):
    if producto in pizzas:
        return True
    return False


def esBebida(producto):
    if producto in bebidas:
        return True
    return False


def obtenerPrecioProducto(producto, temporada):
    if esPizza(producto):
        return calcularPrecioPizza(producto, temporada)
    elif esBebida(producto):
        return bebidas[producto]
    else:
        return 0


def agregarProductoCarrito(carrito, texto, cantidad):
    producto = buscarProducto(texto)

    if producto == "":
        print("Ese producto no existe")
    else:
        for i in range(cantidad):
            carrito.append(producto)
        print("Se ha añadido", cantidad, producto)


def quitarProductoCarrito(carrito, texto):
    producto = buscarProducto(texto)

    if producto in carrito:
        carrito.remove(producto)
        print("Se ha quitado", producto)
    else:
        print("Ese producto no esta en el carrito")


#cuenta cuantas veces esta cada producto en el carrito
def contarProductos(carrito):
    cantidades = {}
    for producto in carrito:
        if producto in cantidades:
            cantidades[producto] = cantidades[producto] + 1
        else:
            cantidades[producto] = 1
    return cantidades


def calcularTotalCarrito(carrito, temporada):
    total = 0
    for producto in carrito:
        total = total + obtenerPrecioProducto(producto, temporada)
    return round(total, 2)


def mostrarCarrito(carrito, temporada):
    print("")
    print("--- CARRITO ---")
    if len(carrito) == 0:
        print("El carrito esta vacio")
    else:
        cantidades = contarProductos(carrito)
        for producto in cantidades:
            precio = obtenerPrecioProducto(producto, temporada) * cantidades[producto]
            print(producto, "x", cantidades[producto], "-", round(precio, 2), "€")
        print("Total sin ofertas:", calcularTotalCarrito(carrito, temporada), "€")
