#O zip em Python é uma função embutida que permite combinar dois ou 
#mais iteráveis (como listas, tuplas, etc.) em pares ou grupos 
#correspondentes. Ele é muito útil para unir dados de coleções 
#diferentes em um formato iterável.

#Exemplo Básico: Combinar Duas Listas
nomes = ["Ana", "Carlos", "Maria"]
idades = [25, 30, 22]

# Emparelhando nomes e idades
dados = zip(nomes, idades)

# Convertendo para lista
print(list(dados))  # Saída: [('Ana', 25), ('Carlos', 30), ('Maria', 22)]


nomes = ["Ana", "Carlos", "Maria"]
idades = [25, 30, 22]
cidades = ["São Paulo", "Rio de Janeiro", "Belo Horizonte"]

dados = zip(nomes, idades, cidades)
print(list(dados))
# Saída: [('Ana', 25, 'São Paulo'), ('Carlos', 30, 'Rio de Janeiro'), ('Maria', 22, 'Belo Horizonte')]


#ocê pode usar zip para combinar duas listas em um dicionário:
chaves = ["nome", "idade", "cidade"]
valores = ["Ana", 25, "São Paulo"]

dicionario = dict(zip(chaves, valores))
print(dicionario)  # Saída: {'nome': 'Ana', 'idade': 25, 'cidade': 'São Paulo'}



#Usando o zip em Loops
#O zip pode ser útil em loops para processar iteráveis em paralelo:
nomes = ["Ana", "Carlos", "Maria"]
idades = [25, 30, 22]

for nome, idade in zip(nomes, idades):
    print(f"{nome} tem {idade} anos.")