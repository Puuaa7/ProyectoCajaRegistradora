#gastos version 2


class Gastos:
    #gastos de la pizzeria
    #suministros: luz, gas, agua, horno, cajas... por cada pizza
    #personal y alquiler: lo que se paga cada mes
    #iva: iva de hosteleria (10%)
    def __init__(self, suministrosPorPizza=0.60, personalMensual=4200, alquilerMensual=1600, iva=0.10):
        self.suministrosPorPizza = suministrosPorPizza
        self.personalMensual = personalMensual
        self.alquilerMensual = alquilerMensual
        self.iva = iva

    #gastos fijos de cada mes (personal + alquiler)
    def gastosFijosMensuales(self):
        return self.personalMensual + self.alquilerMensual

    def __str__(self):
        return (f"Suministros: {self.suministrosPorPizza:.2f} €/pizza - Personal: {self.personalMensual} €/mes"
                f" - Alquiler: {self.alquilerMensual} €/mes - IVA: {round(self.iva * 100)}%")


#gastos que usa el resto del programa
gastos = Gastos()
