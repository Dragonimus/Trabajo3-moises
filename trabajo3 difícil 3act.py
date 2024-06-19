def encontrar_palabra_mas_comun(manuscrito):
    palabras = manuscrito.split()
    frecuencia_palabras = {}
    for palabra in palabras:
        frecuencia_palabras[palabra] = frecuencia_palabras.get(palabra, 0) + 1
    palabra_mas_comun = max(frecuencia_palabras, key=frecuencia_palabras.get)
    return palabra_mas_comun

if __name__ == "__main__":
    manuscrito_antiguo = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat."

    palabra_comun = encontrar_palabra_mas_comun(manuscrito_antiguo)

    print("Palabra más común en el manuscrito antiguo:", palabra_comun)
