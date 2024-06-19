from collections import defaultdict

def contar_frecuencia_letras(inscripcion):
    diccionario_frecuencia = defaultdict(int)
    for letra in inscripcion:
        diccionario_frecuencia[letra] += 1
    return diccionario_frecuencia

if __name__ == "__main__":
    inscripcion_antigua = "Lorem ipsum dolor sit amet, consectetur adipiscing elit."

    frecuencia_letras = contar_frecuencia_letras(inscripcion_antigua)

    print("Frecuencia de cada letra en la inscripción antigua:")
    for letra, frecuencia in frecuencia_letras.items():
        print(f"{letra}: {frecuencia}")
