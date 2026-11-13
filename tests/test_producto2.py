import unittest
from srcV2.producto2 import Producto
from srcV2.pizzas2 import Pizza, pizzas
from srcV2.bebidas2 import Bebida, bebidas
from srcV2.excepciones2 import IngredienteNoEncontradoError, PrecioNoValidoError


class TestProducto(unittest.TestCase):
    def test_no_se_puede_crear_un_producto(self):
        #Producto es abstracta
        with self.assertRaises(TypeError):
            Producto("algo")

    def test_herencia(self):
        self.assertIsInstance(pizzas["Margarita"], Producto)
        self.assertIsInstance(bebidas["cola"], Producto)
        self.assertTrue(issubclass(Pizza, Producto))
        self.assertTrue(issubclass(Bebida, Producto))

    def test_polimorfismo(self):
        #el mismo bucle sirve para pizzas y bebidas: cada una calcula su precio a su manera
        productos = [pizzas["Margarita"], bebidas["cola"], pizzas["Barbacoa"]]
        for producto in productos:
            self.assertEqual(producto.precio("media"),
                             round(producto.precioSinIva("media") + producto.iva("media"), 2))

    def test_iva_de_la_margarita(self):
        margarita = pizzas["Margarita"]
        self.assertEqual(margarita.precio("media"), 11.95)
        self.assertEqual(round(margarita.precioSinIva("media"), 2), 10.87)
        self.assertEqual(margarita.iva("media"), 1.08)

    def test_iva_de_la_bebida(self):
        cola = bebidas["cola"]
        self.assertEqual(cola.precio(), 2.00)
        self.assertAlmostEqual(cola.precioSinIva(), 2.00 / 1.10)
        self.assertEqual(cola.iva(), 0.18)

    def test_nombre_solo_lectura(self):
        with self.assertRaises(AttributeError):
            pizzas["Margarita"].nombre = "Otra"

    def test_validaciones(self):
        with self.assertRaises(IngredienteNoEncontradoError):
            Pizza("Rara", {"harina": 250, "kiwi": 50})
        with self.assertRaises(PrecioNoValidoError):
            Bebida("regalo", -1)


if __name__ == "__main__":
    unittest.main()
