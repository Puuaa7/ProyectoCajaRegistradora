#carrito version 2

from srcV2.pizzas2 import Pizza, buscarPizza
from srcV2.bebidas2 import Bebida, buscarBebida


#busca el producto (pizza o bebida) aunque lo escribas en minusculas
#si no lo encuentra devuelve None
def buscarProducto(texto):
    pizza = buscarPizza(texto)
    if pizza is not None:
        return pizza
    return buscarBebida(texto)


#devuelve True si el producto es una pizza
def esPizza(producto):
    return isinstance(producto, Pizza)


#devuelve True si el producto es una bebida
def esBebida(producto):
    return isinstance(producto, Bebida)


class Carrito:
    #el carrito es una lista de productos (objetos Pizza o Bebida)
    def __init__(self):
        self.productos = []

    #añade un producto al carrito tantas veces como la cantidad
    def agregar(self, texto, cantidad):
        producto = buscarProducto(texto)

        if producto is None:
            print("Ese producto no existe")
            return False

        for i in range(cantidad):
            self.productos.append(producto)
        print("Se ha añadido", cantidad, producto.nombre)
        return True

    #quita una unidad del producto del carrito
    def quitar(self, texto):
        producto = buscarProducto(texto)

        if producto in self.productos:
            self.productos.remove(producto)
            print("Se ha quitado", producto.nombre)
            return True

        print("Ese producto no esta en el carrito")
        return False

    #deja el carrito vacio (por ejemplo despues de pagar)
    def vaciar(self):
        self.productos = []

    def estaVacio(self):
        return len(self.productos) == 0

    #las pizzas que hay en el carrito
    def pizzas(self):
        return [producto for producto in self.productos if esPizza(producto)]

    #las bebidas que hay en el carrito
    def bebidas(self):
        return [producto for producto in self.productos if esBebida(producto)]

    #cuenta cuantas veces esta cada producto en el carrito
    def contarProductos(self):
        cantidades = {}
        for producto in self.productos:
            if producto in cantidades:
                cantidades[producto] = cantidades[producto] + 1
            else:
                cantidades[producto] = 1
        return cantidades

    #suma el precio de todo el carrito (sin ofertas)
    def total(self, temporada):
        total = 0
        for producto in self.productos:
            total = total + producto.precio(temporada)
        return round(total, 2)

    #muestra los productos agrupados con su precio y el total
    def mostrar(self, temporada):
        print("")
        print("--- CARRITO ---")
        if self.estaVacio():
            print("El carrito esta vacio")
            return

        cantidades = self.contarProductos()
        for producto in cantidades:
            precio = producto.precio(temporada) * cantidades[producto]
            print(f"{producto.nombre} x {cantidades[producto]} - {precio:.2f} €")
        print(f"Total sin ofertas: {self.total(temporada):.2f} €")

    #len(carrito) da el numero de productos
    def __len__(self):
        return len(self.productos)
