# os - Interacción con el sistema operativo
import os

# Obtener directorio actual
directorio_actual = os.getcwd()
print(f"Directorio actual: {directorio_actual}")

# Listar archivos
archivos = os.listdir('.')
print(f"Archivos: {archivos}")

# Crear directorio
os.makedirs('nuevo_directorio', exist_ok=True)