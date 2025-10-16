# sys - Información del sistema y intérprete
import sys

print(f"Versión de Python: {sys.version}")
print(f"Plataforma: {sys.platform}")
print(f"Argumentos de línea de comandos: {sys.argv}")

# Agregar rutas al PATH de Python
sys.path.append('/ruta/personalizada')