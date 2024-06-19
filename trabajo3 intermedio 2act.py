def registrar_coordenadas_lago():
    x, y = map(float, input("Ingrese las coordenadas del lago (x y): ").split())
    return x, y

if __name__ == "__main__":
    coordenadas_lago = registrar_coordenadas_lago()

    print("Coordenadas del lago:")
    print(f"x: {coordenadas_lago[0]}")
    print(f"y: {coordenadas_lago[1]}")
