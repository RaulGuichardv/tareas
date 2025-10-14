from fastapi import FastAPI

# Inicializa la aplicación de FastAPI
app = FastAPI()

# Define una ruta en la URL raíz ("/")
@app.get('/')
def hola_mundo():
    """
    Esta función se ejecuta cuando alguien accede a la URL raíz con un método GET.
    """
    return {"mensaje": "Hola Mundo desde FastAPI!"}