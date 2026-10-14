#BEBIDAS

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


#Carta de bebidas
def mostrarBebidas():
    print()
    print("----- BEBIDAS -----")
    numero = 1
    for nombre in bebidas:
        print(f"{numero:>2}. {nombre:<20}{bebidas[nombre]:>6.2f} €")
        numero = numero + 1