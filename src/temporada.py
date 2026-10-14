# Prevision mensual segun la temporada.

def obtener_pizzas_estimadas(temporada):
    match temporada:
        case "baja":
            return 600
        case "media":
            return 1000
        case "alta":
            return 1500
        case _:
            return 1000
