from src.ingredientes import calcularPrecioIngrediente
from src.calculos import calcularCosteFijoPorPizza, calcularCosteTotal, calcularPrecioSinIva, calcularPrecioConIva
from src.gastos import gasto_suministros_por_pizza

#1. PIZZAS Y SUS INGREDIENTES (gramos por ingrediente)
pizzas = {
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


#funcion que suma lo que cuestan todos los ingredientes de una pizza
def calcularCosteIngredientes(nombrePizza):
    costeIngredientes = 0

    for ingrediente in pizzas[nombrePizza]:
        gramos = pizzas[nombrePizza][ingrediente]
        costeIngredientes = costeIngredientes + calcularPrecioIngrediente(ingrediente, gramos)

    return round(costeIngredientes, 2)


#funcion para calcular el precio final de la pizza (con gastos, beneficio e iva)
def calcularPrecioPizza(nombrePizza, temporada):
    costeIngredientes = calcularCosteIngredientes(nombrePizza)
    costeTotal = calcularCosteTotal(costeIngredientes, temporada)
    precioSinIva = calcularPrecioSinIva(costeTotal)
    precioConIva = calcularPrecioConIva(precioSinIva)
    return precioConIva


#muestra todas las pizzas con su precio
def mostrarPizzas(temporada):
    print("")
    print("--- PIZZAS ---")
    numero = 1
    for nombre in pizzas:
        precio = calcularPrecioPizza(nombre, temporada)

        textoIngredientes = ""
        for ingrediente in pizzas[nombre]:
            textoIngredientes = textoIngredientes + ingrediente + " "

        print(f"{numero}. {nombre} - {precio} €  ({textoIngredientes})")
        numero = numero + 1


#muestra como se calcula el precio de una pizza
def mostrarDesglosePizza(nombrePizza, temporada):
    costeIngredientes = calcularCosteIngredientes(nombrePizza)
    costeFijo = calcularCosteFijoPorPizza(temporada)
    costeTotal = calcularCosteTotal(costeIngredientes, temporada)
    precioSinIva = calcularPrecioSinIva(costeTotal)
    precioConIva = calcularPrecioConIva(precioSinIva)

    print("")
    print("Precio de la pizza", nombrePizza)
    print("Ingredientes:", round(costeIngredientes, 2), "€")
    print("Suministros:", gasto_suministros_por_pizza, "€")
    print("Gastos fijos:", round(costeFijo, 2), "€")
    print("Coste total:", round(costeTotal, 2), "€")
    print("Beneficio:", round(precioSinIva - costeTotal, 2), "€")
    print("Precio sin IVA:", round(precioSinIva, 2), "€")
    print("IVA:", round(precioConIva - precioSinIva, 2), "€")
    print("Precio final:", precioConIva, "€")
