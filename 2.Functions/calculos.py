#CALCULO DEL PRECIO DE UNA PIZZA E IVA

from gastos import gasto_suministros_por_pizza, gasto_personal_mensual, gasto_alquiler_mensual, iva
from Margenes import margen_beneficio_pizza
from temporadaPrevision import obtenerPizzasEstimadas


#reparte los gastos fijos del mes (personal + alquiler) entre las pizzas que se esperan vender
def calcularCosteFijoPorPizza(temporada):
    gastos_fijos_mensuales = gasto_personal_mensual + gasto_alquiler_mensual
    pizzas_estimadas_mes = obtenerPizzasEstimadas(temporada)
    coste_fijo_por_pizza = gastos_fijos_mensuales / pizzas_estimadas_mes
    return coste_fijo_por_pizza


#a partir del coste de los ingredientes calcula todos los pasos del precio
#devuelve un diccionario con cada parte, para poder mostrar el desglose
def calcularDesglosePrecio(coste_ingredientes, temporada):
    coste_fijo_por_pizza = calcularCosteFijoPorPizza(temporada)

    coste_total_pizza = coste_ingredientes + gasto_suministros_por_pizza + coste_fijo_por_pizza
    precio_sin_iva = coste_total_pizza * margen_beneficio_pizza
    precio_con_iva = round(precio_sin_iva * (1 + iva), 2)

    desglose = {
        "coste_ingredientes": coste_ingredientes,
        "suministros": gasto_suministros_por_pizza,
        "coste_fijo": coste_fijo_por_pizza,
        "coste_total": coste_total_pizza,
        "beneficio": precio_sin_iva - coste_total_pizza,
        "precio_sin_iva": precio_sin_iva,
        "iva": precio_con_iva - precio_sin_iva,
        "precio_con_iva": precio_con_iva
    }
    return desglose


#separa un importe con IVA incluido en base imponible + IVA
#devuelve una tupla (base_imponible, importe_iva)
def desglosarIva(total_con_iva):
    base_imponible = round(total_con_iva / (1 + iva), 2)
    importe_iva = round(total_con_iva - base_imponible, 2)
    return base_imponible, importe_iva