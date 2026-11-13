import unittest
from srcV2.pizzas2 import Pizza, pizzas, buscarPizza
from srcV2.ingredientes2 import ingredientes
from srcV1.pizzas import pizzas as pizzasV1, calcularCosteIngredientes, calcularPrecioPizza


class TestPizzas(unittest.TestCase):
    def test_mismas_pizzas_que_v1(self):
        self.assertEqual(list(pizzas), list(pizzasV1))

    def test_ingredientes_existen(self):
        for pizza in pizzas.values():
            for ingrediente in pizza.receta:
                self.assertIn(ingrediente, ingredientes)

    def test_mismo_precio_que_v1(self):
        for nombre in pizzas:
            self.assertEqual(pizzas[nombre].costeIngredientes(), calcularCosteIngredientes(nombre))
            for temporada in ("baja", "media", "alta"):
                self.assertEqual(pizzas[nombre].precio(temporada), calcularPrecioPizza(nombre, temporada))

    def test_buscar(self):
        self.assertIs(buscarPizza("  margarita "), pizzas["Margarita"])
        self.assertIsNone(buscarPizza("kebab"))

    def test_nombre_ticket(self):
        self.assertEqual(pizzas["Margarita"].nombreTicket(), "Pizza Margarita")

    def test_pizza_nueva(self):
        pizza = Pizza("Prueba", {"harina": 250, "tomate": 100})
        self.assertEqual(pizza.costeIngredientes(), 0.45)


if __name__ == "__main__":
    unittest.main()
