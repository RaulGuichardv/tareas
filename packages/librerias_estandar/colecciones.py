from collections import defaultdict, Counter, namedtuple, deque

# defaultdict - diccionario con valores por defecto
grupos = defaultdict(list)
personas = [
    ("Juan", "Ingeniería"),
    ("María", "Medicina"),
    ("Carlos", "Ingeniería"),
    ("Ana", "Medicina")
]

for nombre, carrera in personas:
    grupos[carrera].append(nombre)

print(dict(grupos))  # {'Ingeniería': ['Juan', 'Carlos'], 'Medicina': ['María', 'Ana']}

# Counter - contador de elementos
palabras = "python es genial python es poderoso".split()
contador = Counter(palabras)
print(contador.most_common(2))  # [('python', 2), ('es', 2)]

# namedtuple - tupla con nombres
Persona = namedtuple('Persona', ['nombre', 'edad', 'ciudad'])
persona1 = Persona("Juan", 25, "Madrid")
print(f"{persona1.nombre} tiene {persona1.edad} años")

# deque - cola de doble extremo
cola = deque(['a', 'b', 'c'])
cola.appendleft('z')  # Agregar al inicio
cola.append('d')      # Agregar al final
print(cola)  # deque(['z', 'a', 'b', 'c', 'd'])