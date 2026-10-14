import unittest
from src.pizzas import pizzas, calcularPrecioPizza
from src.temporada import obtener_pizzas_estimadas
from src.calculos import calcular_precio_venta

class TestCaja(unittest.TestCase):
    def test_todas_las_pizzas(self):
        for nombre in pizzas:
            self.assertGreater(calcularPrecioPizza(nombre), 0)
            self.assertGreater(calcular_precio_venta(nombre)["precio_con_iva"], 0)

    def test_temporada(self):
        self.assertEqual(obtener_pizzas_estimadas("baja"), 600)
        self.assertEqual(obtener_pizzas_estimadas("alta"), 1500)

if __name__ == "__main__":
    unittest.main()
