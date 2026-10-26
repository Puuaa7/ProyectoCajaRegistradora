#carrito de la compra
#es una lista con los nombres de los productos, por ejemplo ["Margarita", "cola"]

#importamos las pizzas y bebidas para buscar productos y precios
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


#devuelve True si el producto es una pizza
def esPizza(producto):
    if producto in pizzas:
        return True
    return False


#devuelve True si el producto es una bebida
def esBebida(producto):
    if producto in bebidas:
        return True
    return False


#precio de un producto (pizza calculada o bebida fija), 0 si no existe
def obtenerPrecioProducto(producto, temporada):
    if esPizza(producto):
        return calcularPrecioPizza(producto, temporada)
    elif esBebida(producto):
        return bebidas[producto]
    else:
        return 0


#añade un producto al carrito tantas veces como la cantidad
def agregarProductoCarrito(carrito, texto, cantidad):
    producto = buscarProducto(texto)

    if producto == "":
        print("Ese producto no existe")
    else:
        for i in range(cantidad):
            carrito.append(producto)
        print("Se ha añadido", cantidad, producto)


#quita una unidad del producto del carrito
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


#suma el precio de todo el carrito (sin ofertas)
def calcularTotalCarrito(carrito, temporada):
    total = 0
    for producto in carrito:
        total = total + obtenerPrecioProducto(producto, temporada)
    return round(total, 2)

#muestra los productos agrupados con su precio y el total
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
