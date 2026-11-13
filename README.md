# Caja registradora de una pizzería

Programa en Python que simula la caja registradora de una pizzería. Calcula el precio de las pizzas a partir de los ingredientes y los gastos del negocio, deja añadir pizzas y bebidas a un carrito, aplica ofertas y muestra un ticket con el IVA separado.

## Cómo se usa

```
python main.py
```

Al arrancar, el programa pregunta qué versión quieres usar:

```
----- CAJA REGISTRADORA PIZZERIA -----
1. Version 1 (funciones)
2. Version 2 (clases y objetos)
Que version quieres usar?
```

Las dos versiones calculan los mismos precios de pizzas y bebidas. La diferencia principal está en cómo está escrito el código, y la versión 2 añade los menús, una oferta de temporada y excepciones propias:

- **Versión 1** (`srcV1/`): funciones sueltas y datos en diccionarios y listas.
- **Versión 2** (`srcV2/`): clases y objetos. Cada cosa de la pizzería (ingrediente, pizza, bebida, carrito, ofertas, ticket, caja) es una clase con sus datos y sus métodos.

## Estructura del proyecto

```
main.py                  -> pregunta la versión y arranca el programa
srcV1/                   -> versión 1 (funciones)
  ingredientes.py        -> ingredientes y su precio por kg
  pizzas.py              -> las 21 pizzas con los gramos de cada ingrediente
  gastos.py              -> suministros, personal, alquiler e IVA
  margenes.py            -> margen de beneficio
  temporada.py           -> pizzas que se venden al mes según la temporada
  calculos.py            -> cálculo del precio de una pizza y del IVA
  bebidas.py             -> carta de bebidas
  carrito.py             -> añadir, quitar y ver productos del carrito
  ofertas.py             -> las 4 ofertas
  ticket.py              -> ticket final
  menu.py                -> menú de la caja
srcV2/                   -> versión 2 (clases)
  excepciones2.py        -> excepciones propias (PizzeriaError y sus subclases)
  ingredientes2.py       -> clase Ingrediente
  producto2.py           -> clase base abstracta Producto
  pizzas2.py             -> clase Pizza (hereda de Producto)
  bebidas2.py            -> clase Bebida (hereda de Producto)
  menus2.py              -> clase Menu (hereda de Producto): pizza + bebida y familiar
  temporada.py           -> clase Temporada
  gastos2.py             -> clase Gastos (suministros, personal, alquiler e IVA)
  margenes2.py           -> clase Margen (margen de beneficio)
  calculos2.py           -> clase Calculadora
  carrito2.py            -> clases Carrito y LineaCarrito
  ofertas2.py            -> clase base Oferta, sus 5 subclases y la clase Ofertas
  ticket2.py             -> clase Ticket
  menu2.py               -> clase Caja (menú de la caja)
tests/                   -> pruebas de las dos versiones
docsV1/                  -> memoria y enunciado de la versión 1
docsV2/                  -> notas de la versión 2
```

## Versión 1: funciones

### Estructuras de datos

- **Diccionarios**: `ingredientes` (ingrediente → precio por kg), `pizzas` (pizza → diccionario de ingrediente → gramos), `bebidas` (bebida → precio) y el que devuelve `contarProductos` (producto → cantidad).
- **Listas**: el `carrito` (por ejemplo `["Margarita", "Margarita", "cola"]`) y la lista de descuentos que se aplican.
- **Tuplas**: `temporadas` y `diasSemana`, que no cambian nunca. Cada descuento también es una tupla `(nombre, dinero)`.
- **Conjuntos**: `pizzas_2x1`, las pizzas que entran en el 2x1.

### Funciones

