#ofertas version 2


class Ofertas:
    #las ofertas guardan sus numeros, asi es facil cambiarlos
    def __init__(self, pizzas2x1=("Margarita", "Prosciutto", "Hawaiana"), descuentoMenu=1,
                 diaDescuento="martes", porcentajeDia=0.20, minimoPedido=30, porcentajePedido=0.10):
        self.pizzas2x1 = list(pizzas2x1)
        self.descuentoMenu = descuentoMenu
        self.diaDescuento = diaDescuento
        self.porcentajeDia = porcentajeDia
        self.minimoPedido = minimoPedido
        self.porcentajePedido = porcentajePedido

    #oferta 1: 2x1 en algunas pizzas
    #se pueden mezclar (por ejemplo Margarita + Hawaiana), la mas barata sale gratis
    #devuelve el descuento y cuantas pizzas salen gratis
    def dosPorUno(self, carrito, temporada):
        precios = []
        for pizza in carrito.pizzas():
            if pizza.nombre in self.pizzas2x1:
                precios.append(pizza.precio(temporada))

        #ordenamos de mas barata a mas cara
        precios.sort()

        #la mitad de las pizzas salen gratis (las mas baratas)
        pizzasGratis = len(precios) // 2
        descuento = 0
        for i in range(pizzasGratis):
            descuento = descuento + precios[i]

        return round(descuento, 2), pizzasGratis

    #oferta 2: menu pizza + bebida, descuento por cada menu
    #cada menu necesita una pizza y una bebida (las pizzas gratis del 2x1 no cuentan)
    def menu(self, carrito, pizzasGratis):
        numPizzas = len(carrito.pizzas()) - pizzasGratis
        numBebidas = len(carrito.bebidas())
        menus = min(numPizzas, numBebidas)
        return menus * self.descuentoMenu

    #oferta 3: un dia de la semana descuento en las pizzas
    #no se aplica a las pizzas que ya salen gratis con el 2x1
    def descuentoDelDia(self, carrito, temporada, dia, descuento2x1):
        if dia != self.diaDescuento:
            return 0
        totalPizzas = 0
        for pizza in carrito.pizzas():
            totalPizzas = totalPizzas + pizza.precio(temporada)
        totalPizzas = totalPizzas - descuento2x1
        return round(totalPizzas * self.porcentajeDia, 2)

    #oferta 4: si el pedido pasa del minimo, descuento en el total
    def pedidoGrande(self, total):
        if total > self.minimoPedido:
            return round(total * self.porcentajePedido, 2)
        return 0

    #aplica todas las ofertas y devuelve una lista con los descuentos
    #cada descuento es una tupla (nombre de la oferta, dinero)
    def aplicar(self, carrito, temporada, dia):
        descuentos = []

        descuento2x1, pizzasGratis = self.dosPorUno(carrito, temporada)
        if descuento2x1 > 0:
            descuentos.append(("2x1", descuento2x1))

        descuentoMenu = self.menu(carrito, pizzasGratis)
        if descuentoMenu > 0:
            descuentos.append(("Menu pizza + bebida", descuentoMenu))

        descuentoDia = self.descuentoDelDia(carrito, temporada, dia, descuento2x1)
        if descuentoDia > 0:
            descuentos.append((self.nombreDescuentoDia(), descuentoDia))

        #el total despues de las otras ofertas
        total = carrito.total(temporada)
        for nombre, importe in descuentos:
            total = total - importe

        descuentoGrande = self.pedidoGrande(total)
        if descuentoGrande > 0:
            descuentos.append((self.nombrePedidoGrande(), descuentoGrande))

        return descuentos

    #textos de las ofertas, salen de los numeros guardados
    def nombreDescuentoDia(self):
        return f"{self.diaDescuento.capitalize()} {round(self.porcentajeDia * 100)}% pizzas"

    def nombrePedidoGrande(self):
        return f"Mas de {self.minimoPedido} euros {round(self.porcentajePedido * 100)}%"

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
        print("- 2x1 en " + ", ".join(self.pizzas2x1))
        print(f"- Menu pizza + bebida: {self.descuentoMenu} euro de descuento")
        print(f"- Los {self.diaDescuento} {round(self.porcentajeDia * 100)}% de descuento en pizzas")
        print(f"- Si el pedido pasa de {self.minimoPedido} euros, {round(self.porcentajePedido * 100)}% de descuento")


#ofertas que usa el resto del programa (por ejemplo el ticket)
ofertas = Ofertas()
