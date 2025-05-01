dados_pessoa = {
    "nome": "Ana",
    "idade": 28,
    "cidade": "São Paulo"
}
print(dados_pessoa)  # Saída: {'nome': 'Ana', 'idade': 28, 'cidade': 'São Paulo'}

#Use a chave para acessar o valor correspondente:
print(dados_pessoa["nome"])  # Saída: Ana
print(dados_pessoa["idade"])  # Saída: 28

#Você pode adicionar novas chaves ou atualizar valores existentes:
dados_pessoa["profissão"] = "Engenheira"  # Adicionando um novo par chave-valor
dados_pessoa["idade"] = 29  # Atualizando o valor existente
print(dados_pessoa)

#Use métodos como pop() ou del para remover itens:
dados_pessoa.pop("cidade")  # Remove o item com a chave "cidade"
print(dados_pessoa)
del dados_pessoa["profissão"]  # Outra maneira de remover
print(dados_pessoa)

# Iterar pelas chaves
for chave in dados_pessoa:
    print(chave)

# Iterar pelos valores
for valor in dados_pessoa.values():
    print(valor)

# Iterar pelas chaves e valores
for chave, valor in dados_pessoa.items():
    print(f"{chave}: {valor}")

#Você pode ter dicionários dentro de dicionários:
empresa = {
    "funcionarios": {
        "João": {"idade": 30, "cargo": "Analista"},
        "Maria": {"idade": 25, "cargo": "Designer"}
    }
}
print(empresa["funcionarios"]["João"]["cargo"])  # Saída: Analista

#keys(): Retorna todas as chaves.
print(dados_pessoa.keys())  # Saída: dict_keys(['nome', 'idade'])

#items(): Retorna pares chave-valor como tuplas.
print(dados_pessoa.items())  # Saída: dict_items([('nome', 'Ana'), ('idade', 29)])

#values(): Retorna todos os valores.
print(dados_pessoa.values())  # Saída: dict_values(['Ana', 29])

#get(): Retorna o valor de uma chave, mas evita erros se a chave não existir.
print(dados_pessoa.get("cidade", "Chave não encontrada"))  # Saída: Chave não encontrada

#clear(): Remove todos os itens do dicionário.
dados_pessoa.clear()
print(dados_pessoa)  # Saída: {}


