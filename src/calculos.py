from src.gastos import (
    gasto_suministros_por_pizza,
    gasto_personal_mensual,
    gasto_alquiler_mensual,
    iva,
)
from src.pizzas import calcularPrecioPizza
from src.temporada import obtener_pizzas_estimadas


def calcular_precio_venta(nombre_pizza, temporada="media"):
    coste_ingredientes = calcularPrecioPizza(nombre_pizza)
    pizzas_estimadas_mes = obtener_pizzas_estimadas(temporada)
    gastos_fijos_mensuales = gasto_personal_mensual + gasto_alquiler_mensual
    coste_fijo_por_pizza = gastos_fijos_mensuales / pizzas_estimadas_mes
    coste_total_pizza = coste_ingredientes + gasto_suministros_por_pizza + coste_fijo_por_pizza
    precio_sin_iva = coste_total_pizza * 1.35
    precio_con_iva = precio_sin_iva * (1 + iva)
    return {
        "coste_ingredientes": round(coste_ingredientes, 2),
        "coste_total": round(coste_total_pizza, 2),
        "precio_sin_iva": round(precio_sin_iva, 2),
        "iva": round(precio_con_iva - precio_sin_iva, 2),
        "precio_con_iva": round(precio_con_iva, 2),
    }
