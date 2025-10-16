from datetime import datetime, timedelta, date
import time

# Fecha y hora actual
ahora = datetime.now()
print(f"Ahora: {ahora}")

# Formateo de fechas
fecha_formateada = ahora.strftime("%d/%m/%Y %H:%M:%S")
print(f"Fecha formateada: {fecha_formateada}")

# Operaciones con fechas
mañana = ahora + timedelta(days=1)
hace_una_semana = ahora - timedelta(weeks=1)

# Medición de tiempo de ejecución
inicio = time.time()
# ... código a medir ...
fin = time.time()
tiempo_ejecucion = fin - inicio