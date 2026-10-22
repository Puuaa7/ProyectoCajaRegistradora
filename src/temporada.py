temporadas = ("baja", "media", "alta")

#pizzas que se venden al mes
def obtenerPizzasEstimadas(temporada):
    if temporada == "baja":
        return 600
    elif temporada == "media":
        return 1000
    elif temporada == "alta":
        return 1500
    #raise protege el cálculo si otra parte del programa llama a la función con una temporada incorrecta
    raise ValueError("Temporada no válida")