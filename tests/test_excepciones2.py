import unittest
from srcV2.excepciones2 import (PizzeriaError, ProductoNoEncontradoError, IngredienteNoEncontradoError,
                                CantidadNoValidaError, PrecioNoValidoError, leerCantidad)


class TestExcepciones(unittest.TestCase):
    def test_todas_heredan_de_pizzeria_error(self):
        for clase in (ProductoNoEncontradoError, IngredienteNoEncontradoError, CantidadNoValidaError, PrecioNoValidoError):
            self.assertTrue(issubclass(clase, PizzeriaError))
            self.assertTrue(issubclass(clase, Exception))

    def test_leer_cantidad_correcta(self):
        self.assertEqual(leerCantidad("3"), 3)
        self.assertEqual(leerCantidad(" 12 "), 12)
        self.assertEqual(leerCantidad(2), 2)

    def test_leer_cantidad_incorrecta(self):
        for valor in ("0", "-1", "dos", "1.5", "", "²", 0, -4, True):
            with self.assertRaises(CantidadNoValidaError):
                leerCantidad(valor)

    def test_mensaje(self):
        self.assertEqual(str(ProductoNoEncontradoError("kebab")), "El producto 'kebab' no existe")


if __name__ == "__main__":
    unittest.main()