| Archivo | Funciones |
|---|---|
| ingredientes.py | `calcularPrecioIngrediente` |
| pizzas.py | `calcularCosteIngredientes`, `calcularPrecioPizza`, `mostrarPizzas`, `mostrarDesglosePizza` |
| temporada.py | `obtenerPizzasEstimadas` |
| calculos.py | `calcularCosteFijoPorPizza`, `calcularCosteTotal`, `calcularPrecioSinIva`, `calcularPrecioConIva`, `separarIva` |
| bebidas.py | `mostrarBebidas` |
| carrito.py | `buscarProducto`, `esPizza`, `esBebida`, `obtenerPrecioProducto`, `agregarProductoCarrito`, `quitarProductoCarrito`, `contarProductos`, `calcularTotalCarrito`, `mostrarCarrito` |
| ofertas.py | `ofertaDosPorUno`, `ofertaMenu`, `ofertaMartes`, `ofertaMasDe30`, `aplicarOferta`, `mostrarDescuentosCarrito`, `mostrarOfertasDisponibles` |
| ticket.py | `mostrarTicket` |
| menu.py | `mostrarMenu`, `pedirTemporada`, `pedirDia`, `iniciarCaja` |

## Versión 2: clases

### Diagrama de clases

```
Herencia:

Producto (abstracta)        Oferta (abstracta)          PizzeriaError (Exception)
 ├── Pizza                   ├── Oferta2x1               ├── ProductoNoEncontradoError
 ├── Bebida                  ├── OfertaMenu              ├── IngredienteNoEncontradoError
 └── Menu                    ├── OfertaDiaSemana         ├── CantidadNoValidaError
                             ├── OfertaTemporada         └── PrecioNoValidoError
                             └── OfertaPedidoGrande

Composición (un objeto tiene o usa otros):

Pizza ──> Ingrediente               Menu ──> Producto (sus pizzas y bebidas)
Carrito ──> LineaCarrito ──> Producto
Calculadora ──> Gastos, Margen y Temporada
Caja ──> Carrito, Ofertas y Ticket
```

### Clases

| Archivo | Clase | Atributos | Métodos |
|---|---|---|---|
| excepciones2.py | `PizzeriaError` y subclases | mensaje del error | — |
| ingredientes2.py | `Ingrediente` | `nombre`, `precioKg` (con `@property`, el precio no puede ser negativo) | `precio(gramos)` |
| producto2.py | `Producto` (abstracta) | `nombre` | `precioSinIva()` (abstracto), `precio()`, `iva()`, `nombreTicket()` |
| pizzas2.py | `Pizza(Producto)` | `nombre`, `receta` (objetos `Ingrediente` y sus gramos) | `costeIngredientes()`, `costeTotal()`, `precioSinIva()`, `mostrarDesglose()` |
| bebidas2.py | `Bebida(Producto)` | `nombre`, `precioFijo` | `precioSinIva()`, `precio()` |
| menus2.py | `Menu(Producto)` | `nombre`, `productos`, `descuento` | `precioPorSeparado()`, `precio()`, `precioSinIva()`, `nombreTicket()` |
| temporada.py | `Temporada` | `nombre`, `pizzasEstimadas` | `obtenerPizzasEstimadas()` |
| gastos2.py | `Gastos` | `suministrosPorPizza`, `personalMensual`, `alquilerMensual`, `iva` | `gastosFijosMensuales()` |
| margenes2.py | `Margen` | `beneficio` | `aplicar(coste)`, `porcentaje()` |
| calculos2.py | `Calculadora` | `gastos` (objeto `Gastos`), `margen` (objeto `Margen`) | `pizzasDelMes`, `costeFijoPorPizza`, `costeTotal`, `precioSinIva`, `precioConIva`, `precioFinal`, `separarIva` |
| carrito2.py | `LineaCarrito` | `producto`, `cantidad` | `subtotal(temporada)` |
| carrito2.py | `Carrito` | `lineas` (objetos `LineaCarrito`) | `agregar`, `agregarProducto`, `quitar`, `vaciar`, `estaVacio`, `pizzas`, `bebidas`, `contarProductos`, `total`, `baseImponible`, `iva`, `mostrar` |
| ofertas2.py | `Oferta` (abstracta) | `nombre` | `calcular()` (abstracto), `descripcion()` (abstracto), `esAplicable()` |
| ofertas2.py | `Oferta2x1`, `OfertaMenu`, `OfertaDiaSemana`, `OfertaTemporada`, `OfertaPedidoGrande` | los datos de cada oferta | sobrescriben `calcular()` y `descripcion()` |
| ofertas2.py | `Ofertas` | `lista` (objetos `Oferta`) | `aplicar(carrito, temporada, dia)`, `mostrarDescuentos`, `mostrarDisponibles` |
| ticket2.py | `Ticket` | `carrito`, `temporada`, `dia`, `ofertas` | `mostrar()` |
| menu2.py | `Caja` | `carrito`, `temporada`, `dia`, `ofertas` | un método por opción del menú, `ejecutarOpcion()` e `iniciar()` |

