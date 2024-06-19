def calcular_datos(monedas):
    suma_total = sum(monedas)
    promedio = suma_total / len(monedas)
    moneda_mas_valiosa = max(monedas)
    return suma_total, promedio, moneda_mas_valiosa

if __name__ == "__main__":
    monedas_de_oro = [10, 20, 30, 40, 50]

    suma_total, promedio, moneda_mas_valiosa = calcular_datos(monedas_de_oro)

    print(f"Suma total de monedas: {suma_total}")
    print(f"Promedio de valor de monedas: {promedio}")
    print(f"Moneda más valiosa: {moneda_mas_valiosa}")
