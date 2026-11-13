#carrito version 2

from srcV2.pizzas2 import Pizza, buscarPizza
from srcV2.bebidas2 import Bebida, buscarBebida
from srcV2.excepciones2 import ProductoNoEncontradoError, leerCantidad
from srcV2.calculos2 import calculadora


#busca el producto (pizza o bebida) aunque lo escribas en minusculas
#si no lo encuentra lanza ProductoNoEncontradoError
def buscarProducto(texto):
    pizza = buscarPizza(texto)
    if pizza is not None:
        return pizza
    bebida = buscarBebida(texto)
    if bebida is not None:
        return bebida
    raise ProductoNoEncontradoError(texto)


#devuelve True si el producto es una pizza
def esPizza(producto):
    return isinstance(producto, Pizza)


#devuelve True si el producto es una bebida
def esBebida(producto):
    return isinstance(producto, Bebida)


class LineaCarrito:
    #una linea del carrito: un producto y cuantas unidades hay de el
    def __init__(self, producto, cantidad):
        self._producto = producto
        self.cantidad = cantidad

    @property
    def producto(self):
        return self._producto

    @property
    def cantidad(self):
        return self._cantidad

    #la cantidad siempre es un entero mayor que 0
    @cantidad.setter
    def cantidad(self, cantidad):
        self._cantidad = leerCantidad(cantidad)

    #precio de la linea: precio del producto x cantidad
    def subtotal(self, temporada):
        return self._producto.precio(temporada) * self._cantidad

    def __str__(self):
        return f"{self._producto.nombreTicket()} x{self._cantidad}"


class Carrito:
    #el carrito es una lista de objetos LineaCarrito (composicion)
    #cada linea guarda un producto (Pizza, Bebida o Menu) y su cantidad
    def __init__(self):
        self._lineas = []

    #las lineas del carrito (una copia, para que no se cambien desde fuera)
    @property
    def lineas(self):
        return list(self._lineas)

    #busca la linea de un producto, si no esta devuelve None
    def buscarLinea(self, producto):
        for linea in self._lineas:
            if linea.producto is producto:
                return linea
        return None

    #añade un producto (objeto) al carrito
    #si ya estaba, suma la cantidad a su linea en vez de crear otra
    def agregarProducto(self, producto, cantidad):
        cantidad = leerCantidad(cantidad)
        linea = self.buscarLinea(producto)
        if linea is None:
            self._lineas.append(LineaCarrito(producto, cantidad))
        else:
            linea.cantidad = linea.cantidad + cantidad
        print("Se ha añadido", cantidad, producto.nombre)
        return True

    #añade un producto por su nombre (lo que escribe el usuario)
    #si el producto no existe o la cantidad no es valida lanza una excepcion propia
    def agregar(self, texto, cantidad):
        cantidad = leerCantidad(cantidad)
        producto = buscarProducto(texto)
        return self.agregarProducto(producto, cantidad)

    #quita una unidad del producto del carrito
    #sirve para pizzas, bebidas y menus (se busca por el nombre)
    #si el producto no existe en la carta lanza ProductoNoEncontradoError
    def quitar(self, texto):
        nombre = texto.lower().strip()
        for linea in self._lineas:
            if linea.producto.nombre.lower() == nombre:
                if linea.cantidad > 1:
                    linea.cantidad = linea.cantidad - 1
                else:
                    self._lineas.remove(linea)
                print("Se ha quitado", linea.producto.nombre)
                return True

        #no esta en el carrito: comprobamos si al menos existe
        buscarProducto(texto)
        print("Ese producto no esta en el carrito")
        return False

    #deja el carrito vacio (por ejemplo despues de pagar)
    def vaciar(self):
        self._lineas = []

    def estaVacio(self):
        return len(self._lineas) == 0

    #todos los productos, uno por unidad (2 Margaritas = 2 elementos)
    @property
    def productos(self):
        lista = []
        for linea in self._lineas:
            lista = lista + [linea.producto] * linea.cantidad
        return lista

    #las pizzas sueltas que hay en el carrito (las de los menus no cuentan)
    def pizzas(self):
        return [producto for producto in self.productos if esPizza(producto)]

    #las bebidas sueltas que hay en el carrito
    def bebidas(self):
        return [producto for producto in self.productos if esBebida(producto)]

    #cuantas unidades hay de cada producto
    def contarProductos(self):
        return {linea.producto: linea.cantidad for linea in self._lineas}

    #suma el precio de todo el carrito (sin ofertas)
    def total(self, temporada):
        total = 0
        for linea in self._lineas:
            total = total + linea.subtotal(temporada)
        return round(total, 2)

    #base imponible e iva del total del carrito (sin ofertas)
    def baseImponible(self, temporada):
        return calculadora.separarIva(self.total(temporada))[0]

    def iva(self, temporada):
        return calculadora.separarIva(self.total(temporada))[1]

    #muestra las lineas con su precio y el total
    def mostrar(self, temporada):
        print("")
        print("--- CARRITO ---")
        if self.estaVacio():
            print("El carrito esta vacio")
            return

        for linea in self._lineas:
            print(f"{linea.producto.nombreTicket()} x {linea.cantidad} - {linea.subtotal(temporada):.2f} €")
        print(f"Total sin ofertas: {self.total(temporada):.2f} €")

    #len(carrito) da el numero de productos (unidades)
    def __len__(self):
        return sum(linea.cantidad for linea in self._lineas)
