
#O range pode ser usado para gerar números sequenciais:
for i in range(5):  # Gera números de 0 a 4
    print(i)

for i in range(2, 6):  # Gera números de 2 a 5
    print(i)

for i in range(0, 10, 2):  # Gera números de 0 a 9 com passo de 2
    print(i)

#Passo (Step): Pulando Números
for i in range(10, 0, -1):  # Conta de 10 até 1
    print(i)

#Você pode transformar um range em uma lista usando a função list():
numeros = list(range(5))  # Converte para uma lista [0, 1, 2, 3, 4]
print(numeros)

#Exercicios
#Imprima os números pares de 1 a 20:
for i in range(2,21,2):
    print(i)

#Gere uma sequência decrescente de 20 até 0 com passo de 2:
for i in range(20, -1, -2):
    print(i)

#Imprima os números múltiplos de 3 entre 0 e 30:
for i in range(0, 31, 3):
    print(i)

#Exiba os números de 50 a 60 (inclusive):
for i in range(50, 61):
    print(i)

