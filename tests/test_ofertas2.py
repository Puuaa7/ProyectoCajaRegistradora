import unittest
import random
from srcV2.ofertas2 import Ofertas, ofertas
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
            temporada = random.choice(("baja", "media", "alta"))
            dia = random.choice(dias)
            self.assertEqual(ofertas.aplicar(carrito, temporada, dia), aplicarOferta(lista, temporada, dia))

    def test_otras_ofertas(self):
        sinMenu = Ofertas(descuentoMenu=0, diaDescuento="lunes")
        carrito, lista = crearCarritos(["Barbacoa", "cola"])
        nombres = [nombre for nombre, importe in sinMenu.aplicar(carrito, "media", "lunes")]
        self.assertEqual(nombres, ["Lunes 20% pizzas"])


if __name__ == "__main__":
    unittest.main()
