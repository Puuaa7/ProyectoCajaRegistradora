import unittest
from srcV2.bebidas2 import Bebida, bebidas, buscarBebida
from srcV1.bebidas import bebidas as bebidasV1


class TestBebidas(unittest.TestCase):
    def test_mismas_bebidas_que_v1(self):
        self.assertEqual(list(bebidas), list(bebidasV1))
        for nombre in bebidas:
            self.assertEqual(bebidas[nombre].precio(), bebidasV1[nombre])

    def test_precio_igual_en_todas_las_temporadas(self):
        cola = bebidas["cola"]
        for temporada in ("baja", "media", "alta"):
            self.assertEqual(cola.precio(temporada), 2.00)

    def test_buscar(self):
        self.assertIs(buscarBebida(" COLAZERO "), bebidas["colaZero"])
        self.assertIsNone(buscarBebida("vino"))

    def test_nombre_ticket(self):
        self.assertEqual(Bebida("agua", 1.20).nombreTicket(), "agua")


if __name__ == "__main__":
    unittest.main()
