# Lista simples
minha_lista = [1, 2, 3, 4, 5]
print(minha_lista)  # Saída: [1, 2, 3, 4, 5]

# Lista com elementos de diferentes tipos
lista_mista = ["texto", 10, True, 3.14]
print(lista_mista)  # Saída: ['texto', 10, True, 3.14]

# Índices positivos
print(minha_lista[0])  # Saída: 1 (primeiro elemento)
print(minha_lista[2])  # Saída: 3

# Índices negativos (conta de trás para frente)
print(minha_lista[-1])  # Saída: 5 (último elemento)
print(minha_lista[-2])  # Saída: 4

minha_lista[1] = 20  # Atualiza o valor no índice 1
print(minha_lista)  # Saída: [1, 20, 3, 4, 5]

#append(): Adiciona um único elemento ao final da lista
minha_lista.append(6)
print(minha_lista)  # Saída: [1, 20, 3, 4, 5, 6]

#insert(): Insere um elemento em uma posição específica.
minha_lista.insert(2, 15)  # Insere o 15 no índice 2
print(minha_lista)  # Saída: [1, 20, 15, 3, 4, 5, 6]

extend(): Adiciona múltiplos elementos (de outra lista ou iterável).
minha_lista.extend([7, 8, 9])
print(minha_lista)  # Saída: [1, 20, 15, 3, 4, 5, 6, 7, 8, 9]

#remove(): Remove a primeira ocorrência de um elemento.
minha_lista.remove(15)
print(minha_lista)  # Saída: [1, 20, 3, 4, 5, 6, 7, 8, 9]

#pop(): Remove e retorna o elemento em um índice específico.
ultimo = minha_lista.pop()  # Remove o último elemento
print(ultimo)  # Saída: 9
print(minha_lista)  # Saída: [1, 20, 3, 4, 5, 6, 7, 8]

#clear(): Remove todos os elementos da lista.
minha_lista.clear()
print(minha_lista)  # Saída: []

for elemento in minha_lista:
    print(elemento)

lista = [10, 20, 30, 40, 50]
print(lista[1:4])  # Saída: [20, 30, 40] (do índice 1 ao 3)
print(lista[:3])  # Saída: [10, 20, 30] (do início ao índice 2)
print(lista[::2])  # Saída: [10, 30, 50] (passo de 2)

#len(): Retorna o tamanho da lista.
print(len(lista))  # Saída: 5
sort(): Ordena a lista em ordem crescente.

#sort(): Ordena a lista em ordem crescente.
lista.sort()
print(lista)  # Saída: [10, 20, 30, 40, 50]
reverse(): Inverte a ordem da lista.

#reverse(): Inverte a ordem da lista.
lista.reverse()
print(lista)  # Saída: [50, 40, 30, 20, 10]

#count(): Conta quantas vezes um elemento aparece.
print(lista.count(30))  # Saída: 1
index(): Retorna o índice da primeira ocorrência de um elemento.

#index(): Retorna o índice da primeira ocorrência de um elemento.
print(lista.index(40))  # Saída: 1