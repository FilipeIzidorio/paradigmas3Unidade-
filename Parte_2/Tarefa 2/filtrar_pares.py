
def filtrar_pares(lista):
    pares = []
    for numero in lista:
        if numero % 2 == 0:
            pares.append(numero)
    return pares


entrada = [1, 2, 3, 4, 5, 6]
print("Números pares:", filtrar_pares(entrada))
