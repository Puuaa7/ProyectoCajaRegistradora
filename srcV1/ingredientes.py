#ingredientes y sus precios por kg
ingredientes = {
    "harina": 1.00,
    "tomate": 2.00,
    "mozzarella": 10.00,
    "jamon": 14.00,
    "bacon": 11.00,
    "pollo": 8.00,
    "atun": 12.00,
    "champinones": 4.00,
    "cebolla": 1.50,
    "aceitunas": 6.00,
    "pepperoni": 15.00,
    "chocolateDubai": 25.00,
    "platano": 2.00,
    "piña": 3.00,
    "parmesano": 20.00,
    "quesoDeCabra": 16.00,
    "burrata": 14.00,
    "rucula": 12.00,
    "pesto": 14.00,
    "pimientos": 3.00,
    "miel": 10.00,
    "trufa": 800.00,
    "huevo": 4.00,
    "salchicha": 9.00,
    "salsaBarbacoa": 5.00,
    "salsaAjo": 5.00,
    "quesoAzul": 15.00,
    "gorgonzola": 18.00,
    "olivasNegras": 6.00,
    "olivasVerdes": 6.00,
    "pimientosRojos": 3.00,
    "pimientosVerdes": 3.00,
    "pimientosAmarillos": 3.00,
    "pimientosPicantes": 5.00,
    "tomateSeco": 18.00,
    "cebollaCaramelizada": 8.00,
    "espinacas": 5.00,
    "alcachofas": 7.00,
    "maiz": 4.00,
    "brocoli": 3.00,
    "calabacin": 2.50,
    "berenjena": 3.00,
    "oregano": 25.00,
    "albahaca": 18.00,
    "romero": 18.00,
    "tomillo": 20.00,
    "huevosDeCodorniz": 8.50,
    "huevoDuro": 4.00,
    "salsaRosa": 5.00,
    "mozzarellaDiBufala": 16.00
}



#funcion para calcular el coste de los ingredientes de una pizza por gramo
def calcularPrecioIngrediente(ingrediente, gramos):
    precioKg = ingredientes[ingrediente]
    precio = precioKg * (gramos / 1000)
    return round(precio, 2)