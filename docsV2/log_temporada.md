# Log de temporada (versión 2)

## 2026-11-09 · Pau Mas · rama `version2_src_temporada`

### Rama actualizada
- `version2_src_temporada` se ha igualado con `version2` (fast-forward hasta el commit `dfb01cb`).
- No se ha perdido nada: la rama no tenía commits propios, solo le faltaban los dos últimos de `version2`.

### `srcV2/temporada.py` (nuevo)
La temporada pasa de funciones sueltas (`srcV1/temporada.py`) a una clase con objetos.

- **Clase `Temporada`**
  - `nombre`: "baja", "media" o "alta".
  - `pizzasEstimadas`: pizzas que se venden al mes.
  - `obtenerPizzasEstimadas()`: devuelve las pizzas estimadas.
  - `__str__()`: al hacer `print` muestra, por ejemplo, `Temporada alta (1500 pizzas/mes)`.
- **Objetos**: `baja` (600), `media` (1000) y `alta` (1500), los mismos valores que en la versión 1.
- **`temporadas`**: tupla con las tres temporadas.
- **`obtenerTemporada(nombre)`**: busca una temporada por su nombre y lanza `ValueError` si no existe.

Ejemplo:
```python
from srcV2.temporada import alta
alta.obtenerPizzasEstimadas()   # 1500
```

### `srcV2/__init__.py` (nuevo)
- Archivo vacío para que `srcV2` sea un paquete y funcionen los imports (`from srcV2.temporada import ...`).

### Pruebas
- Se crean las tres temporadas y se imprimen bien.
- `obtenerTemporada("media")` devuelve 1000 pizzas al mes.
- `obtenerTemporada("x")` lanza `ValueError("Temporada no válida")`.
