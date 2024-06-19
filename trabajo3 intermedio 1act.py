def eliminar_duplicados(lista_cristales):
    lista_sin_duplicados = []
    for cristal in lista_cristales:
        if cristal not in lista_sin_duplicados:
            lista_sin_duplicados.append(cristal)
    return lista_sin_duplicados

if __name__ == "__main__":
    cristales_preciosos = ["diamante", "rubí", "esmeralda", "zafiro", "rubí", "diamante"]

    lista_sin_duplicados = eliminar_duplicados(cristales_preciosos)

    print("Lista de cristales preciosos sin duplicados:", lista_sin_duplicados)
