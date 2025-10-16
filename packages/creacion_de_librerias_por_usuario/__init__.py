"""
Mi Librería Personal - Herramientas de Desarrollo
================================================

Una librería completa con utilidades para desarrollo en Python.

Módulos disponibles:
- utilidades: Funciones matemáticas y de texto
- datos: Procesamiento y validación de datos
- visualizacion: Gráficos y reportes
"""

__version__ = "1.0.0"
__author__ = "Tu Nombre"
__email__ = "tu.email@universidad.edu"

# Importaciones principales para acceso directo
from .utilidades.matematicas import (
    factorial, fibonacci, es_primo, calcular_estadisticas
)
from .utilidades.texto import (
    limpiar_texto, extraer_numeros, capitalizar_palabras
)
from .datos.procesador import ProcesadorDatos
from .datos.validador import ValidadorDatos
from .visualizacion.graficos import GraficadorAvanzado

# Lista de componentes públicos
__all__ = [
    'factorial', 'fibonacci', 'es_primo', 'calcular_estadisticas',
    'limpiar_texto', 'extraer_numeros', 'capitalizar_palabras',
    'ProcesadorDatos', 'ValidadorDatos', 'GraficadorAvanzado'
]

def info():
    """Muestra información sobre la librería."""
    print(f"""
    Mi Librería Personal v{__version__}
    {'='*40}
    Autor: {__author__}
    Email: {__email__}
    
    Módulos disponibles:
    - utilidades.matematicas: Funciones matemáticas
    - utilidades.texto: Procesamiento de texto
    - datos.procesador: Procesamiento de datos
    - datos.validador: Validación de datos
    - visualizacion.graficos: Gráficos avanzados
    
    Uso: import mi_libreria
    """)