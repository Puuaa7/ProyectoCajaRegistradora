import unittest
from unittest.mock import patch
from io import StringIO
import main


#ejecuta main() escribiendo las respuestas como si fuera el usuario
def ejecutar(respuestas):
    with patch("builtins.input", side_effect=respuestas), patch("sys.stdout", new=StringIO()) as salida:
        main.main()
    return salida.getvalue()


class TestMain(unittest.TestCase):
    def test_version_1(self):
        salida = ejecutar(["1", "media", "0"])
        self.assertIn("----- PIZZERIA PYTHON -----", salida)
        self.assertNotIn("(v2)", salida)

    def test_version_2(self):
        salida = ejecutar(["2", "media", "0"])
        self.assertIn("PIZZERIA PYTHON (v2)", salida)

    def test_respuesta_incorrecta(self):
        salida = ejecutar(["3", "dos", "2", "media", "0"])
        self.assertEqual(salida.count("Escribe 1 o 2"), 2)
        self.assertIn("(v2)", salida)


if __name__ == "__main__":
    unittest.main()
