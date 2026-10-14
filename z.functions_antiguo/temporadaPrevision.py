temporada = "media"

match temporada:
    case "baja":
        pizzas_estimadas_mes = 600
    case "media":
        pizzas_estimadas_mes = 1000
    case "alta":
        pizzas_estimadas_mes = 1500
    case _:
        pizzas_estimadas_mes = 1000