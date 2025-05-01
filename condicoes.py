idade = 18
if idade >= 18:
    print("Você é maior de idade.")


idade = 16
if idade >= 18:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")

nota = 85
if nota >= 90:
    print("Excelente!")
elif nota >= 70:
    print("Bom trabalho!")
else:
    print("Precisa melhorar.")


idade = 20
if idade >= 18:
    if idade >= 21:
        print("Você pode consumir bebidas alcoólicas nos EUA.")
    else:
        print("Você é maior de idade, mas não pode consumir bebidas alcoólicas nos EUA.")
else:
    print("Você é menor de idade.")

idade = 25
tem_carteira = True

if idade >= 18 and tem_carteira:
    print("Você pode dirigir.")
else:
    print("Você não pode dirigir.")

#OPERADOR TERNÁRIO Python permite usar uma forma compacta de if e else, chamada de operador ternário.
idade = 20
mensagem = "Maior de idade" if idade >= 18 else "Menor de idade"
print(mensagem)

#Verifique se um número é par ou ímpar:
numero = 7
if numero % 2 == 0:
    print("O número é par.")
else:
    print("O número é ímpar.")


a, b = 10, 20
if a > b:
    print(f"{a} é maior que {b}.")
elif a < b:
    print(f"{b} é maior que {a}.")
else:
    print("Os números são iguais.")
