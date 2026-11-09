#ticket version 2

from srcV2.calculos2 import calculadora


class Ticket:
    #el ticket necesita el carrito, la temporada, el dia y las ofertas
    def __init__(self, carrito, temporada, dia, ofertas):
        self.carrito = carrito
        self.temporada = temporada
        self.dia = dia
        self.ofertas = ofertas

    #imprime el ticket y devuelve el total pagado
    def mostrar(self):
        if self.carrito.estaVacio():
            print("El carrito esta vacio")
            return 0

        print("")
        print("PIZZERIA PYTHON")
        print("")

        #productos
        print("Productos:")
        cantidades = self.carrito.contarProductos()
        for producto in cantidades:
            precio = producto.precio(self.temporada) * cantidades[producto]
            print(f"- {producto.nombreTicket()} x{cantidades[producto]}: {precio:.2f} €")

        #descuentos
        total = self.carrito.total(self.temporada)
        descuentos = self.ofertas.aplicar(self.carrito, self.temporada, self.dia)

        if len(descuentos) > 0:
            print("")
            print("Descuentos:")
            for descuento in descuentos:
                nombre, importe = descuento
                print(f"- {nombre}: -{importe:.2f} €")
                total = total - importe

        #total final y su desglose de iva
        total = round(total, 2)
        baseImponible, importeIva = calculadora.separarIva(total)

        print("")
        print(f"Base imponible: {baseImponible:.2f} €")
        print(f"IVA: {importeIva:.2f} €")
        print(f"Total: {total:.2f} €")
        print("")
        print("Gracias por su compra.")

        return total
