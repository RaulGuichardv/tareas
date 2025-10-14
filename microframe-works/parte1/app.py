from flask import Flask, jsonify

# Inicializa la aplicación de Flask
app = Flask(__name__)

# Define una ruta en la URL raíz ("/")
@app.route('/')
def hola_mundo():
    """
    Esta función se ejecuta cuando alguien accede a la URL raíz.
    """
    return jsonify(mensaje="Hola Mundo desde Flask!")

# Permite ejecutar la aplicación directamente con 'python app.py'
if __name__ == '__main__':
    app.run(debug=True)