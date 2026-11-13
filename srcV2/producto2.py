#producto version 2: clase base de todo lo que se vende

from abc import ABC, abstractmethod

from srcV2.calculos2 import calculadora


class Producto(ABC):
    #Producto es una clase abstracta (hereda de ABC): no se puede crear un Producto
    #directamente, solo sus subclases Pizza, Bebida y Menu
    #define lo que todos los productos saben hacer, asi el carrito, las ofertas y el
    #ticket los tratan igual sin saber de que tipo es cada uno (polimorfismo)
    def __init__(self, nombre):
        self._nombre = nombre

    #el nombre se puede leer pero no cambiar (encapsulacion)
    @property
    def nombre(self):
        return self._nombre

    #cada subclase calcula su precio sin iva a su manera
    @abstractmethod
    def precioSinIva(self, temporada=None):
        pass

    #precio con iva redondeado a 2 decimales (lo que paga el cliente)
    def precio(self, temporada=None):
        return calculadora.precioConIva(self.precioSinIva(temporada))

    #iva que lleva el precio del producto
    def iva(self, temporada=None):
        return round(self.precio(temporada) - self.precioSinIva(temporada), 2)

    #nombre que sale en el ticket
    def nombreTicket(self):
        return self.nombre

    def __str__(self):
        return self.nombreTicket()
