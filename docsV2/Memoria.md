# Memoria – Versión 2 (clases y objetos)

La versión 2 hace lo mismo que la versión 1 (calcular el precio de las pizzas, el carrito, las ofertas y el ticket con el IVA separado), pero escrita con clases y objetos en vez de funciones sueltas. Al arrancar el programa se puede elegir qué versión usar. La versión 1 se ha dejado tal cual en "srcV1" y la versión 2 está en "srcV2".


Preparación "02/11/2026" y "04/11/2026"

    1.Se ha reorganizado el repositorio para que convivan las dos versiones: el código de la versión 1 se ha movido de "src" a "srcV1" y la documentación de "docs" a "docsV1". El 04/11 se arreglaron los imports de la versión 1 para que usen "srcV1".
    2.Se ha creado la rama "version2" como rama principal de la versión 2, y una rama "version2_src_..." para cada parte del programa. Cada parte se hace en su rama y, cuando está lista, se junta con "version2". A "main" no se pasa nada hasta que la versión 2 esté terminada y revisada.


Dia 1 "09/11/2026"

    1.Se ha hecho la clase Ticket ("ticket2.py"). Recibe el carrito, la temporada, el día y las ofertas, y su método mostrar() imprime el ticket y devuelve el total. Se ha cambiado para que los importes salgan siempre con 2 decimales.
    2.Se ha hecho la clase Calculadora ("calculos2.py") con los mismos cálculos que la versión 1: coste fijo por pizza, coste total, precio sin IVA, precio con IVA y separar el IVA del total.
    3.Pau ha hecho la clase Temporada ("temporada.py") con tres objetos: baja (600 pizzas al mes), media (1000) y alta (1500).
    4.Se ha hecho la clase Ingrediente ("ingredientes2.py"), con el nombre, el precio por kg y un método para saber cuánto cuestan unos gramos.
    5.Problemas que hemos tenido:
        - Al subir la rama del ticket se hizo el Pull Request contra "main" en vez de contra "version2", y se juntó sin querer (Pull Request #7). Como "main.py" todavía importaba "src", que ya no existía, el programa de "main" dejó de funcionar. Lo dejamos así hasta pasar la versión 2 completa a "main", que lo arreglará.
        - Al subir la rama de ingredientes, Git rechazó el push de "version2" porque Pau había subido la temporada mientras tanto. Aprendimos a hacer "git pull" de "version2" antes de subirla para juntar los cambios de los dos.


Dia 2 "10/11/2026"

    1.Se ha hecho la clase Pizza ("pizzas2.py"). Cada pizza tiene su nombre y su receta, y sabe calcular su coste de ingredientes, su precio según la temporada y mostrar el desglose del precio.
    2.Se ha hecho la clase Bebida ("bebidas2.py"). Tiene los mismos métodos que Pizza, precio(temporada) y nombreTicket(), aunque la bebida siempre cuesta lo mismo. Así el carrito y el ticket pueden tratar igual las pizzas y las bebidas, sin preguntar qué es cada producto.
    3.Se ha hecho la clase Carrito ("carrito2.py"). En la versión 1 el carrito era una lista que se pasaba a todas las funciones. Ahora es un objeto que guarda sus productos y tiene métodos para añadir, quitar, vaciar, contar y sumar.
    4.Se ha hecho la clase Ofertas ("ofertas2.py") con las 4 ofertas de la versión 1. Los números de las ofertas (las pizzas del 2x1, el euro del menú, el día y el porcentaje del descuento, el mínimo del pedido) se guardan como atributos, así que se pueden cambiar sin tocar el código.
    5.Se ha hecho la clase Caja ("menu2.py"), que es el menú. Guarda el carrito, la temporada, el día y las ofertas, y tiene un método para cada opción del menú.
    6.Se ha cambiado "main.py" para que pregunte al principio si se quiere usar la versión 1 o la versión 2.
    7.Se han arreglado las pruebas de la versión 1, que todavía importaban de "src", y una prueba de la temporada que esperaba un resultado que el código no da.
    8.Se ha cambiado la Calculadora para que use la clase Temporada de Pau en vez de tener las 600, 1000 y 1500 pizzas repetidas.
    9.Se han hecho las clases Gastos ("gastos2.py") y Margen ("margenes2.py"), que eran las dos piezas de la versión 1 que todavía no tenían archivo en la versión 2. Antes sus números estaban dentro de la Calculadora; ahora la Calculadora recibe un objeto Gastos y un objeto Margen.
    10.Se ha actualizado el README con las dos versiones, las clases de la versión 2 y cómo lanzar las pruebas. También se ha escrito en "docsV2/Resumen_funciones_version2.md" un log con lo que se ha hecho en cada rama, junto con el de la temporada de Pau.
    11.Pruebas: cada clase de la versión 2 tiene su archivo de pruebas, y muchas pruebas comparan el resultado con la versión 1 para asegurarnos de que las dos dan los mismos precios. Por ejemplo, las ofertas se prueban con 300 carritos al azar. También hay pruebas que simulan a una persona usando el menú. En total pasan 56 pruebas, que se lanzan todas con: python -m unittest discover -s tests -t .



Dia 3 "13/11/2026"

    1.Al revisar el tablero de Trello de la versión 2 vimos que las tarjetas pedían un diseño orientado a objetos más completo que el que teníamos: herencia, clases abstractas, encapsulación con @property y excepciones propias. Primero clasificamos las 20 tarjetas que estaban en "Pendiente" según lo que ya estaba hecho (5 terminadas, 3 en revisión, 8 en proceso y 3 sin empezar), haciendo capturas al principio, a mitad y al final.
    2.Se han hecho las excepciones propias ("excepciones2.py"): PizzeriaError y sus subclases ProductoNoEncontradoError, IngredienteNoEncontradoError, CantidadNoValidaError y PrecioNoValidoError. La Caja las captura con try/except, enseña el mensaje y sigue funcionando. El Ingrediente se ha encapsulado con @property y su precio no puede ser negativo.
    3.Se ha hecho la clase base abstracta Producto ("producto2.py"). Pizza y Bebida heredan de ella y cada una sobrescribe precioSinIva() a su manera: la pizza lo calcula con sus ingredientes y gastos, y la bebida lo saca de su precio de carta. Así el carrito y el ticket tratan igual a todos los productos (polimorfismo).
    4.Se ha hecho la clase LineaCarrito: el carrito ya no guarda los productos sueltos, sino líneas con el producto y su cantidad. Si se añade un producto que ya está, se suma a su línea.
    5.Se ha hecho la clase Menu ("menus2.py"), que también hereda de Producto y contiene otros productos: el menú pizza + bebida (1 € menos) y el menú familiar con 2 pizzas y 2 bebidas (5 € menos). Se piden con la opción 11 de la caja.
    6.Se han separado las ofertas en una jerarquía: una clase base abstracta Oferta y una subclase por oferta (Oferta2x1, OfertaMenu, OfertaDiaSemana, OfertaTemporada y OfertaPedidoGrande). Se ha añadido una oferta nueva: en temporada baja, 10% de descuento en las bebidas.
    7.Se han actualizado las tarjetas de Trello con lo que se ha hecho, el README (con un diagrama de clases y una explicación de dónde se usa la herencia, el polimorfismo y la encapsulación) y esta memoria. En total pasan 82 pruebas.
    8.Decisión: la bebida mantiene el precio fijo de carta con el IVA incluido, como en la versión 1, en vez de "precio de compra + margen" como ponía la tarjeta de Trello. Así los precios de las bebidas son los mismos en las dos versiones y el criterio es el que ya explicábamos en el README.

Qué hemos aprendido con la versión 2

    1.Una clase junta los datos y lo que se puede hacer con ellos. En la versión 1, para saber el precio de una pizza había que llamar a calcularPrecioPizza("Margarita", temporada). En la versión 2 la pizza lo sabe calcular sola: pizzas["Margarita"].precio(temporada).
    2.Si dos clases tienen los mismos métodos (como Pizza y Bebida), el resto del programa las puede usar igual sin saber cuál es cuál. Esto ha hecho el carrito y el ticket más sencillos.
    3.Guardar los números en atributos (en los Gastos, el Margen y las Ofertas) permite crear objetos con otros valores, por ejemplo Calculadora(gastos=Gastos(iva=0.21)) u Ofertas([OfertaDiaSemana(Oferta2x1(), dia="lunes")]), sin cambiar el código. Además, un objeto puede usar otros: la Calculadora usa un objeto Gastos, un objeto Margen y las Temporadas.
    4.La herencia evita repetir código: Producto tiene una sola vez lo que comparten todos los productos (precio con IVA, IVA, nombre en el ticket), y cada subclase solo escribe lo que la hace distinta. Con las clases abstractas Python no deja olvidarse de escribir ese método.
    5.Hacer una rama por cada parte, con su commit y juntándola con "version2" en cuanto está lista, ha funcionado mucho mejor que en la versión 1, donde lo juntamos todo al final. Hay que fijarse bien en la rama de destino de los Pull Requests ("version2" y no "main").
