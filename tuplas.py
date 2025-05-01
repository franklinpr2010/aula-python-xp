# Criando tuplas
tupla1 = (1, 2, 3)
tupla2 = "a", "b", "c"  # Parênteses são opcionais
tupla_vazia = ()  # Tupla vazia

print(tupla1)  # Saída: (1, 2, 3)
print(tupla2)  # Saída: ('a', 'b', 'c')

#Os elementos de uma tupla podem ser acessados usando índices:
tupla = (10, 20, 30, 40)
print(tupla[1])  # Saída: 20 (índice 1)
print(tupla[-1])  # Saída: 40 (último elemento)

#Fatiamento (slicing):
print(tupla[1:3])  # Saída: (20, 30)
print(tupla[:2])   # Saída: (10, 20)
print(tupla[::2])  # Saída: (10, 30) (passo de 2)

#Concatenar tuplas: Você pode juntar duas tuplas com o operador +:
nova_tupla = (1, 2) + (3, 4)
print(nova_tupla)  # Saída: (1, 2, 3, 4)

#Repetir tuplas: Use o operador * para repetir os elementos:
print((1, 2) * 3)  # Saída: (1, 2, 1, 2, 1, 2)

#Verificar se um elemento está na tupla:
print(20 in tupla)  # Saída: True
print(50 in tupla)  # Saída: False

print(len(tupla))  # Saída: 4

#count(): Conta quantas vezes um valor aparece na tupla.
tupla_repetida = (1, 2, 2, 3)
print(tupla_repetida.count(2))  # Saída: 2

#index(): Retorna o índice da primeira ocorrência de um valor.
print(tupla.index(30))  # Saída: 2

#tuple(): Converte outros iteráveis (como listas) em tuplas.
lista = [10, 20, 30]
tupla_convertida = tuple(lista)
print(tupla_convertida)  # Saída: (10, 20, 30)

tupla = ('franklin', 'peixoto', 'roza')
print(tupla[-1])

#Você pode criar tuplas dentro de outras tuplas:
tupla_aninhada = ((1, 2), (3, 4))
print(tupla_aninhada[0])  # Saída: (1, 2)
print(tupla_aninhada[0][1])  # Saída: 2

