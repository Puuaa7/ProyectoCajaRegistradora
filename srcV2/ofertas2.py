#ofertas version 2: jerarquia de ofertas

from abc import ABC, abstractmethod

from srcV2.temporada import Temporada


class Oferta(ABC):
    #clase base (abstracta) de todas las ofertas
    #cada oferta es una subclase que sobrescribe calcular() a su manera (polimorfismo):
    #la lista de ofertas se recorre sin saber de que tipo es cada una
    def __init__(self, nombre):
        self._nombre = nombre

    @property
    def nombre(self):
        return self._nombre

    #dinero que descuenta la oferta
    #descuentosPrevios es la lista de (nombre, importe) de las ofertas que van antes
    @abstractmethod
    def calcular(self, carrito, temporada, dia, descuentosPrevios):
        pass

    #texto que sale en "Ver ofertas"
    @abstractmethod
    def descripcion(self):
        pass

    #devuelve True si la oferta descuenta algo en este pedido
    def esAplicable(self, carrito, temporada, dia, descuentosPrevios=()):
        return self.calcular(carrito, temporada, dia, descuentosPrevios) > 0


class Oferta2x1(Oferta):
    #2x1 en algunas pizzas: se pueden mezclar y la mas barata de cada pareja sale gratis
    def __init__(self, pizzas=("Margarita", "Prosciutto", "Hawaiana")):
        super().__init__("2x1")
        self._pizzas = list(pizzas)

    @property
    def pizzas(self):
        return list(self._pizzas)

    #precios de las pizzas del carrito que entran en el 2x1, de mas barata a mas cara
    def preciosEnOferta(self, carrito, temporada):
        precios = [pizza.precio(temporada) for pizza in carrito.pizzas() if pizza.nombre in self._pizzas]
        precios.sort()
        return precios

    #cuantas pizzas salen gratis (la mitad, las mas baratas)
    def pizzasGratis(self, carrito, temporada):
        return len(self.preciosEnOferta(carrito, temporada)) // 2

    def calcular(self, carrito, temporada, dia, descuentosPrevios=()):
        precios = self.preciosEnOferta(carrito, temporada)
        return round(sum(precios[:len(precios) // 2]), 2)

    def descripcion(self):
        return "2x1 en " + ", ".join(self._pizzas)


class OfertaMenu(Oferta):
    #menu pizza + bebida: descuento por cada pizza que va con una bebida
    #las pizzas gratis del 2x1 no cuentan, por eso necesita la oferta 2x1
    def __init__(self, oferta2x1, descuentoPorMenu=1):
        super().__init__("Menu pizza + bebida")
        self._oferta2x1 = oferta2x1
        self._descuentoPorMenu = descuentoPorMenu

    def calcular(self, carrito, temporada, dia, descuentosPrevios=()):
        numPizzas = len(carrito.pizzas()) - self._oferta2x1.pizzasGratis(carrito, temporada)
        menus = min(numPizzas, len(carrito.bebidas()))
        return menus * self._descuentoPorMenu

    def descripcion(self):
        return f"Menu pizza + bebida: {self._descuentoPorMenu} euro de descuento"


class OfertaDiaSemana(Oferta):
    #un dia de la semana, descuento en las pizzas (sin contar las gratis del 2x1)
    def __init__(self, oferta2x1, dia="martes", porcentaje=0.20):
        super().__init__(f"{dia.capitalize()} {round(porcentaje * 100)}% pizzas")
        self._oferta2x1 = oferta2x1
        self._dia = dia
        self._porcentaje = porcentaje

    def calcular(self, carrito, temporada, dia, descuentosPrevios=()):
        if dia != self._dia:
            return 0
        totalPizzas = sum(pizza.precio(temporada) for pizza in carrito.pizzas())
        totalPizzas = totalPizzas - self._oferta2x1.calcular(carrito, temporada, dia)
        return round(totalPizzas * self._porcentaje, 2)

    def descripcion(self):
        return f"Los {self._dia} {round(self._porcentaje * 100)}% de descuento en pizzas"


class OfertaTemporada(Oferta):
    #en una temporada concreta, descuento en las bebidas
    #(en temporada baja se venden menos pizzas, asi animamos a pedir bebida)
    def __init__(self, temporada="baja", porcentaje=0.10):
        super().__init__(f"Temporada {temporada} {round(porcentaje * 100)}% bebidas")
        self._temporada = temporada
        self._porcentaje = porcentaje

    def calcular(self, carrito, temporada, dia, descuentosPrevios=()):
        #la temporada puede llegar como objeto Temporada o como su nombre
        if isinstance(temporada, Temporada):
            temporada = temporada.nombre
        if temporada != self._temporada:
            return 0
        totalBebidas = sum(bebida.precio(temporada) for bebida in carrito.bebidas())
        return round(totalBebidas * self._porcentaje, 2)

    def descripcion(self):
        return f"En temporada {self._temporada}, {round(self._porcentaje * 100)}% de descuento en bebidas"


class OfertaPedidoGrande(Oferta):
    #si el pedido pasa de un minimo (despues de las otras ofertas), descuento en el total
    def __init__(self, minimo=30, porcentaje=0.10):
        super().__init__(f"Mas de {minimo} euros {round(porcentaje * 100)}%")
        self._minimo = minimo
        self._porcentaje = porcentaje

    def calcular(self, carrito, temporada, dia, descuentosPrevios=()):
        total = carrito.total(temporada)
        for nombre, importe in descuentosPrevios:
            total = total - importe
        if total > self._minimo:
            return round(total * self._porcentaje, 2)
        return 0

    def descripcion(self):
        return f"Si el pedido pasa de {self._minimo} euros, {round(self._porcentaje * 100)}% de descuento"


#las ofertas de la pizzeria, en el orden en que se aplican
def crearOfertasPizzeria():
    oferta2x1 = Oferta2x1()
    return [oferta2x1,
            OfertaMenu(oferta2x1),
            OfertaDiaSemana(oferta2x1),
            OfertaTemporada(),
            OfertaPedidoGrande()]


class Ofertas:
    #lista de objetos Oferta que se aplican a un pedido
    def __init__(self, lista=None):
        if lista is None:
            lista = crearOfertasPizzeria()
        self._lista = list(lista)

    @property
    def lista(self):
        return list(self._lista)

    #aplica todas las ofertas en orden y devuelve una lista con los descuentos
    #cada descuento es una tupla (nombre de la oferta, dinero)
    def aplicar(self, carrito, temporada, dia):
        descuentos = []
        for oferta in self._lista:
            importe = oferta.calcular(carrito, temporada, dia, descuentos)
            if importe > 0:
                descuentos.append((oferta.nombre, importe))
        return descuentos

    #muestra los descuentos que tiene el carrito y el total con ofertas
    def mostrarDescuentos(self, carrito, temporada, dia):
        if carrito.estaVacio():
            return

        total = carrito.total(temporada)
        descuentos = self.aplicar(carrito, temporada, dia)

        if len(descuentos) == 0:
            print("No hay ofertas para este pedido")
        else:
            print("Descuentos:")
            for nombre, importe in descuentos:
                print(f"- {nombre}: -{importe:.2f} €")
                total = total - importe

        print(f"Total con ofertas: {total:.2f} €")

    #muestra la lista de ofertas de la pizzeria
    def mostrarDisponibles(self):
        print("")
        print("--- OFERTAS ---")
        for oferta in self._lista:
            print("- " + oferta.descripcion())


#ofertas que usa el resto del programa (por ejemplo el ticket)
ofertas = Ofertas()
