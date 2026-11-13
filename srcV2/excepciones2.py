#excepciones propias version 2
#son clases que heredan de Exception, asi podemos lanzar errores con nombre propio
#y controlarlos con try/except sin que el programa se cierre


class PizzeriaError(Exception):
    #error base de la pizzeria: todas las demas excepciones heredan de esta,
    #asi la caja puede capturarlas todas con un solo except PizzeriaError
    pass


class ProductoNoEncontradoError(PizzeriaError):
    #se pide un producto (pizza o bebida) que no esta en la carta
    def __init__(self, texto):
        super().__init__(f"El producto '{texto}' no existe")
        self.texto = texto


class IngredienteNoEncontradoError(PizzeriaError):
    #una receta usa un ingrediente que no esta en el catalogo
    def __init__(self, nombre):
        super().__init__(f"El ingrediente '{nombre}' no existe")
        self.nombre = nombre


class CantidadNoValidaError(PizzeriaError):
    #la cantidad es cero, negativa o no es un numero entero
    def __init__(self, cantidad):
        super().__init__(f"La cantidad '{cantidad}' no es válida: tiene que ser un número entero mayor que 0")
        self.cantidad = cantidad


class PrecioNoValidoError(PizzeriaError):
    #un precio o un descuento negativo
    def __init__(self, precio):
        super().__init__(f"El precio {precio} no es válido: no puede ser negativo")
        self.precio = precio


#convierte lo que escribe el usuario en una cantidad entera mayor que 0
#si no se puede, lanza CantidadNoValidaError
def leerCantidad(cantidad):
    if isinstance(cantidad, bool):
        raise CantidadNoValidaError(cantidad)
    if isinstance(cantidad, int):
        numero = cantidad
    else:
        texto = str(cantidad).strip()
        if not (texto.isascii() and texto.isdigit()):
            raise CantidadNoValidaError(cantidad)
        numero = int(texto)
    if numero <= 0:
        raise CantidadNoValidaError(cantidad)
    return numero
