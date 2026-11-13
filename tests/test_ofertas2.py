import unittest
import random
from srcV2.ofertas2 import (Ofertas, ofertas, Oferta, Oferta2x1, OfertaMenu, OfertaDiaSemana,
                            OfertaTemporada, OfertaPedidoGrande)
from srcV2.carrito2 import Carrito
from srcV2.pizzas2 import pizzas
from srcV2.bebidas2 import bebidas
from srcV1.ofertas import aplicarOferta

dias = ("lunes", "martes", "miercoles", "jueves", "viernes", "sabado", "domingo")


#crea un carrito v2 y la lista equivalente de la v1
def crearCarritos(nombres):
    carrito = Carrito()
    for nombre in nombres:
        carrito.agregar(nombre, 1)
    return carrito, list(nombres)


class TestOfertas(unittest.TestCase):
    def test_sin_ofertas(self):
        carrito, lista = crearCarritos(["Barbacoa"])
        self.assertEqual(ofertas.aplicar(carrito, "media", "lunes"), [])

    def test_2x1(self):
        carrito, lista = crearCarritos(["Margarita", "Prosciutto"])
        self.assertIn(("2x1", pizzas["Margarita"].precio("media")), ofertas.aplicar(carrito, "media", "lunes"))

    def test_menu(self):
        carrito, lista = crearCarritos(["Barbacoa", "cola"])
        self.assertIn(("Menu pizza + bebida", 1), ofertas.aplicar(carrito, "media", "lunes"))

    def test_martes(self):
        carrito, lista = crearCarritos(["Barbacoa"])
        nombres = [nombre for nombre, importe in ofertas.aplicar(carrito, "media", "martes")]
        self.assertIn("Martes 20% pizzas", nombres)

    def test_mismos_descuentos_que_v1(self):
        random.seed(7)
        productos = list(pizzas) + list(bebidas)
        for prueba in range(300):
            nombres = [random.choice(productos) for i in range(random.randint(1, 8))]
            carrito, lista = crearCarritos(nombres)
            #en temporada baja la v2 tiene una oferta nueva (bebidas), por eso solo media y alta
            temporada = random.choice(("media", "alta"))
            dia = random.choice(dias)
            self.assertEqual(ofertas.aplicar(carrito, temporada, dia), aplicarOferta(lista, temporada, dia))

    def test_otras_ofertas(self):
        #se puede crear una lista de ofertas distinta sin tocar el codigo
        soloLunes = Ofertas([OfertaDiaSemana(Oferta2x1(), dia="lunes")])
        carrito, lista = crearCarritos(["Barbacoa", "cola"])
        nombres = [nombre for nombre, importe in soloLunes.aplicar(carrito, "media", "lunes")]
        self.assertEqual(nombres, ["Lunes 20% pizzas"])

    def test_jerarquia(self):
        with self.assertRaises(TypeError):
            Oferta("abstracta")
        for oferta in ofertas.lista:
            self.assertIsInstance(oferta, Oferta)
        self.assertEqual([type(o) for o in ofertas.lista],
                         [Oferta2x1, OfertaMenu, OfertaDiaSemana, OfertaTemporada, OfertaPedidoGrande])

    def test_temporada_baja(self):
        carrito, lista = crearCarritos(["cerveza", "cerveza"])
        self.assertIn(("Temporada baja 10% bebidas", 0.5), ofertas.aplicar(carrito, "baja", "lunes"))
        self.assertEqual(ofertas.aplicar(carrito, "media", "lunes"), [])

    def test_es_aplicable(self):
        carrito, lista = crearCarritos(["Barbacoa"])
        self.assertTrue(OfertaDiaSemana(Oferta2x1()).esAplicable(carrito, "media", "martes"))
        self.assertFalse(OfertaDiaSemana(Oferta2x1()).esAplicable(carrito, "media", "lunes"))

    def test_baja_igual_que_v1_sin_bebidas(self):
        #sin bebidas, la temporada baja da lo mismo que en la v1
        random.seed(3)
        for prueba in range(100):
            nombres = [random.choice(list(pizzas)) for i in range(random.randint(1, 6))]
            carrito, lista = crearCarritos(nombres)
            dia = random.choice(dias)
            self.assertEqual(ofertas.aplicar(carrito, "baja", dia), aplicarOferta(lista, "baja", dia))


if __name__ == "__main__":
    unittest.main()
