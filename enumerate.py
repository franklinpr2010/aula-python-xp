
#O enumerate em Python é uma função embutida muito útil que permite iterar 
#sobre um iterável (como listas, tuplas ou strings) enquanto acompanha 
#os índices dos elementos. É ideal para casos em que você precisa tanto 
#do índice quanto do valor durante um loop.
#Você pode usar enumerate para obter índices e valores simultaneamente:

frutas = ["Maçã", "Banana", "Laranja"]

for indice, fruta in enumerate(frutas):
    print(f"{indice}: {fruta}")


#Você pode ajustar o índice inicial usando o argumento start:
frutas = ["Maçã", "Banana", "Laranja"]

for indice, fruta in enumerate(frutas, start=1):
    print(f"{indice}: {fruta}")

#O enumerate retorna um objeto iterável que pode ser convertido para uma lista ou outro tipo de coleção:
frutas = ["Maçã", "Banana", "Laranja"]
enumeracao = list(enumerate(frutas))
print(enumeracao)
# Saída: [(0, 'Maçã'), (1, 'Banana'), (2, 'Laranja')]

texto = "Python"
for indice, letra in enumerate(texto):
    print(f"{indice}: {letra}")

#Utilize enumerate para acompanhar os índices enquanto verifica números ímpares e pares:
numeros = [10, 15, 20, 25]

for indice, numero in enumerate(numeros):
    tipo = "par" if numero % 2 == 0 else "ímpar"
    print(f"Índice {indice}: {numero} é {tipo}.")