Cada archivo crea también los objetos que usa el resto del programa: el diccionario `ingredientes` con un `Ingrediente` por ingrediente, `pizzas` con una `Pizza` por receta, `bebidas`, las temporadas `baja`, `media` y `alta`, y los objetos `gastos`, `margen`, `calculadora` y `ofertas`.

### Programación orientada a objetos en la versión 2

- **Herencia.** `Pizza`, `Bebida` y `Menu` heredan de `Producto`. Las cinco ofertas heredan de `Oferta`. Las excepciones heredan de `PizzeriaError`, que hereda de `Exception`.
- **Clases abstractas.** `Producto` y `Oferta` usan `abc`: no se pueden crear directamente y obligan a cada subclase a escribir su `precioSinIva()` o su `calcular()`.
- **Polimorfismo.** El carrito y el ticket llaman a `producto.precio(temporada)` sin saber si es una pizza (precio calculado), una bebida (precio fijo de carta) o un menú (suma con descuento). `Ofertas.aplicar()` recorre la lista llamando a `oferta.calcular()` sin saber qué oferta es.
- **Encapsulación.** Los atributos empiezan por `_` y se leen con `@property`. Los que se pueden cambiar tienen un *setter* que valida el dato: el precio de un ingrediente no puede ser negativo y la cantidad de una línea del carrito tiene que ser un entero mayor que 0.
- **Composición.** Una `Pizza` está hecha de objetos `Ingrediente`. Un `Menu` contiene otros productos. El `Carrito` tiene objetos `LineaCarrito`. La `Calculadora` usa un objeto `Gastos`, un `Margen` y las `Temporada`.
- **Excepciones propias.** Si se pide un producto que no existe o una cantidad no válida, se lanza `ProductoNoEncontradoError` o `CantidadNoValidaError`. La `Caja` las captura con `try/except PizzeriaError`, enseña el mensaje y sigue funcionando.

### Qué cambia respecto a la versión 1

- **Los datos van con su comportamiento.** En la v1 el precio de una pizza se calcula con `calcularPrecioPizza("Margarita", temporada)`. En la v2 la pizza sabe calcularlo: `pizzas["Margarita"].precio(temporada)`.
- **Menús como producto.** En la v2 se puede pedir un menú pizza + bebida o un menú familiar (opción 11 de la caja). En el ticket sale el menú con lo que lleva dentro.
- **Una oferta más.** En temporada baja hay un 10% de descuento en las bebidas (`OfertaTemporada`).
- **Los números se pueden cambiar sin tocar el código.** Por ejemplo, `Ofertas([OfertaDiaSemana(Oferta2x1(), dia="lunes")])` crea una lista de ofertas con descuento los lunes, y `Calculadora(gastos=Gastos(iva=0.21))` calcula con otro IVA.
- **Las temporadas son objetos.** Una temporada nueva como `Temporada("festival", 2900)` funciona sin cambiar nada más.
- **Los errores no cierran el programa.** Se controlan con excepciones propias.

## Ofertas

1. **2x1** en Margarita, Prosciutto y Hawaiana. Se pueden mezclar y la más barata sale gratis.
2. **Menú pizza + bebida**: 1 € de descuento por cada pizza con bebida. Las pizzas gratis del 2x1 no cuentan.
3. **Martes**: 20% de descuento en las pizzas (sin contar las que ya son gratis).
4. **Pedido de más de 30 €**: 10% de descuento. Se mira con el total después de las otras ofertas.
5. **Temporada baja** (solo en la versión 2): 10% de descuento en las bebidas.

