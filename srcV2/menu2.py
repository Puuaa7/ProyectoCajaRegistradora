#menu version 2

#date sirve para saber el dia de hoy
from datetime import date

from srcV2.temporada import temporadas
from srcV2.pizzas2 import mostrarPizzas, buscarPizza
from srcV2.bebidas2 import mostrarBebidas
from srcV2.carrito2 import Carrito
from srcV2.ofertas2 import ofertas
from srcV2.ticket2 import Ticket
from srcV2.excepciones2 import PizzeriaError

#dias validos (tupla porque no cambian)
diasSemana = ("lunes", "martes", "miercoles", "jueves", "viernes", "sabado", "domingo")

#nombres de las temporadas ("baja", "media", "alta")
nombresTemporadas = tuple(temporada.nombre for temporada in temporadas)


class Caja:
    #la caja guarda el carrito, la temporada, el dia y las ofertas
    def __init__(self, temporada, dia, ofertas=ofertas):
        self.carrito = Carrito()
        self.temporada = temporada
        self.dia = dia
        self.ofertas = ofertas

    #imprime las opciones del menu principal
    def mostrarMenu(self):
        print("")
        print("----- PIZZERIA PYTHON (v2) -----")
        print("Temporada:", self.temporada, "- Dia:", self.dia)
        print("1. Ver pizzas")
        print("2. Ver bebidas")
        print("3. Ver ofertas")
        print("4. Añadir producto")
        print("5. Quitar producto")
        print("6. Ver carrito")
        print("7. Pagar y ver ticket")
        print("8. Ver como se calcula el precio de una pizza")
        print("9. Cambiar temporada")
        print("10. Cambiar dia")
        print("0. Salir")

    def verOfertas(self):
        self.ofertas.mostrarDisponibles()
        if not self.carrito.estaVacio():
            print("")
            print("Ofertas de tu pedido:")
            self.ofertas.mostrarDescuentos(self.carrito, self.temporada, self.dia)

    def anadirProducto(self):
        producto = input("Que quieres añadir? ")
        #si la cantidad no es un entero mayor que 0, el carrito lanza CantidadNoValidaError
        cantidad = input("Cuantas? ")
        self.carrito.agregar(producto, cantidad)

    def quitarProducto(self):
        self.carrito.quitar(input("Que quieres quitar? "))

    def verCarrito(self):
        self.carrito.mostrar(self.temporada)
        self.ofertas.mostrarDescuentos(self.carrito, self.temporada, self.dia)

    def pagar(self):
        total = Ticket(self.carrito, self.temporada, self.dia, self.ofertas).mostrar()
        #si se ha pagado, vaciamos el carrito
        if total > 0:
            self.carrito.vaciar()

    def verDesglose(self):
        pizza = buscarPizza(input("Que pizza? "))
        if pizza is None:
            print("Esa pizza no existe")
        else:
            pizza.mostrarDesglose(self.temporada)

    #bucle principal de la caja: muestra el menu y ejecuta la opcion elegida
    def iniciar(self):
        while True:
            self.mostrarMenu()
            opcion = input("Elige una opcion: ").strip()
            #si una opcion lanza un error de la pizzeria, se muestra y la caja sigue
            try:
                seguir = self.ejecutarOpcion(opcion)
            except PizzeriaError as error:
                print("Error:", error, "- no se ha hecho nada")
                seguir = True
            if not seguir:
                break

    #ejecuta una opcion del menu; devuelve False cuando hay que salir
    def ejecutarOpcion(self, opcion):
        if opcion == "1":
            mostrarPizzas(self.temporada)
        elif opcion == "2":
            mostrarBebidas()
        elif opcion == "3":
            self.verOfertas()
        elif opcion == "4":
            self.anadirProducto()
        elif opcion == "5":
            self.quitarProducto()
        elif opcion == "6":
            self.verCarrito()
        elif opcion == "7":
            self.pagar()
        elif opcion == "8":
            self.verDesglose()
        elif opcion == "9":
            self.temporada = pedirTemporada()
        elif opcion == "10":
            self.dia = pedirDia()
        elif opcion == "0":
            print("Adios!")
            return False
        else:
            print("Opcion incorrecta")
        return True


#pide la temporada hasta que sea valida
def pedirTemporada():
    temporada = input("Temporada (baja, media o alta): ").lower().strip()
    while temporada not in nombresTemporadas:
        print("Esa temporada no existe")
        temporada = input("Temporada (baja, media o alta): ").lower().strip()
    return temporada


#pide el dia hasta que sea valido
def pedirDia():
    dia = input("Que dia es hoy? ").lower().strip()
    while dia not in diasSemana:
        print("Ese dia no existe")
        dia = input("Que dia es hoy? ").lower().strip()
    return dia


#arranca la caja de la version 2 (lo llama main.py)
def iniciarCaja():
    temporada = pedirTemporada()
    #dia de hoy (weekday da 0 el lunes, 1 el martes...)
    dia = diasSemana[date.today().weekday()]
    Caja(temporada, dia).iniciar()
