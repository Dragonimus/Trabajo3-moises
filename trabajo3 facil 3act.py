def crear_diccionario_edades():
    return {
        "Carlos": 30,
        "Marta": 25,
        "Pedro": 40,
        "Antonella": 35
    }

if __name__ == "__main__":
    diccionario_edades = crear_diccionario_edades()

    print("Diccionario de edades de las personas encontradas en la isla:")
    for nombre, edad in diccionario_edades.items():
        print(f"{nombre}: {edad} años")
