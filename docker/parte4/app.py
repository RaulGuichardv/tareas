from flask import Flask
import redis
import os

app = Flask(__name__)
redis_client = redis.Redis(host='redis', port=6379)

@app.route('/')
def hello():
    contador = redis_client.incr('visitas')
    return f'¡Esta página ha sido visitada {contador} veces!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)