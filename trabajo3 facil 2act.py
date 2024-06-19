def crear_tupla_frutas():
    return "manzana", "banana", "naranja", "uva", "pera"  # Se puede omitir los paréntesis

if __name__ == "__main__":
    tupla_frutas = crear_tupla_frutas()

    print("Frutas encontradas en la isla misteriosa:")
    for fruta in tupla_frutas:
        print(fruta)
