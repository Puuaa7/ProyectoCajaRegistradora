import unittest
from srcV2.ingredientes2 import Ingrediente, ingredientes, buscarIngrediente
from srcV1.ingredientes import ingredientes as ingredientesV1, calcularPrecioIngrediente


class TestIngredientes(unittest.TestCase):
    def test_mismos_ingredientes_que_v1(self):
        self.assertEqual(set(ingredientes), set(ingredientesV1))

    def test_mismo_precio_que_v1(self):
        for nombre in ingredientes:
            for gramos in (2, 50, 125, 250):
                self.assertEqual(ingredientes[nombre].precio(gramos),
                                 calcularPrecioIngrediente(nombre, gramos))

    def test_precio(self):
        self.assertEqual(Ingrediente("harina", 1.00).precio(250), 0.25)

    def test_buscar(self):
        self.assertEqual(buscarIngrediente("tomate").precioKg, 2.00)
        with self.assertRaises(ValueError):
            buscarIngrediente("kiwi")


if __name__ == "__main__":
    unittest.main()
