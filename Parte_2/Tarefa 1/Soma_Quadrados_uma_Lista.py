
def soma_quadrados(lista):
    soma = 0
    for numero in lista:
        soma += numero ** 2
    return soma


entrada = [1, 2, 3, 4]
print("Soma dos quadrados:", soma_quadrados(entrada))
