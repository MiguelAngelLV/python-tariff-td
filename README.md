# Tariff TD

Tariff TD es una biblioteca para Python que permite determinar el periodo de las tarifas 2.0 TD y 3.0 TD españolas en una fecha determinada así como obtener el precio correspondiente.

Esta biblioteca usa los festivos proporcionados por la biblioteca `hollidays` pero elimina los `Viernes Santos`, puesto que dicho festivo,
al cambiar de fecha cada año, no es considerado valle.

## Ejemplo de suo

```python

from datetime import datetime

from src.tariff_td import Tariff20TD

FORMAT = "%Y-%m-%d %H:%M:%S"

# Creamos la instancia especificando los precios.
# En caso de la Tarifa 3.0, se usaría Tariff30TD
tariff = Tariff20TD(p1=0.17, p2=0.15, p3=0.10)

# Creamos una fecha
date = datetime.strptime("2024-01-02 06:00:00", FORMAT)

# Obtenemos el periodo
period = tariff.get_period(date)

# Obtenemos el precio
price = tariff.get_price(date)
```
