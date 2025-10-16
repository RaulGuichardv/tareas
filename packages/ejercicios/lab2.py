# Ejercicio 2: Procesamiento de fechas
from datetime import datetime, timedelta, date

def calcular_edad_dias(fecha_fecha_nac: str):
    """Calcula edad en días desde fecha de fecha_nac."""
    # TODO: Implementar cálculo de edad en días
    # Formato fecha: "YYYY-MM-DD"
    fecha_nac = datetime.strptime(fecha_fecha_nac, "%Y-%m-%d").date()
    fecha_actual = datetime.now().date()

    return (fecha_actual - fecha_nac).days

print(calcular_edad_dias("2005-07-04"))

def proximo_cumpleanos(fecha_fecha_nac: str):
    """Calcula días hasta el próximo cumpleaños."""
    # TODO: Implementar cálculo
    fecha_nac = datetime.strptime(fecha_fecha_nac, "%Y-%m-%d").date()
    fecha_actual = date.today()
    
    proximo = date(fecha_actual.year, fecha_nac.month, fecha_nac.day)

    if proximo < fecha_actual:
        proximo = date(fecha_actual.year + 1, fecha_nac.month, fecha_nac.day)

    dias_restantes = (proximo - fecha_actual).days

    return dias_restantes

print(proximo_cumpleanos("2005-07-04"))