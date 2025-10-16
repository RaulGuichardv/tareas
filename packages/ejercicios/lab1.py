# Ejercicio 1: Usar os y sys para información del sistema
import os
import sys
import platform


def info_sistema():
    """Recopila información del sistema."""
    # TODO: Implementar función que retorne diccionario con:
    # - Sistema operativo
    # - Versión de Python
    # - Directorio actual
    # - Variables de entorno importantes
    informacion = {
        "sistema_operativo" : platform.system(), 
        "version_de_python": sys.version,
        "directorio_actual": os.getcwd(),
        "variables_de_entorno_importantes": {
            "PATH": os.environ.get("PATH"),
            "HOME": os.environ.get("HOME") or os.environ.get("USERPROFILE"),
            "USER": os.environ.get("USER") or os.environ.get("USERNAME"),
        }
    }
    return informacion

if __name__ == "__main__":
    datos = info_sistema()
    for clave, valor in datos.items():
        print(f"{clave}: {valor}\n")