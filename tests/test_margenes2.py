import unittest
from srcV2.margenes2 import Margen, margen
from srcV2.calculos2 import Calculadora, calculadora
from srcV1.margenes import margen_beneficio_pizza


class TestMargen(unittest.TestCase):
    def test_mismo_margen_que_v1(self):
        self.assertEqual(margen.beneficio, margen_beneficio_pizza)
        self.assertEqual(margen.porcentaje(), 35)

    def test_aplicar(self):
        self.assertEqual(Margen(1.5).aplicar(10), 15)

    def test_la_calculadora_usa_el_margen(self):
        self.assertIs(calculadora.margen, margen)
        sinBeneficio = Calculadora(margen=Margen(1))
        self.assertEqual(sinBeneficio.precioSinIva(8.05), 8.05)


if __name__ == "__main__":
    unittest.main()
