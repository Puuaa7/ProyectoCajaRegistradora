#bebidas con su precio
#el precio es fijo y ya lleva el iva incluido
bebidas = {
    "agua": 1.20,
    "cola": 2.00,
    "colaZero": 2.00,
    "limonada": 2.00,
    "naranja": 2.00,
    "teFrio": 2.20,
    "cerveza": 2.50,
    "cervezaSinAlcohol": 2.50
}


def mostrarBebidas():
    print("")
    print("--- BEBIDAS ---")
    for nombre in bebidas:
        print(nombre, "-", bebidas[nombre], "€")
