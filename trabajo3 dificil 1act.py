def comparar_cofres(cofre1, cofre2):
    """
    Compara el contenido de dos cofres del tesoro y devuelve una lista con las monedas que se encuentran en ambos cofres.

    Args:
        cofre1 (list): La lista de monedas del primer cofre.
        cofre2 (list): La lista de monedas del segundo cofre.

    Returns:
        list: La lista de monedas que se encuentran en ambos cofres.
    """
    monedas_comunes = []
    for moneda in cofre1:
        if moneda in cofre2:
            monedas_comunes.append(moneda)
    return monedas_comunes

if __name__ == "__main__":
    cofre1 = ["moneda de oro", "moneda de plata", "gema", "rubí", "esmeralda"]
    cofre2 = ["moneda de oro", "diamante", "gema", "zafiro", "rubí"]

    monedas_comunes = comparar_cofres(cofre1, cofre2)

    print("Monedas comunes en ambos cofres:", monedas_comunes)
