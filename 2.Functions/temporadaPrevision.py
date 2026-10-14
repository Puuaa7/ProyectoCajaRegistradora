#TEMPORADA Y PREVISION DE VENTAS

#tupla con las temporadas posibles (no cambian nunca, por eso es una tupla)
temporadas = ("baja", "media", "alta")


#devuelve cuantas pizzas se espera vender al mes segun la temporada
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