import matplotlib.pyplot as plt
import numpy as np
from typing import List, Dict

class VisualizadorDatos:
    def __init__(self, estilo: str = "seaborn"):
        plt.style.use(estilo)

    def grafico_barras(self, datos: Dict[str, float], titulo: str = ""):
        etiquetas = list(datos.keys())
        valores = list(datos.values())
        colores = plt.cm.viridis(np.linspace(0.2, 0.8, len(valores)))
        plt.bar(etiquetas, valores, color=colores)
        plt.title(titulo)
        plt.xlabel("Categorías")
        plt.ylabel("Valores")
        plt.show()

    def grafico_lineas(self, x: List, y: List, titulo: str = ""):
        plt.plot(x, y, marker="o")
        plt.title(titulo)
        plt.xlabel("Eje X")
        plt.ylabel("Eje Y")
        plt.grid(True)
        plt.show()

    def histograma(self, datos: List[float], bins: int = 20):
        plt.hist(datos, bins=bins, color="skyblue", edgecolor="black")
        plt.title("Histograma")
        plt.xlabel("Valores")
        plt.ylabel("Frecuencia")
        plt.show()

    def guardar_figura(self, nombre: str):
        plt.savefig(nombre, bbox_inches="tight")

ventas_mensuales = {
    "Enero": 15000, "Febrero": 18000, "Marzo": 22000,
    "Abril": 19000, "Mayo": 25000, "Junio": 28000
}

temperaturas = [23, 25, 27, 24, 22, 26, 28, 30, 29, 27, 25, 24]