El día se coge solo con la fecha del ordenador, pero se puede cambiar en el menú (opción 10) para probar la oferta del martes.

En la versión 2, además, se pueden pedir **menús**: el menú pizza + bebida (1 € menos) y el menú familiar con 2 pizzas y 2 bebidas (5 € menos). Las pizzas y bebidas de un menú ya tienen su descuento, así que no cuentan para el 2x1, la oferta de menú automática ni la del martes.

## Cómo se calcula el precio de una pizza

1. **Coste de ingredientes**: precio por kg × gramos que lleva la pizza / 1000, sumando todos los ingredientes.
2. **Suministros**: 0,60 € por pizza (luz, gas, agua, horno, cajas...).
3. **Gastos fijos**: (personal 4200 € + alquiler 1600 €) / pizzas que se venden al mes. Depende de la temporada: baja 600, media 1000 y alta 1500 pizzas.
4. **Coste total** = ingredientes + suministros + gastos fijos.
5. **Precio sin IVA** = coste total × 1,35. Ganamos un 35% sobre el coste. Elegimos el 35% porque es el que venía en el enunciado y los precios salen parecidos a los de una pizzería normal (entre 11 y 17 € en temporada media).
6. **Precio con IVA** = precio sin IVA × 1,10.

Ejemplo con la Margarita en temporada media:

```
Ingredientes: 1.65 €
Suministros: 0.6 €
Gastos fijos: 5.8 €
Coste total: 8.05 €
Beneficio: 2.82 €
Precio sin IVA: 10.87 €
IVA: 1.08 €
Precio final: 11.95 €
```

En temporada alta las pizzas salen más baratas, porque los gastos fijos se reparten entre más pizzas.

## Cómo se calcula el IVA

El IVA de la comida en hostelería es del **10%**. Los precios de la carta ya llevan el IVA. En el ticket se suma todo, se restan los descuentos y luego se separa el IVA del total:

- Base imponible = total / 1,10
- IVA = total − base imponible

Así el IVA se calcula con el precio después de los descuentos.

## Criterio de las bebidas

Las bebidas tienen un **precio fijo de carta con el IVA incluido**, como en cualquier bar (agua 1,20 €, refrescos 2 €, cerveza 2,50 €...). No las calculamos como las pizzas porque no se cocinan: solo se compran y se venden. En el ticket su IVA se separa igual que el de las pizzas.

## Ejemplo de ejecución

Pedido de 2 Margaritas, 1 Barbacoa y 2 colas un martes, en temporada media (versión 1; la versión 2 da el mismo total y muestra los importes siempre con 2 decimales):

```
PIZZERIA PYTHON

Productos:
- Pizza Margarita x2: 23.9 €
- Pizza Barbacoa x1: 14.12 €
- cola x2: 4.0 €

Descuentos:
- 2x1: -11.95 €
- Menu pizza + bebida: -2 €
- Martes 20% pizzas: -5.21 €

Base imponible: 20.78 €
IVA: 2.08 €
Total: 22.86 €

Gracias por su compra.
```

## Pruebas

Las pruebas están en la carpeta `tests/`. Para lanzarlas todas desde la carpeta del proyecto:

```
python -m unittest discover -s tests -t .
```

- `test_calculos.py` prueba la versión 1.
- Los `test_*2.py` prueban cada clase de la versión 2. Varios comparan sus resultados con la versión 1 para asegurarse de que las dos dan los mismos precios y descuentos (por ejemplo, `test_ofertas2.py` compara 300 carritos al azar).
- `test_producto2.py`, `test_menus2.py` y `test_excepciones2.py` prueban la herencia, el polimorfismo, la encapsulación y las excepciones propias.
- `test_menu2.py` y `test_main.py` simulan a una persona usando el menú.
