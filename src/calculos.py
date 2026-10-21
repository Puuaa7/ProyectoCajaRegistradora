#Cálculo del precio de una pizza

from src.gastos import gasto_suministros_por_pizza, gasto_personal_mensual, gasto_alquiler_mensual, iva
from src.margenes import margen_beneficio_pizza
from src.temporada import obtenerPizzasEstimadas


#gastos fijos (personal + alquiler) que le tocan a cada pizza
def calcularCosteFijoPorPizza(temporada):
    gastos_fijos_mensuales = gasto_personal_mensual + gasto_alquiler_mensual
    pizzas_estimadas_mes = obtenerPizzasEstimadas(temporada)
    coste_fijo_por_pizza = gastos_fijos_mensuales / pizzas_estimadas_mes
    return coste_fijo_por_pizza


#lo que nos cuesta hacer la pizza
def calcularCosteTotal(coste_ingredientes, temporada):
    coste_fijo_por_pizza = calcularCosteFijoPorPizza(temporada)
    coste_total_pizza = coste_ingredientes + gasto_suministros_por_pizza + coste_fijo_por_pizza
    return coste_total_pizza


def calcularPrecioSinIva(coste_total_pizza):
    precio_sin_iva = coste_total_pizza * margen_beneficio_pizza
    return precio_sin_iva


def calcularPrecioConIva(precio_sin_iva):
    precio_con_iva = precio_sin_iva * (1 + iva)
    return round(precio_con_iva, 2)


#separa el total en base imponible e iva
def separarIva(total):
    base_imponible = round(total / (1 + iva), 2)
    importe_iva = round(total - base_imponible, 2)
    return base_imponible, importe_iva
