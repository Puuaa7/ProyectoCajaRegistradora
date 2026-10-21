Dia 1 "07/10/2026"

    1.Se ha creado la estructura de archivos y carpetas
    2.Dentro del archivo py "ingredientes" se han añadido los ingredientes para las pizzas y el precio por kg de cada uno.
    3.Dentro del archivo py "PizzaAddLista" se han añadido ciertas pizzas con sus ingredientes y los gramos de cada uno, y finalmente una funcion que llama a la funcion creada en "ingredientes" para calcular el precio base de la pizza.
    4.Se han creado los gastos fijos de la pizza y del local. Tmbién se han empezado a realizar los calculos final de costes.

Dia 2 "14/10/2026"

    1.Se ha reorganizado el proyecto, dejando el codigo activo en "src", la documentacion en "docs" y las pruebas en "tests". El codigo antiguo se ha guardado en "z.functions_antiguo" como referencia.
    2.Se ha creado el archivo "main.py" para iniciar el programa y un menu que permite consultar las pizzas y sus precios, cambiar la temporada y salir.
    3.Se ha añadido el calculo del precio de venta de las pizzas, teniendo en cuenta los ingredientes, los suministros, los gastos de personal y alquiler, un recargo del 35% sobre el coste y el IVA del 10%. Los gastos fijos por pizza se reparten segun las ventas previstas de cada temporada: baja, media o alta.
    4.Se ha creado la carta de bebidas con sus precios y una funcion para mostrarla. Tambien se han añadido pruebas para los calculos, el archivo "requirements.txt" y un ".gitignore".
    5.Dentro del archivo "ofertas.py" se ha creado la oferta 2x1 para las pizzas Margarita, Prosciutto y Barbacoa. Se ordenan sus precios y se descuenta la pizza mas barata de cada pareja.
    6.Se ha añadido una funcion que aplica un descuento del 10% cuando el total supera los 30 euros. Tambien se han dejado comentarios con ideas para una oferta de pizza y bebida y para la futura aplicacion de las ofertas al ticket.


Dia 3 "21/10/2026"

    1.Tenemos que ser sinceros sobre como hemos trabajado. Durante estas semanas Alex y yo hemos programado casi todo juntos con Live Share de Visual Studio Code, en una carpeta llamada "PIZZA" en el ordenador de Pau. Nos resultaba mas comodo programar a la vez y ayudarnos en directo, pero no nos dimos cuenta de que asi no quedaba guardado ningun commit en GitHub de todo lo que ibamos haciendo.
    2.Cuando nos dimos cuenta, el programa ya estaba casi terminado fuera del repositorio, y en GitHub solo estaba la version del dia 2. Nos agobiamos bastante, porque el enunciado pide ramas, commits y una distribucion clara de tareas, y parecia que no habiamos hecho nada cuando en realidad llevabamos muchas horas trabajando.
    3.Para arreglarlo, primero adaptamos el codigo de "PIZZA" a la estructura del repositorio: todo dentro de "src" con un archivo "__init__.py", para poder importar con "from src..." en vez de añadir carpetas a mano con "sys.path". Tambien juntamos las pizzas e ingredientes de Pau con el resto del codigo, hasta llegar a 21 pizzas.
    4.Despues pasamos el codigo a GitHub poco a poco, no todo de golpe. Una rama es como una copia del proyecto donde puedes hacer cambios sin estropear la version principal ("main"). Hicimos una rama para cada parte del programa, y cada parte la subio quien la tenia asignada en Trello:
        - Pau subio 3 partes: los calculos del precio, las 21 pizzas y las ofertas.
        - Alex subio 5 partes: las bebidas y el carrito, el ticket, el menu, las pruebas y el README.
       Cuando una parte estaba lista, la juntabamos con "main" para que el programa completo la tuviera.
    5.Tuvimos varios problemas por el camino:
        - La rama "feature/bebidas" se habia creado con la estructura antigua de carpetas y daba conflictos con "src". Primero intentamos arreglarla, pero seguia dando problemas con "calculos.py", asi que al final Alex la borro y la volvimos a hacer desde "main", limpia y con solo los archivos de bebidas y carrito.
        - Al cambiar los nombres de las funciones de calculo, el programa de "main" dejaba de funcionar hasta tener todas las ramas, porque el menu, las ofertas y las pruebas usaban los nombres antiguos. Tuvimos que tener mucho cuidado con el orden en que juntabamos las ramas.
        - Intentamos hacer revisiones de los Pull Requests entre nosotros, pero no sabiamos bien como funcionaban y nos estaban bloqueando, asi que decidimos dejarlo y juntar las ramas directamente.
    6.Con las prisas, al final juntamos todas las ramas en "main" el mismo dia, antes de lo que habiamos planeado. Por eso en el historial parece que todo se ha hecho de golpe, aunque el trabajo es de varias semanas.
    7.Cambios de criterio: la oferta 2x1 era para Margarita, Prosciutto y Barbacoa (dia 2), y al final la dejamos para Margarita, Prosciutto y Hawaiana. Tambien añadimos dos ofertas mas: menu pizza + bebida (1 euro de descuento) y 20% en las pizzas los martes. Actualizamos la tarjeta de Trello para que coincida con el codigo.
    8.Al terminar comprobamos que todo funciona: pasan las 7 pruebas y el menu completo funciona desde el principio hasta el ticket, con la base imponible y el IVA separados.
    9.Lo que hemos aprendido: hay que hacer commits desde el primer dia, aunque se programe con Live Share, y crear las ramas antes de empezar cada parte, no al final. Nos ha costado mucho mas arreglarlo despues que si lo hubieramos hecho bien desde el principio. En los proximos dias seguiremos mejorando el proyecto haciendo commits de cada cambio.







