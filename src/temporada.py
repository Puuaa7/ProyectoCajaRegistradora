temporadas = ("baja", "media", "alta")


#pizzas que se venden al mes segun la temporada
def obtenerPizzasEstimadas(temporada):
    match temporada:
        case "baja":
            pizzas_estimadas_mes = 600
        case "media":
            pizzas_estimadas_mes = 1000
        case "alta":
            pizzas_estimadas_mes = 1500
        case _:
            pizzas_estimadas_mes = 1000

    return pizzas_estimadas_mes
