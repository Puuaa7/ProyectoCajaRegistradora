from src.pizzas import pizzas
from src.calculos import calcular_precio_venta
# OFERTAS DE LA PIZZERIA

# Oferta 1: Pizza + bebida
# Mirar si el cliente ha pedido una pizza y una bebida
# Si tiene las dos cosas, hacer un descuento


# Oferta 2: 2x1 en pizzas
# Comprobar si el cliente ha pedido 2 pizzas de la oferta
# Si las dos entran en la oferta, solo paga una
# Si tienen precios diferentes, paga la mas cara
# Si no entran en la oferta, paga las dos


# Oferta 3: Descuento del 10%
# Mirar si el pedido supera los 30 euros
# Si los supera, descontar un 10% del precio


# Aplicar ofertas
# Crear una funcion para mirar las ofertas disponibles
# Comprobar si el carrito cumple alguna oferta
# Calcular el descuento
# Devolver el precio con el descuento


# Tener en cuenta
# No aplicar el mismo descuento dos veces
# Mostrar el descuento en el ticket
# Calcular el IVA con el precio despues del descuento


from src.calculos import calcular_precio_venta

# Pizzas que entran en el 2x1
pizzas_oferta = ["Margarita", "Prosciutto", "Barbacoa"]


def oferta_2x1(carrito, temporada="media"):
    pizzas_en_oferta = []

    # Buscar las pizzas del carrito que entran en la oferta
    for pizza in carrito:
        if pizza in pizzas_oferta:
            pizzas_en_oferta.append(pizza)

    # Comprobar si hay al menos 2 pizzas
    if len(pizzas_en_oferta) >= 2:

        precios = []

        # Calcular los precios de las pizzas
        for pizza in pizzas_en_oferta:
            precio = calcular_precio_venta(pizza, temporada)["precio_con_iva"]
            precios.append(precio)

        # Si hay 2 pizzas, la mas barata sale gratis
        # Si hay mas, se aplica un 2x1 por cada pareja
        precios.sort(reverse=True)

        descuento = 0

        for i in range(1, len(precios), 2):
            descuento = descuento + precios[i]

        return round(descuento, 2)

    else:
        return 0



#para la oferta 2x1, devolver el precio de la pizza mas cara
# def oferta_2x1(precio1, precio2):
#     if precio1 > precio2:
#         return precio1
#     else:
#         return precio2



#descuento del 10% si el total supera los 30 euros
def descuento_10(total):
    if total > 30:
        return total * 0.9
    else:
        return total