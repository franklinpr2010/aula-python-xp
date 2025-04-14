numero = "42"  # Tipo string
numero_inteiro = int(numero)  # Converte para inteiro
print(numero_inteiro)  # Resultado: 42

nome = "João"
idade = 30
altura = 1.80
print(f"{nome} tem {idade} anos e mede {float(altura)} metros.")  

a=10
b=5
soma = a + b
print (f"A soma de {a} e {b} é {soma}.")  # Resultado: A soma de 10 e 5 é 15.

#Exemplo 2: Atribuição do mesmo valor a várias variáveis
x = y = z = 100
print(x)  # Saída: 100
print(y)  # Saída: 100
print(z)  # Saída: 100

#Exemplo 4: Desempacotamento de listas ou tuplas
valores = (1, 2, 3)
x, y, z = valores
print(x)  # Saída: 1
print(y)  # Saída: 2
print(z)  # Saída: 3


#Exemplo 5: Combinando múltiplas declarações
a, b, c = 1, 2, 3; d = 4
print(a, b, c, d)  # Saída: 1 2 3 4