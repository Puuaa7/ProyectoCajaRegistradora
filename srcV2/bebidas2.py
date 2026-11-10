#bebidas version 2


class Bebida:
    #cada bebida tiene un nombre y un precio fijo (ya lleva el iva incluido)
    def __init__(self, nombre, precioFijo):
        self.nombre = nombre
        self.precioFijo = precioFijo

    #la bebida cuesta lo mismo en todas las temporadas
    #recibe la temporada igual que la pizza, asi el carrito y el ticket
    #pueden pedir el precio de cualquier producto de la misma forma
    def precio(self, temporada=None):
        return self.precioFijo

    #nombre que sale en el ticket
    def nombreTicket(self):
        return self.nombre

    def __str__(self):
        return f"{self.nombre} - {self.precioFijo:.2f} €"


#bebidas con su precio
PRECIOS_BEBIDAS = {
    "agua": 1.20,
    "cola": 2.00,
    "colaZero": 2.00,
    "limonada": 2.00,
    "naranja": 2.00,
    "teFrio": 2.20,
    "cerveza": 2.50,
    "cervezaSinAlcohol": 2.50
}

#creamos un objeto Bebida por cada una
bebidas = {}
for nombre in PRECIOS_BEBIDAS:
    bebidas[nombre] = Bebida(nombre, PRECIOS_BEBIDAS[nombre])


#busca la bebida aunque la escribas en minusculas, si no existe devuelve None
def buscarBebida(texto):
    texto = texto.lower().strip()
    for nombre in bebidas:
        if nombre.lower() == texto:
            return bebidas[nombre]
    return None


#muestra todas las bebidas con su precio
def mostrarBebidas():
    print("")
    print("--- BEBIDAS ---")
    for bebida in bebidas.values():
        print(bebida)
