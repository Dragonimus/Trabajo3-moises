import cmath

def convertir_coordenadas_polares(x, y):
    """
    Convierte las coordenadas cartesianas (x, y) a coordenadas polares (r, θ).

    Args:
        x (float): Coordenada x en el plano cartesiano.
        y (float): Coordenada y en el plano cartesiano.

    Returns:
        tuple: Una tupla que contiene la distancia desde el origen (r) y el ángulo con respecto al eje x (θ) en radianes.
    """
    coordenadas_cartesianas = complex(x, y)
    coordenadas_polares = cmath.polar(coordenadas_cartesianas)
    return coordenadas_polares

if __name__ == "__main__":
    x = float(input("Ingrese la coordenada x del objeto misterioso: "))
    y = float(input("Ingrese la coordenada y del objeto misterioso: "))

    r, theta = convertir_coordenadas_polares(x, y)

    print("Coordenadas polares del objeto misterioso:")
    print(f"Distancia desde el origen (r): {r}")
    print(f"Ángulo con respecto al eje x (θ) en radianes: {theta}")
