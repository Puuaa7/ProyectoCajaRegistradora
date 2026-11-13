import unittest
from srcV2.calculos2 import Calculadora, calculadora
from srcV2.temporada import Temporada, media
from srcV2.gastos2 import Gastos
from srcV1.pizzas import pizzas, calcularCosteIngredientes, calcularPrecioPizza


class TestCalculadora(unittest.TestCase):
    def test_separar_iva(self):
        self.assertEqual(calculadora.separarIva(11.00), (10.00, 1.00))

    def test_pizzas_del_mes(self):
        self.assertEqual(calculadora.pizzasDelMes("baja"), 600)
        self.assertEqual(calculadora.pizzasDelMes("alta"), 1500)

    def test_temporada_incorrecta(self):
        with self.assertRaises(ValueError):
            calculadora.pizzasDelMes("otra")

    def test_acepta_objeto_temporada(self):
        self.assertEqual(calculadora.pizzasDelMes(media), 1000)
        self.assertEqual(calculadora.costeFijoPorPizza(media), calculadora.costeFijoPorPizza("media"))

    def test_temporada_nueva(self):
        #una temporada inventada con 2900 pizzas: (4200 + 1600) / 2900 = 2 euros por pizza
        festival = Temporada("festival", 2900)
        self.assertEqual(calculadora.costeFijoPorPizza(festival), 2)

    def test_mismo_precio_que_v1(self):
        for nombre in pizzas:
            for temporada in ("baja", "media", "alta"):
                coste = calcularCosteIngredientes(nombre)
                self.assertEqual(calculadora.precioFinal(coste, temporada),
                                 calcularPrecioPizza(nombre, temporada))

    def test_otra_calculadora(self):
        sinIva = Calculadora(gastos=Gastos(iva=0))
        self.assertEqual(sinIva.separarIva(10), (10, 0))


if __name__ == "__main__":
    unittest.main()
