#menus version 2: productos que agrupan otros productos

from srcV2.producto2 import Producto
from srcV2.calculos2 import calculadora
from srcV2.excepciones2 import PrecioNoValidoError


class Menu(Producto):
    #Menu hereda de Producto y contiene otros productos (composicion)
    #cuesta lo mismo que sus productos por separado menos un descuento
    def __init__(self, nombre, productos, descuento):
        super().__init__(nombre)
        if descuento < 0:
            raise PrecioNoValidoError(descuento)
        self._productos = tuple(productos)
        self._descuento = descuento

    @property
    def productos(self):
        return self._productos

    @property
    def descuento(self):
        return self._descuento

    #lo que costarian los productos del menu comprados por separado
    def precioPorSeparado(self, temporada=None):
        return round(sum(producto.precio(temporada) for producto in self._productos), 2)

    #sobrescribe precio de Producto: por separado menos el descuento del menu
    def precio(self, temporada=None):
        return round(self.precioPorSeparado(temporada) - self._descuento, 2)

    #sobrescribe el metodo abstracto de Producto
    def precioSinIva(self, temporada=None):
        return self.precio(temporada) / (1 + calculadora.gastos.iva)

    #en el ticket sale el menu con lo que lleva dentro
    def nombreTicket(self):
        contenido = ", ".join(producto.nombreTicket() for producto in self._productos)
        return f"{self.nombre} ({contenido})"


#los dos tipos de menu de la pizzeria
DESCUENTO_MENU_PIZZA_BEBIDA = 1
DESCUENTO_MENU_FAMILIAR = 5


#menu de una pizza y una bebida: 1 euro menos
def crearMenuPizzaBebida(pizza, bebida):
    return Menu("Menu pizza + bebida", [pizza, bebida], DESCUENTO_MENU_PIZZA_BEBIDA)


#menu familiar de 2 pizzas y 2 bebidas: 5 euros menos
def crearMenuFamiliar(pizza1, pizza2, bebida1, bebida2):
    return Menu("Menu familiar", [pizza1, pizza2, bebida1, bebida2], DESCUENTO_MENU_FAMILIAR)


#muestra los menus que se pueden pedir
def mostrarMenus():
    print("")
    print("--- MENUS ---")
    print(f"1. Menu pizza + bebida: una pizza y una bebida con {DESCUENTO_MENU_PIZZA_BEBIDA} € de descuento")
    print(f"2. Menu familiar: 2 pizzas y 2 bebidas con {DESCUENTO_MENU_FAMILIAR} € de descuento")
