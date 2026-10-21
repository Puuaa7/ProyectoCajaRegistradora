import unittest
from src.pizzas import pizzas, calcularCosteIngredientes, calcularPrecioPizza
from src.ingredientes import ingredientes
from src.temporada import obtenerPizzasEstimadas
from src.calculos import separarIva
from src.carrito import calcularTotalCarrito
from src.ofertas import aplicarOferta

class TestCaja(unittest.TestCase):
    def test_hay_20_pizzas(self):
        self.assertGreaterEqual(len(pizzas), 20)

    def test_ingredientes_existen(self):
        for nombre in pizzas:
            for ingrediente in pizzas[nombre]:
                self.assertIn(ingrediente, ingredientes)

    def test_todas_las_pizzas(self):
        for nombre in pizzas:
            self.assertGreater(calcularCosteIngredientes(nombre), 0)
            self.assertGreater(calcularPrecioPizza(nombre, "media"), 0)

    def test_temporada(self):
        self.assertEqual(obtenerPizzasEstimadas("baja"), 600)
        self.assertEqual(obtenerPizzasEstimadas("alta"), 1500)
        self.assertEqual(obtenerPizzasEstimadas("otra"), 1000)

    def test_separar_iva(self):
        base, importe_iva = separarIva(11.00)
        self.assertEqual(base, 10.00)
        self.assertEqual(importe_iva, 1.00)

    def test_2x1(self):
        carrito = ["Margarita", "Prosciutto"]
        descuentos = aplicarOferta(carrito, "media", "lunes")
        self.assertIn(("2x1", calcularPrecioPizza("Margarita", "media")), descuentos)

    def test_sin_ofertas(self):
        carrito = ["Barbacoa"]
        self.assertEqual(aplicarOferta(carrito, "media", "lunes"), [])
        self.assertEqual(calcularTotalCarrito(carrito, "media"), calcularPrecioPizza("Barbacoa", "media"))

if __name__ == "__main__":
    unittest.main()
