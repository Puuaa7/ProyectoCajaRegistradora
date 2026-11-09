#temporada version 2


class Temporada:
    #cada temporada tiene un nombre y las pizzas que se venden al mes
    def __init__(self, nombre, pizzasEstimadas):
        self.nombre = nombre
        self.pizzasEstimadas = pizzasEstimadas

    #pizzas que se venden al mes en esta temporada
    def obtenerPizzasEstimadas(self):
        return self.pizzasEstimadas

    #lo que se ve al hacer print de la temporada
    def __str__(self):
        return f"Temporada {self.nombre} ({self.pizzasEstimadas} pizzas/mes)"


#temporadas posibles
baja = Temporada("baja", 600)
media = Temporada("media", 1000)
alta = Temporada("alta", 1500)

temporadas = (baja, media, alta)


#busca la temporada por su nombre ("baja", "media" o "alta")
def obtenerTemporada(nombre):
    for temporada in temporadas:
        if temporada.nombre == nombre:
            return temporada
    #raise protege el programa si alguien pide una temporada que no existe
    raise ValueError("Temporada no válida")
