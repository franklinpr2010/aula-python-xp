numeros = [1, 2, 3, 4, 5, 6]

# Filtrando os números pares
pares = filter(lambda x: x % 2 == 0, numeros)
# Convertendo o objeto filter para uma lista
print(list(pares))  # Saída: [2, 4, 6]


def eh_par(x):
    return x % 2 == 0

numeros = [1, 2, 3, 4, 5, 6]
pares = filter(eh_par, numeros)
print(list(pares))  # Saída: [2, 4, 6]


#Exemplo: Filtrando Strings
#Você pode usar o filter para remover elementos que não atendem a uma condição, como strings vazias:
nomes = ["Ana", "", "Carlos", "", "Maria"]
nomes_validos = filter(lambda nome: nome != "", nomes)
print(list(nomes_validos))  # Saída: ['Ana', 'Carlos', 'Maria']

#Exemplo: Números Positivos
#Filtrando apenas números positivos de uma lista:
numeros = [-1, 0, 3, -5, 8]
positivos = filter(lambda x: x > 0, numeros)
print(list(positivos))  # Saída: [3, 8]

numeros = [1, 2, 3, 4, 5]
pares = filter(lambda x: x % 2 == 0, numeros)
print(list(pares))  # Saída: [2, 4]

numeros = [4, 11, 15, 8, 22]
maiores_que_dez = filter(lambda x: x > 10, numeros)
print(list(maiores_que_dez))  # Saída: [11, 15, 22]

#Filtrar palavras que começam com "A":
palavras = ["Ana", "Carlos", "Antonio", "Maria"]
com_a = filter(lambda palavra: palavra.startswith("A"), palavras)
print(list(com_a))  # Saída: ['Ana', 'Antonio']