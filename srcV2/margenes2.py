#margenes version 2


class Margen:
    #margen de beneficio
    #1.35 = ganamos un 35% sobre lo que nos cuesta hacer la pizza
    def __init__(self, beneficio=1.35):
        self.beneficio = beneficio

    #aplica el margen al coste
    def aplicar(self, coste):
        return coste * self.beneficio

    #el margen en porcentaje (1.35 -> 35)
    def porcentaje(self):
        return round((self.beneficio - 1) * 100)

    def __str__(self):
        return f"Margen de beneficio: {self.porcentaje()}%"


#margen que usa el resto del programa
margen = Margen()
