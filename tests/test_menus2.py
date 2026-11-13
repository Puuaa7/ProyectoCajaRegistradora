import unittest
from unittest.mock import patch
from io import StringIO
from srcV2.menus2 import Menu, crearMenuPizzaBebida, crearMenuFamiliar
from srcV2.producto2 import Producto
from srcV2.pizzas2 import pizzas
from srcV2.bebidas2 import bebidas
from srcV2.carrito2 import Carrito
from srcV2.ofertas2 import ofertas
from srcV2.ticket2 import Ticket
from srcV2.menu2 import Caja
from srcV2.excepciones2 import PrecioNoValidoError


def ejecutar(funcion, respuestas):
    with patch("builtins.input", side_effect=respuestas), patch("sys.stdout", new=StringIO()) as salida:
        resultado = funcion()
    return salida.getvalue(), resultado


class TestMenus(unittest.TestCase):
    def test_menu_es_un_producto(self):
        menu = crearMenuPizzaBebida(pizzas["Barbacoa"], bebidas["cola"])
        self.assertIsInstance(menu, Producto)

    def test_precio_menu_pizza_bebida(self):
        menu = crearMenuPizzaBebida(pizzas["Barbacoa"], bebidas["cola"])
        porSeparado = round(pizzas["Barbacoa"].precio("media") + 2.00, 2)
        self.assertEqual(menu.precioPorSeparado("media"), porSeparado)
        self.assertEqual(menu.precio("media"), round(porSeparado - 1, 2))
        self.assertEqual(menu.iva("media"), round(menu.precio("media") - menu.precioSinIva("media"), 2))

    def test_menu_familiar(self):
        menu = crearMenuFamiliar(pizzas["Margarita"], pizzas["Funghi"], bebidas["agua"], bebidas["cerveza"])
        self.assertEqual(len(menu.productos), 4)
        self.assertEqual(menu.precio("alta"), round(menu.precioPorSeparado("alta") - 5, 2))
        self.assertIn("Pizza Funghi", menu.nombreTicket())

    def test_descuento_negativo(self):
        with self.assertRaises(PrecioNoValidoError):
            Menu("Raro", [bebidas["agua"]], -1)

    def test_menu_en_el_carrito_y_el_ticket(self):
        carrito = Carrito()
        menu = crearMenuPizzaBebida(pizzas["Barbacoa"], bebidas["cola"])
        carrito.agregarProducto(menu, 1)
        #las pizzas del menu no cuentan para las demas ofertas (ya tienen su descuento)
        self.assertEqual(carrito.pizzas(), [])
        salida, total = ejecutar(lambda: Ticket(carrito, "media", "lunes", ofertas).mostrar(), [])
        self.assertIn("Menu pizza + bebida (Pizza Barbacoa, cola)", salida)
        self.assertEqual(total, menu.precio("media"))

    def test_añadir_menu_desde_la_caja(self):
        caja = Caja("media", "lunes")
        salida, resultado = ejecutar(caja.iniciar, ["11", "2", "margarita", "funghi", "agua", "cola",
                                                    "11", "1", "kebab", "cola", "11", "9", "0"])
        self.assertEqual(len(caja.carrito), 1)
        self.assertIn("Menu familiar", salida)
        self.assertIn("El producto 'kebab' no existe", salida)
        self.assertIn("Ese menu no existe", salida)


if __name__ == "__main__":
    unittest.main()
