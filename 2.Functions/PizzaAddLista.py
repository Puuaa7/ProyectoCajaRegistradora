from ingredientes import calcularPrecioIngrediente

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
    }
}


#función para calcular el precio total de una pizza según sus ingredientes
def calcularPrecioPizza(nombrePizza):
    precioTotalPizza = 0

    for ingrediente in pizzas[nombrePizza]:
        gramos = pizzas[nombrePizza][ingrediente]
        total = total + calcularPrecioIngrediente(ingrediente, gramos)

    return round(precioTotalPizza, 2)

#falta calcular gasto fijo, gasto alquiler, beneficio, iva