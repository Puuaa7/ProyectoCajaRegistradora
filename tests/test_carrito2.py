import unittest
from srcV2.carrito2 import Carrito, buscarProducto, esPizza, esBebida
from srcV2.pizzas2 import pizzas
from srcV2.bebidas2 import bebidas
from srcV2.ticket2 import Ticket
from srcV1.carrito import calcularTotalCarrito


class TestCarrito(unittest.TestCase):
    def setUp(self):
        self.carrito = Carrito()

    def test_empieza_vacio(self):
        self.assertTrue(self.carrito.estaVacio())
        self.assertEqual(self.carrito.total("media"), 0)

    def test_buscar_producto(self):
        self.assertIs(buscarProducto("margarita"), pizzas["Margarita"])
        self.assertIs(buscarProducto("Cola"), bebidas["cola"])
        self.assertIsNone(buscarProducto("kebab"))
        self.assertTrue(esPizza(pizzas["Margarita"]))
        self.assertTrue(esBebida(bebidas["cola"]))

    def test_agregar_y_quitar(self):
        self.assertTrue(self.carrito.agregar("margarita", 2))
        self.assertFalse(self.carrito.agregar("kebab", 1))
        self.assertTrue(self.carrito.agregar("cola", 1))
        self.assertEqual(len(self.carrito), 3)
        self.assertTrue(self.carrito.quitar("Margarita"))
        self.assertFalse(self.carrito.quitar("agua"))
        self.assertEqual(len(self.carrito), 2)

    def test_contar_y_separar(self):
        self.carrito.agregar("margarita", 2)
        self.carrito.agregar("cola", 1)
        cantidades = self.carrito.contarProductos()
        self.assertEqual(cantidades[pizzas["Margarita"]], 2)
        self.assertEqual(cantidades[bebidas["cola"]], 1)
        self.assertEqual(len(self.carrito.pizzas()), 2)
        self.assertEqual(len(self.carrito.bebidas()), 1)

    def test_mismo_total_que_v1(self):
        self.carrito.agregar("barbacoa", 2)
        self.carrito.agregar("trufada", 1)
        self.carrito.agregar("cerveza", 3)
        listaV1 = ["Barbacoa", "Barbacoa", "Trufada", "cerveza", "cerveza", "cerveza"]
        for temporada in ("baja", "media", "alta"):
            self.assertEqual(self.carrito.total(temporada), calcularTotalCarrito(listaV1, temporada))

    def test_vaciar(self):
        self.carrito.agregar("agua", 2)
        self.carrito.vaciar()
        self.assertTrue(self.carrito.estaVacio())

    def test_ticket_con_carrito_real(self):
        class SinOfertas:
            def aplicar(self, carrito, temporada, dia):
                return []
        self.carrito.agregar("margarita", 1)
        self.carrito.agregar("agua", 1)
        total = Ticket(self.carrito, "media", "lunes", SinOfertas()).mostrar()
        self.assertEqual(total, round(pizzas["Margarita"].precio("media") + 1.20, 2))


if __name__ == "__main__":
    unittest.main()
