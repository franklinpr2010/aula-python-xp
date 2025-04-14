meu_conjunto = {1, 2, 3, 4}
print(meu_conjunto)  # Saída: {1, 2, 3, 4}

#Usando a função set():
meu_conjunto = set([1, 2, 3, 3])
print(meu_conjunto)  # Saída: {1, 2, 3} (duplicatas são removidas)

#Adicionar elementos (add):
meu_conjunto = {1, 2, 3}
meu_conjunto.add(4)
print(meu_conjunto)  # Saída: {1, 2, 3, 4}

#Remover elementos (remove)
meu_conjunto = {1, 2, 3}
meu_conjunto.remove(2)
print(meu_conjunto)  # Saída: {1, 3}

#Verificar se um elemento está no conjunto:
print(3 in meu_conjunto)  # Saída: True

#União (union): Junta os elementos de dois conjuntos.
conjunto_a = {1, 2, 3}
conjunto_b = {3, 4, 5}
print(conjunto_a.union(conjunto_b))  # Saída: {1, 2, 3, 4, 5}
print(conjunto_a.intersection(conjunto_b))  # Saída: {3}
#Diferença (difference): Elementos que estão em um conjunto mas não no outro.
print(conjunto_a.difference(conjunto_b))  # Saída: {1, 2}
#Diferença simétrica (symmetric_difference): Elementos que estão em um dos conjuntos, mas não em ambos.
print(conjunto_a.symmetric_difference(conjunto_b))  # Saída: {1, 2, 4, 5}
#len(): Retorna o número de elementos no conjunto.
print(len(conjunto_a))  # Saída: 3
#clear(): Remove todos os elementos do conjunto.
conjunto_a.clear()
print(conjunto_a)  # Saída: set()
#discard(): Remove um elemento sem causar erro caso ele não exista.
conjunto_a.discard(10)  # Não gera erro mesmo se o elemento não estiver no conjunto.

#Se precisar de conjuntos imutáveis, você pode usar o tipo frozenset:
conjunto_imutavel = frozenset([1, 2, 3])
print(conjunto_imutavel)  # Saída: frozenset({1, 2, 3})
# conjunto_imutavel.add(4)  # Isso causará um erro, pois o conjunto é imutável.


