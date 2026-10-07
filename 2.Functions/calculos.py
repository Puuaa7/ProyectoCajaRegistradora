#Cálculo del precio de una pizza


gastos_fijos_mensuales = gasto_personal_mensual + gasto_alquiler_mensual
coste_fijo_por_pizza = gastos_fijos_mensuales / pizzas_estimadas_mes
coste_total_pizza = coste_ingredientes + gasto_suministros_por_pizza +
coste_fijo_por_pizza
precio_sin_iva = coste_total_pizza * 1.35
precio_con_iva = precio_sin_iva * (1 + iva)

