# Log de la versión 2

Un apartado por cada rama, ordenados por día. Cada rama se crea a partir de version2 y, cuando está lista, se junta con version2.

## 09/11/2026

### Ticket (version2_src_ticket)

Se ha creado la rama version2_src_ticket a partir de version2. Se ha revisado srcV2/ticket2.py, que tiene la clase Ticket: recibe el carrito, la temporada, el día y las ofertas, y su método mostrar() imprime el ticket y devuelve el total. Se han cambiado los importes para que salgan siempre con 2 decimales (9.60 € en vez de 9.6 €) y se ha añadido srcV2/__init__.py para que srcV2 sea un paquete como srcV1. Por error, la rama se juntó primero con main en vez de con version2 (Pull Request #7). Después se juntó también con version2.

### Cálculos (version2_src_calculos)

Se ha creado srcV2/calculos2.py con la clase Calculadora, que hace los mismos cálculos que srcV1/calculos.py: coste fijo por pizza, coste total, precio sin IVA, precio con IVA y separar el IVA del total. También se ha creado un objeto calculadora listo para usar, que es el que importa el ticket. Se ha añadido tests/test_calculos2.py, que comprueba que da los mismos precios que la v1 en las 21 pizzas y las 3 temporadas.

### Temporada (version2_src_temporada)

Hoy he actualizado la rama version2_src_temporada con lo último de version2. Después he creado srcV2/temporada.py con la clase Temporada y tres objetos: baja (600 pizzas al mes), media (1000) y alta (1500). Lo he probado y lo he subido a la rama.

### Ingredientes (version2_src_ingredientes)

Se ha creado la rama version2_src_ingredientes a partir de version2. Se ha creado srcV2/ingredientes2.py con la clase Ingrediente (nombre y precio por kg) y su método precio(gramos). Hay un diccionario ingredientes con un objeto por cada uno de los 50 ingredientes de la v1 y la función buscarIngrediente(nombre). Al subirlo, version2 ya tenía la rama de temporada de Pau, así que hubo que hacer git pull antes del push.

## 10/11/2026

### Pizzas (version2_src_pizzas)

Se ha creado la rama version2_src_pizzas a partir de version2. Se ha creado srcV2/pizzas2.py con la clase Pizza (nombre y receta) y sus métodos costeIngredientes(), precio(temporada), nombreTicket() y mostrarDesglose(temporada). Hay un diccionario pizzas con las 21 pizzas de la v1, buscarPizza(texto) y mostrarPizzas(temporada). Las pruebas comprueban que todas las pizzas dan el mismo precio que en la v1.

### Bebidas (version2_src_bebidas)

Se ha creado la rama version2_src_bebidas a partir de version2. Se ha creado srcV2/bebidas2.py con la clase Bebida (nombre y precio fijo). Tiene los mismos métodos que Pizza, precio(temporada) y nombreTicket(), para que el carrito y el ticket puedan tratar igual las pizzas y las bebidas. La bebida devuelve siempre el mismo precio aunque reciba la temporada.

### Carrito (version2_src_carrito)

Se ha creado la rama version2_src_carrito a partir de version2. Se ha creado srcV2/carrito2.py con la clase Carrito, que guarda una lista de productos (objetos Pizza o Bebida). Tiene los métodos agregar, quitar, vaciar, estaVacio, contarProductos, total(temporada) y mostrar(temporada), y también pizzas() y bebidas() para las ofertas. Se ha probado que da el mismo total que la v1 y que el ticket funciona con un carrito de verdad.

### Ofertas (version2_src_ofertas)

Se ha creado la rama version2_src_ofertas a partir de version2. Se ha creado srcV2/ofertas2.py con la clase Ofertas: un método para cada oferta (2x1, menú pizza + bebida, descuento del martes y pedido de más de 30 euros) y aplicar(carrito, temporada, dia), que es el que usa el ticket. Los números de las ofertas se guardan como atributos para poder cambiarlos. La prueba compara 300 carritos al azar con la v1 y en todos da los mismos descuentos.

### Menú (version2_src_menu)

Se ha creado la rama version2_src_menu a partir de version2. Se ha creado srcV2/menu2.py con la clase Caja, que guarda el carrito, la temporada, el día y las ofertas, y tiene un método para cada opción del menú. Tiene las mismas 10 opciones que la v1, y la temporada se comprueba con la clase Temporada de Pau. La prueba simula a una persona escribiendo en el menú y pasa por todas las opciones.

### Main (version2_main)

Se ha usado la rama version2_main. Se ha cambiado main.py para que al arrancar pregunte qué versión se quiere usar (1 o 2) y arranque esa. Solo se importa la versión elegida. También se ha arreglado el import, que seguía usando la carpeta src cuando ya se llamaba srcV1. Se han probado las dos versiones con la misma compra y dan el mismo total.

### Pruebas (version2_tests)

Se ha creado la rama version2_tests a partir de version2. Se ha arreglado tests/test_calculos.py (las pruebas de la v1), que importaba de src en vez de srcV1. También esperaba que una temporada que no existe diera 1000, cuando el código da un error, así que se ha corregido la prueba. Se ha añadido tests/__init__.py para poder lanzar todas las pruebas con un solo comando: python -m unittest discover -s tests -t .

### Cálculos (version2_src_calculos)

Se ha cambiado la Calculadora para que coja las pizzas que se venden al mes de la clase Temporada (srcV2/temporada.py) en vez de tener su propia tabla repetida. Ahora acepta un objeto Temporada o su nombre ("baja", "media" o "alta"). Se han añadido pruebas con un objeto Temporada y con una temporada nueva.

### Gastos (version2_src_gastos)

Se ha creado la rama version2_src_gastos a partir de version2. Se ha creado srcV2/gastos2.py con la clase Gastos (suministros por pizza, personal, alquiler e IVA) y el método gastosFijosMensuales(). La Calculadora ahora recibe un objeto Gastos en vez de tener esos números dentro. La prueba comprueba que los gastos son los mismos que en la v1.

### Margen (version2_src_margenes)

Se ha creado la rama version2_src_margenes a partir de version2. Se ha creado srcV2/margenes2.py con la clase Margen (el 35% de beneficio) y los métodos aplicar(coste) y porcentaje(). La Calculadora ahora recibe un objeto Margen en vez de un número. La prueba comprueba que el margen es el mismo que en la v1.

### README (version2_readme)

Se ha creado la rama version2_readme a partir de version2. Se ha actualizado el README: cómo se elige la versión al arrancar, la estructura con srcV1 y srcV2, una tabla con las clases de la v2, qué cambia respecto a la v1 y cómo lanzar las pruebas.

## 13/11/2026

### Excepciones propias (version2_src_excepciones)

Se ha creado srcV2/excepciones2.py con PizzeriaError y sus subclases ProductoNoEncontradoError, IngredienteNoEncontradoError, CantidadNoValidaError y PrecioNoValidoError, y la función leerCantidad(). El Ingrediente usa @property y su precio no puede ser negativo. El carrito lanza las excepciones y la Caja las captura con try/except sin cerrarse.

### Producto (version2_src_producto)

Se ha creado srcV2/producto2.py con la clase base abstracta Producto (abc): precioSinIva() abstracto y precio(), iva() y nombreTicket() comunes. Pizza y Bebida heredan de Producto. La Pizza guarda objetos Ingrediente (composición). Las pruebas comprueban la herencia, el polimorfismo y que no se puede crear un Producto.

### LineaCarrito (version2_src_lineacarrito)

Se ha añadido la clase LineaCarrito (producto, cantidad y subtotal). El Carrito guarda líneas: si un producto ya está, se suma la cantidad. También calcula la base imponible y el IVA.

### Menús (version2_src_menus)

Se ha creado srcV2/menus2.py con la clase Menu, que hereda de Producto y contiene otros productos. Hay menú pizza + bebida (1 € menos) y menú familiar de 2 pizzas y 2 bebidas (5 € menos). Se añaden con la opción 11 de la caja y en el ticket sale lo que lleva cada menú.

### Jerarquía de ofertas (version2_src_jerarquia_ofertas)

Se ha cambiado srcV2/ofertas2.py: clase base abstracta Oferta y subclases Oferta2x1, OfertaMenu, OfertaDiaSemana, OfertaTemporada (nueva: 10% en bebidas en temporada baja) y OfertaPedidoGrande. La clase Ofertas guarda la lista de ofertas y las aplica en orden.

### Documentación (version2_docs_poo)

Se ha actualizado el README con un diagrama de clases, la tabla de clases y dónde se usa la herencia, el polimorfismo y la encapsulación. Se ha añadido el día 3 a la memoria y las capturas de Trello en docsV2/capturas_trello.
