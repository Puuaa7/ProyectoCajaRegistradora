#CARRITO DE COMPRA
#El carrito es una lista con los nombres de los productos, por ejemplo:
#carrito = ["Margarita", "Margarita", "cola"]

from PizzaAddLista import pizzas, calcularPrecioPizza
from bebidas import bebidas


#busca un producto sin importar mayusculas/minusculas y devuelve su nombre exacto
#si no existe devuelve None
def buscarProducto(texto):
    texto = texto.strip().lower()

    for nombre in pizzas:
        if nombre.lower() == texto:
            return nombre

    for nombre in bebidas:
        if nombre.lower() == texto:
            return nombre

    return None


def esPizza(producto):
    return producto in pizzas


def esBebida(producto):
    return producto in bebidas


#devuelve el precio de venta (con IVA) de cualquier producto
def obtenerPrecioProducto(producto, temporada):
    if esPizza(producto):
        return calcularPrecioPizza(producto, temporada)
    elif esBebida(producto):
        return bebidas[producto]
    else:
        return 0


#añade un producto (o varias unidades) al carrito
def agregarProductoCarrito(carrito, texto, cantidad=1):
    producto = buscarProducto(texto)

    if producto is None:
        print(f"El producto '{texto}' no está en la carta.")
        return False

    for i in range(cantidad):
        carrito.append(producto)

    print(f"Añadido al carrito: {cantidad} x {producto}")
    return True


#quita una unidad de un producto del carrito
def quitarProductoCarrito(carrito, texto):
    producto = buscarProducto(texto)

    if producto is None or producto not in carrito:
        print(f"'{texto}' no está en el carrito.")
        return False

    carrito.remove(producto)
    print(f"Quitado del carrito: 1 x {producto}")
    return True


#agrupa el carrito en un diccionario {producto: cantidad}
def contarProductos(carrito):
    cantidades = {}
    for producto in carrito:
        if producto in cantidades:
            cantidades[producto] = cantidades[producto] + 1
        else:
            cantidades[producto] = 1
    return cantidades


#suma el precio de todos los productos del carrito (con IVA, sin ofertas)
def calcularTotalCarrito(carrito, temporada):
    total = 0
    for producto in carrito:
        total = total + obtenerPrecioProducto(producto, temporada)
    return round(total, 2)


#muestra lo que hay en el carrito en este momento
def mostrarCarrito(carrito, temporada):
    print()
    print("----- CARRITO -----")
    if len(carrito) == 0:
        print("El carrito está vacío.")
        return

    cantidades = contarProductos(carrito)
    for producto in cantidades:
        precio = obtenerPrecioProducto(producto, temporada)
        print(f"{cantidades[producto]} x {producto:<20}{precio * cantidades[producto]:>7.2f} €")
    print(f"Subtotal (sin ofertas):  {calcularTotalCarrito(carrito, temporada):>7.2f} €")