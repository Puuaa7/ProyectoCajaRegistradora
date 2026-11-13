import unittest
from srcV2.ingredientes2 import Ingrediente, ingredientes, buscarIngrediente
from srcV2.excepciones2 import IngredienteNoEncontradoError, PrecioNoValidoError
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
        with self.assertRaises(IngredienteNoEncontradoError):
            buscarIngrediente("kiwi")

    def test_encapsulacion(self):
        harina = Ingrediente("harina", 1.00)
        #el nombre solo se puede leer
        with self.assertRaises(AttributeError):
            harina.nombre = "otra"
        #el precio se puede cambiar, pero nunca a un numero negativo
        harina.precioKg = 1.50
        self.assertEqual(harina.precioKg, 1.50)
        with self.assertRaises(PrecioNoValidoError):
            harina.precioKg = -1
        with self.assertRaises(PrecioNoValidoError):
            Ingrediente("gratis", -2)


if __name__ == "__main__":
    unittest.main()
