#calculos version 2

#gastos, iva y margen de la pizzeria
#(cuando existan gastos2, margenes2 y temporada2 se pueden coger de ahi)
SUMINISTROS_POR_PIZZA = 0.60
PERSONAL_MENSUAL = 4200
ALQUILER_MENSUAL = 1600
IVA = 0.10
MARGEN_BENEFICIO = 1.35

#pizzas que se venden al mes segun la temporada
PIZZAS_ESTIMADAS = {
    "baja": 600,
    "media": 1000,
    "alta": 1500
}


class Calculadora:
    #la calculadora guarda los gastos, el iva y el margen con los que calcula
    def __init__(self, suministrosPorPizza=SUMINISTROS_POR_PIZZA, personalMensual=PERSONAL_MENSUAL,
                 alquilerMensual=ALQUILER_MENSUAL, iva=IVA, margen=MARGEN_BENEFICIO,
                 pizzasEstimadas=PIZZAS_ESTIMADAS):
        self.suministrosPorPizza = suministrosPorPizza
        self.personalMensual = personalMensual
        self.alquilerMensual = alquilerMensual
        self.iva = iva
        self.margen = margen
        self.pizzasEstimadas = pizzasEstimadas

    #pizzas que se venden al mes en esa temporada
    def pizzasDelMes(self, temporada):
        if temporada not in self.pizzasEstimadas:
            raise ValueError("Temporada no válida")
        return self.pizzasEstimadas[temporada]

    #gastos fijos (personal + alquiler) que le tocan a cada pizza
    def costeFijoPorPizza(self, temporada):
        gastosFijos = self.personalMensual + self.alquilerMensual
        return gastosFijos / self.pizzasDelMes(temporada)

    #lo que nos cuesta hacer la pizza
    def costeTotal(self, costeIngredientes, temporada):
        return costeIngredientes + self.suministrosPorPizza + self.costeFijoPorPizza(temporada)

    #aplica el margen de beneficio al coste
    def precioSinIva(self, costeTotal):
        return costeTotal * self.margen

    #suma el iva al precio y lo redondea a 2 decimales
    def precioConIva(self, precioSinIva):
        return round(precioSinIva * (1 + self.iva), 2)

    #todo seguido: de coste de ingredientes a precio final
    def precioFinal(self, costeIngredientes, temporada):
        coste = self.costeTotal(costeIngredientes, temporada)
        return self.precioConIva(self.precioSinIva(coste))

    #separa el total en base imponible e iva
    def separarIva(self, total):
        baseImponible = round(total / (1 + self.iva), 2)
        importeIva = round(total - baseImponible, 2)
        return baseImponible, importeIva


#calculadora que usa el resto del programa (por ejemplo el ticket)
calculadora = Calculadora()
