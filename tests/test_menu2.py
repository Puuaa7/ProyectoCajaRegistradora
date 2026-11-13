import unittest
from unittest.mock import patch
from io import StringIO
from srcV2.menu2 import Caja, iniciarCaja


#ejecuta la caja escribiendo las respuestas como si fuera el usuario
def ejecutar(funcion, respuestas):
    with patch("builtins.input", side_effect=respuestas), patch("sys.stdout", new=StringIO()) as salida:
        funcion()
    return salida.getvalue()


class TestMenu(unittest.TestCase):
    def test_compra_completa(self):
        caja = Caja("media", "martes")
        salida = ejecutar(caja.iniciar, ["4", "margarita", "2", "4", "cola", "1", "7", "0"])
        self.assertIn("Total: ", salida)
        self.assertIn("2x1", salida)
        self.assertTrue(caja.carrito.estaVacio())

    def test_cantidad_incorrecta(self):
        caja = Caja("media", "lunes")
        salida = ejecutar(caja.iniciar, ["4", "margarita", "dos", "4", "margarita", "0", "0"])
        self.assertIn("La cantidad 'dos' no es válida", salida)
        self.assertIn("La cantidad '0' no es válida", salida)
        self.assertTrue(caja.carrito.estaVacio())

    def test_cambiar_temporada_y_dia(self):
        caja = Caja("media", "lunes")
        ejecutar(caja.iniciar, ["9", "invierno", "ALTA", "10", "festivo", "Martes", "0"])
        self.assertEqual(caja.temporada, "alta")
        self.assertEqual(caja.dia, "martes")

    def test_todas_las_opciones(self):
        caja = Caja("baja", "viernes")
        salida = ejecutar(caja.iniciar, ["1", "2", "3", "4", "agua", "1", "5", "agua", "6",
                                         "8", "barbacoa", "8", "kebab", "7", "99", "0"])
        self.assertIn("--- PIZZAS ---", salida)
        self.assertIn("--- BEBIDAS ---", salida)
        self.assertIn("--- OFERTAS ---", salida)
        self.assertIn("Precio de la pizza Barbacoa", salida)
        self.assertIn("Esa pizza no existe", salida)
        self.assertIn("El carrito esta vacio", salida)
        self.assertIn("Opcion incorrecta", salida)

    def test_errores_no_cierran_la_caja(self):
        caja = Caja("media", "lunes")
        salida = ejecutar(caja.iniciar, ["4", "kebab", "1", "5", "kebab", "4", "cola", "1", "0"])
        self.assertEqual(salida.count("El producto 'kebab' no existe"), 2)
        self.assertEqual(len(caja.carrito), 1)

    def test_iniciar_caja(self):
        salida = ejecutar(iniciarCaja, ["media", "0"])
        self.assertIn("PIZZERIA PYTHON (v2)", salida)
        self.assertIn("Adios!", salida)


if __name__ == "__main__":
    unittest.main()
