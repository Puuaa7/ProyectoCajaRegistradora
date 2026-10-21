# Caja registradora de una pizzería

Programa en Python que simula la caja registradora de una pizzería. Calcula el precio de las pizzas a partir de los ingredientes y los gastos del negocio, deja añadir pizzas y bebidas a un carrito, aplica ofertas y muestra un ticket con el IVA separado.

Solo se usa Python (no hace falta instalar nada). Hace falta **Python 3.10 o superior** porque usamos `match`.

## Cómo ejecutarlo

Desde la carpeta del proyecto:

```
python main.py
```

Para pasar las pruebas:

```
python -m unittest tests.test_calculos
```

## Estructura del proyecto

```
main.py              -> arranca el programa
src/
  ingredientes.py    -> ingredientes y su precio por kg
  pizzas.py          -> las 21 pizzas con los gramos de cada ingrediente
  gastos.py          -> suministros, personal, alquiler e IVA
  margenes.py        -> margen de beneficio
  temporada.py       -> pizzas que se venden al mes según la temporada
  calculos.py        -> cálculo del precio de una pizza y del IVA
  bebidas.py         -> carta de bebidas
  carrito.py         -> añadir, quitar y ver productos del carrito
  ofertas.py         -> las 4 ofertas
  ticket.py          -> ticket final
  menu.py            -> menú de la caja
tests/
  test_calculos.py   -> pruebas
docs/                -> memoria y enunciado
```

## Estructuras de datos

- **Diccionarios**: `ingredientes` (ingrediente → precio por kg), `pizzas` (pizza → diccionario de ingrediente → gramos), `bebidas` (bebida → precio) y el que devuelve `contarProductos` (producto → cantidad).
- **Listas**: el `carrito` (por ejemplo `["Margarita", "Margarita", "cola"]`) y la lista de descuentos que se aplican.
- **Tuplas**: `temporadas` y `diasSemana`, que no cambian nunca. Cada descuento también es una tupla `(nombre, dinero)`.
- **Conjuntos**: `pizzas_2x1`, las pizzas que entran en el 2x1.

## Funciones

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

## Ofertas

1. **2x1** en Margarita, Prosciutto y Hawaiana. Se pueden mezclar y la más barata sale gratis.
2. **Menú pizza + bebida**: 1 € de descuento por cada pizza con bebida. Las pizzas gratis del 2x1 no cuentan.
3. **Martes**: 20% de descuento en las pizzas (sin contar las que ya son gratis).
4. **Pedido de más de 30 €**: 10% de descuento. Se mira con el total después de las otras ofertas.

El día se coge solo con la fecha del ordenador, pero se puede cambiar en el menú (opción 10) para probar la oferta del martes.

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

Pedido de 2 Margaritas, 1 Barbacoa y 2 colas un martes, en temporada media:

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
