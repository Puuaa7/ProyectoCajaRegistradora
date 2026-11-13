#pizzas version 2

from srcV2.ingredientes2 import buscarIngrediente
from srcV2.calculos2 import calculadora
from srcV2.producto2 import Producto


class Pizza(Producto):
    #Pizza hereda de Producto
    #cada pizza tiene un nombre y su receta: los objetos Ingrediente que lleva con sus gramos
    #(composicion: la pizza esta hecha de ingredientes)
    def __init__(self, nombre, receta):
        super().__init__(nombre)
        #al crear la pizza buscamos cada ingrediente en el catalogo
        #si alguno no existe se lanza IngredienteNoEncontradoError
        self._receta = {}
        for nombreIngrediente in receta:
            self._receta[buscarIngrediente(nombreIngrediente)] = receta[nombreIngrediente]

    #la receta como diccionario nombre del ingrediente -> gramos
    @property
    def receta(self):
        return {ingrediente.nombre: gramos for ingrediente, gramos in self._receta.items()}

    #suma lo que cuestan todos los ingredientes de la pizza
    def costeIngredientes(self):
        coste = 0
        for ingrediente, gramos in self._receta.items():
            coste = coste + ingrediente.precio(gramos)
        return round(coste, 2)

    #lo que nos cuesta hacer la pizza: ingredientes + suministros + gastos fijos
    def costeTotal(self, temporada):
        return calculadora.costeTotal(self.costeIngredientes(), temporada)

    #sobrescribe el metodo de Producto: coste total x margen de beneficio
    def precioSinIva(self, temporada=None):
        return calculadora.precioSinIva(self.costeTotal(temporada))

    #nombre que sale en el ticket
    def nombreTicket(self):
        return "Pizza " + self.nombre

    #los ingredientes juntos en un texto
    def textoIngredientes(self):
        return " ".join(self.receta)

    #muestra como se calcula el precio de la pizza
    def mostrarDesglose(self, temporada):
        costeIngredientes = self.costeIngredientes()
        costeFijo = calculadora.costeFijoPorPizza(temporada)
        costeTotal = calculadora.costeTotal(costeIngredientes, temporada)
        precioSinIva = calculadora.precioSinIva(costeTotal)
        precioConIva = calculadora.precioConIva(precioSinIva)

        print("")
        print("Precio de la pizza", self.nombre)
        print(f"Ingredientes: {costeIngredientes:.2f} €")
        print(f"Suministros: {calculadora.gastos.suministrosPorPizza:.2f} €")
        print(f"Gastos fijos: {costeFijo:.2f} €")
        print(f"Coste total: {costeTotal:.2f} €")
        print(f"Beneficio: {precioSinIva - costeTotal:.2f} €")
        print(f"Precio sin IVA: {precioSinIva:.2f} €")
        print(f"IVA: {precioConIva - precioSinIva:.2f} €")
        print(f"Precio final: {precioConIva:.2f} €")



#pizzas y sus ingredientes (gramos por ingrediente)
RECETAS = {
    "Margarita": {
        "harina": 250,
        "tomate": 100,
        "mozzarella": 120
    },

    "Prosciutto": {
        "harina": 250,
        "tomate": 100,
        "mozzarella": 120,
        "jamon": 80
    },

    "Barbacoa": {
        "harina": 250,
        "tomate": 100,
        "mozzarella": 100,
        "bacon": 60,
        "pollo": 100,
        "salsaBarbacoa": 40
    },

    "TomateSeco": {
        "harina": 250,
        "tomate": 80,
        "mozzarella": 120,
        "tomateSeco": 50
    },

    "Hawaiana": {
        "harina": 250,
        "tomate": 100,
        "mozzarella": 120,
        "jamon": 80,
        "piña": 70
    },

    "Carbonara": {
        "harina": 250,
        "mozzarella": 100,
        "bacon": 60,
        "huevo": 60
    },

    "Vegetariana": {
        "harina": 250,
        "tomate": 100,
        "mozzarella": 100,
        "champinones": 60,
        "cebolla": 40,
        "pimientos": 50
    },

    "CuatroQuesos": {
        "harina": 250,
        "tomate": 80,
        "mozzarella": 60,
        "parmesano": 30,
        "quesoDeCabra": 40,
        "gorgonzola": 40
    },

    "Pepperoni": {
        "harina": 250,
        "tomate": 100,
        "mozzarella": 120,
        "pepperoni": 70,
        "oregano": 2
    },

    "Tonno": {
        "harina": 250,
        "tomate": 100,
        "mozzarella": 100,
        "atun": 80,
        "cebolla": 40,
        "aceitunas": 30
    },

    "Diavola": {
        "harina": 250,
        "tomate": 100,
        "mozzarella": 110,
        "pepperoni": 50,
        "salchicha": 50,
        "pimientosPicantes": 20
    },

    "Funghi": {
        "harina": 250,
        "tomate": 100,
        "mozzarella": 120,
        "champinones": 90,
        "salsaAjo": 20
    },

    "Bufala": {
        "harina": 250,
        "tomate": 120,
        "mozzarellaDiBufala": 125,
        "albahaca": 5
    },

    "Pesto": {
        "harina": 250,
        "pesto": 50,
        "mozzarella": 100,
        "rucula": 25,
        "parmesano": 20
    },

    "Burrata": {
        "harina": 250,
        "tomate": 100,
        "burrata": 125,
        "rucula": 20,
        "tomateSeco": 30
    },

    "Trufada": {
        "harina": 250,
        "mozzarella": 120,
        "champinones": 60,
        "trufa": 4,
        "parmesano": 20
    },

    "Mediterranea": {
        "harina": 250,
        "tomate": 100,
        "mozzarella": 100,
        "berenjena": 50,
        "calabacin": 50,
        "pimientosRojos": 40,
        "olivasNegras": 30
    },

    "Campesina": {
        "harina": 250,
        "tomate": 100,
        "mozzarella": 100,
        "pollo": 90,
        "maiz": 40,
        "pimientosVerdes": 40,
        "cebolla": 30
    },

    "CabraMiel": {
        "harina": 250,
        "mozzarella": 80,
        "quesoDeCabra": 80,
        "cebollaCaramelizada": 50,
        "miel": 20
    },

    "Primavera": {
        "harina": 250,
        "tomate": 100,
        "mozzarella": 100,
        "espinacas": 50,
        "alcachofas": 50,
        "brocoli": 40,
        "huevoDuro": 50
    },

    "DulceDubai": {
        "harina": 250,
        "chocolateDubai": 60,
        "platano": 80,
        "miel": 15
    }
}

#creamos un objeto Pizza por cada receta
pizzas = {}
for nombre in RECETAS:
    pizzas[nombre] = Pizza(nombre, RECETAS[nombre])


#busca la pizza aunque la escribas en minusculas, si no existe devuelve None
def buscarPizza(texto):
    texto = texto.lower().strip()
    for nombre in pizzas:
        if nombre.lower() == texto:
            return pizzas[nombre]
    return None


#muestra todas las pizzas con su precio
def mostrarPizzas(temporada):
    print("")
    print("--- PIZZAS ---")
    numero = 1
    for pizza in pizzas.values():
        print(f"{numero}. {pizza.nombre} - {pizza.precio(temporada):.2f} €  ({pizza.textoIngredientes()})")
        numero = numero + 1
