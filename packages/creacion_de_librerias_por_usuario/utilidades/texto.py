"""Módulo de utilidades para procesamiento de texto."""

import re
import string
from typing import List, Dict
from collections import Counter

def limpiar_texto(texto: str, mantener_numeros: bool = True, 
                 mantener_espacios: bool = True) -> str:
    """
    Limpia un texto removiendo caracteres especiales.
    
    Args:
        texto: Texto a limpiar
        mantener_numeros: Si mantener números
        mantener_espacios: Si mantener espacios
        
    Returns:
        Texto limpio
    """
    if not texto:
        return ""
    
    # Convertir a minúsculas
    texto = texto.lower()
    
    # Definir caracteres permitidos
    caracteres_permitidos = string.ascii_lowercase
    if mantener_numeros:
        caracteres_permitidos += string.digits
    if mantener_espacios:
        caracteres_permitidos += ' '
    
    # Filtrar caracteres
    texto_limpio = ''.join(c for c in texto if c in caracteres_permitidos)
    
    # Limpiar espacios múltiples
    if mantener_espacios:
        texto_limpio = re.sub(r'\s+', ' ', texto_limpio).strip()
    
    return texto_limpio

def extraer_numeros(texto: str) -> List[float]:
    """
    Extrae todos los números de un texto.
    
    Args:
        texto: Texto del cual extraer números
        
    Returns:
        Lista de números encontrados
    """
    patron = r'-?\d+\.?\d*'
    numeros_str = re.findall(patron, texto)
    return [float(num) for num in numeros_str if num]

def capitalizar_palabras(texto: str, excepciones: List[str] = None) -> str:
    """
    Capitaliza las palabras de un texto, excepto las especificadas.
    
    Args:
        texto: Texto a capitalizar
        excepciones: Lista de palabras que no se deben capitalizar
        
    Returns:
        Texto con palabras capitalizadas
    """
    if not texto:
        return ""
    
    if excepciones is None:
        excepciones = ['y', 'o', 'de', 'del', 'la', 'el', 'los', 'las', 'en', 'con']
    
    palabras = texto.split()
    palabras_capitalizadas = []
    
    for i, palabra in enumerate(palabras):
        # Primera palabra siempre se capitaliza
        if i == 0 or palabra.lower() not in excepciones:
            palabras_capitalizadas.append(palabra.capitalize())
        else:
            palabras_capitalizadas.append(palabra.lower())
    
    return ' '.join(palabras_capitalizadas)

def contar_palabras(texto: str) -> Dict[str, int]:
    """
    Cuenta la frecuencia de palabras en un texto.
    
    Args:
        texto: Texto a analizar
        
    Returns:
        Diccionario con el conteo de palabras
    """
    texto_limpio = limpiar_texto(texto, mantener_numeros=False)
    palabras = texto_limpio.split()
    return dict(Counter(palabras))

def generar_resumen(texto: str, num_oraciones: int = 3) -> str:
    """
    Genera un resumen simple del texto basado en frecuencia de palabras.
    
    Args:
        texto: Texto a resumir
        num_oraciones: Número de oraciones en el resumen
        
    Returns:
        Resumen del texto
    """
    if not texto:
        return ""
    
    # Dividir en oraciones
    oraciones = re.split(r'[.!?]+', texto)
    oraciones = [o.strip() for o in oraciones if o.strip()]
    
    if len(oraciones) <= num_oraciones:
        return texto
    
    # Contar palabras importantes (más de 3 caracteres)
    todas_palabras = []
    for oracion in oraciones:
        palabras = limpiar_texto(oracion, mantener_numeros=False).split()
        todas_palabras.extend([p for p in palabras if len(p) > 3])
    
    frecuencias = Counter(todas_palabras)
    
    # Puntuar oraciones basado en palabras importantes
    puntuaciones = []
    for oracion in oraciones:
        palabras = limpiar_texto(oracion, mantener_numeros=False).split()
        puntuacion = sum(frecuencias.get(p, 0) for p in palabras if len(p) > 3)
        puntuaciones.append((puntuacion, oracion))
    
    # Seleccionar las mejores oraciones
    puntuaciones.sort(reverse=True)
    mejores_oraciones = [oracion for _, oracion in puntuaciones[:num_oraciones]]
    
    return '. '.join(mejores_oraciones) + '.'