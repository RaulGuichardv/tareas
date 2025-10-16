import json

# Datos de ejemplo
datos = {
    "nombre": "Juan Pérez",
    "edad": 30,
    "activo": True,
    "habilidades": ["Python", "JavaScript", "SQL"]
}

# Convertir a JSON
json_string = json.dumps(datos, indent=2, ensure_ascii=False)
print(json_string)

# Leer desde JSON
datos_recuperados = json.loads(json_string)

# Guardar en archivo
with open('datos.json', 'w', encoding='utf-8') as archivo:
    json.dump(datos, archivo, indent=2, ensure_ascii=False)

# Leer desde archivo
with open('datos.json', 'r', encoding='utf-8') as archivo:
    datos_del_archivo = json.load(archivo)