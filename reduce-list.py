from functools import reduce

numeros = [1, 2, 3, 4]

# Função que soma dois números
def soma(x, y):
    return x + y

resultado = reduce(soma, numeros)
print(resultado)  # Saída: 10

from functools import reduce

numeros = [1, 2, 3, 4]
resultado = reduce(lambda soma, numero: soma + numero, numeros)
print(resultado)  # Saída: 10


from functools import reduce

numeros = [1, 2, 3, 4]
produto = reduce(lambda x, y: x * y, numeros)
print(produto)  # Saída: 24


numeros = [5, 1, 8, 3, 2]
maior = reduce(lambda x, y: x if x > y else y, numeros)
print(maior)  # Saída: 8

numeros = [1, 2, 3, 4]
resultado = reduce(lambda x, y: x + y, numeros, 10)
print(resultado)  # Saída: 20



