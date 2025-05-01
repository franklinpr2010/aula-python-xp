frutas = ["Maçã", "Banana", "Laranja"]
for fruta in frutas:
    print(fruta)

for i in range(5):  # Itera de 0 a 4
    print(i)

    texto = "Python"
for letra in texto:
    print(letra)

contador = 0
while contador < 5:
    print(contador)
    contador += 1  # Incremento

numero = 10
while numero > 0:
    print(f"Número atual: {numero}")
    numero -= 2  # Redução

#O comando break termina o loop antes que ele complete todas as iterações.
for i in range(10):
    if i == 5:
        break  # Sai do loop quando `i` for igual a 5
    print(i)

#Você pode criar loops dentro de loops para realizar operações mais complexas.
for i in range(3):
    for j in range(2):
        print(f"i: {i}, j: {j}")

numero = 1
while numero < 100:
    print(numero)
    numero *= 2  # Multiplica por 2