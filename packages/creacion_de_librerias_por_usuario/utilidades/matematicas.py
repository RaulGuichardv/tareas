"""Módulo de utilidades matemáticas."""

import math
from typing import List, Dict, Union
from functools import lru_cache

@lru_cache(maxsize=128)
def factorial(n: int) -> int:
    """
    Calcula el factorial de un número.
    
    Args:
        n: Número entero no negativo
        
    Returns:
        Factorial de n
        
    Raises:
        ValueError: Si n es negativo
    """
    if n < 0:
        raise ValueError("El factorial no está definido para números negativos")
    if n <= 1:
        return 1
    return n * factorial(n - 1)

@lru_cache(maxsize=128)
def fibonacci(n: int) -> int:
    """
    Calcula el n-ésimo número de Fibonacci.
    
    Args:
        n: Posición en la secuencia (0-indexada)
        
    Returns:
        El n-ésimo número de Fibonacci
    """
    if n < 0:
        raise ValueError("n debe ser no negativo")
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

def es_primo(n: int) -> bool:
    """
    Verifica si un número es primo.
    
    Args:
        n: Número a verificar
        
    Returns:
        True si es primo, False en caso contrario
    """
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    # Verificar divisores impares hasta sqrt(n)
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def calcular_estadisticas(datos: List[Union[int, float]]) -> Dict[str, float]:
    """
    Calcula estadísticas descriptivas de una lista de números.
    
    Args:
        datos: Lista de números
        
    Returns:
        Diccionario con estadísticas (media, mediana, moda, desviación estándar)
    """
    if not datos:
        raise ValueError("La lista no puede estar vacía")
    
    datos_ordenados = sorted(datos)
    n = len(datos)
    
    # Media
    media = sum(datos) / n
    
    # Mediana
    if n % 2 == 0:
        mediana = (datos_ordenados[n//2 - 1] + datos_ordenados[n//2]) / 2
    else:
        mediana = datos_ordenados[n//2]
    
    # Moda (valor más frecuente)
    from collections import Counter
    contador = Counter(datos)
    moda = contador.most_common(1)[0][0]
    
    # Desviación estándar
    varianza = sum((x - media) ** 2 for x in datos) / n
    desviacion_estandar = math.sqrt(varianza)
    
    return {
        'media': round(media, 4),
        'mediana': mediana,
        'moda': moda,
        'desviacion_estandar': round(desviacion_estandar, 4),
        'varianza': round(varianza, 4),
        'minimo': min(datos),
        'maximo': max(datos),
        'rango': max(datos) - min(datos)
    }

def generar_primos(limite: int) -> List[int]:
    """
    Genera todos los números primos hasta un límite usando la Criba de Eratóstenes.
    
    Args:
        limite: Número límite (inclusive)
        
    Returns:
        Lista de números primos
    """
    if limite < 2:
        return []
    
    # Criba de Eratóstenes
    es_primo_array = [True] * (limite + 1)
    es_primo_array[0] = es_primo_array[1] = False
    
    for i in range(2, int(math.sqrt(limite)) + 1):
        if es_primo_array[i]:
            for j in range(i*i, limite + 1, i):
                es_primo_array[j] = False
    
    return [i for i in range(2, limite + 1) if es_primo_array[i]]