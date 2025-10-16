import re

# Patrón para validar email
patron_email = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

def validar_email(email):
    return re.match(patron_email, email) is not None

# Búsqueda y reemplazo
texto = "Mi teléfono es 555-1234 y mi móvil es 555-5678"
telefonos = re.findall(r'\d{3}-\d{4}', texto)
print(f"Teléfonos encontrados: {telefonos}")

# Reemplazo
texto_censurado = re.sub(r'\d{3}-\d{4}', 'XXX-XXXX', texto)