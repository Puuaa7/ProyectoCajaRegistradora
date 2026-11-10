import unittest
from srcV2.gastos2 import Gastos, gastos
from srcV2.calculos2 import Calculadora, calculadora
from srcV1 import gastos as gastosV1


class TestGastos(unittest.TestCase):
    def test_mismos_gastos_que_v1(self):
        self.assertEqual(gastos.suministrosPorPizza, gastosV1.gasto_suministros_por_pizza)
        self.assertEqual(gastos.personalMensual, gastosV1.gasto_personal_mensual)
        self.assertEqual(gastos.alquilerMensual, gastosV1.gasto_alquiler_mensual)
        self.assertEqual(gastos.iva, gastosV1.iva)

    def test_gastos_fijos(self):
        self.assertEqual(gastos.gastosFijosMensuales(), 5800)

    def test_la_calculadora_usa_los_gastos(self):
        self.assertIs(calculadora.gastos, gastos)
        #con el doble de alquiler, los gastos fijos por pizza suben
        caro = Calculadora(gastos=Gastos(alquilerMensual=3200))
        self.assertGreater(caro.costeFijoPorPizza("media"), calculadora.costeFijoPorPizza("media"))

    def test_otro_iva(self):
        conIva21 = Calculadora(gastos=Gastos(iva=0.21))
        self.assertEqual(conIva21.separarIva(12.10), (10.00, 2.10))


if __name__ == "__main__":
    unittest.main()
