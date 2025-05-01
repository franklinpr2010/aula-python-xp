def saudacao():
    print("Olá, seja bem-vindo!")

saudacao()  # Saída: Olá, seja bem-vindo!


def saudacao(nome):
    print(f"Olá, {nome}!")
    
saudacao("Ana")  # Saída: Olá, Ana!


def soma(a, b):
    return a + b

resultado = soma(3, 5)
print(resultado)  # Saída: 8

def saudacao(nome="Visitante"):
    print(f"Olá, {nome}!")
saudacao()  # Saída: Olá, Visitante!
saudacao("Carlos")  # Saída: Olá, Carlos!


def soma(*numeros):
    return sum(numeros)
print(soma(1, 2, 3, 4))  # Saída: 10

#Use **kwargs para passar um número variável de argumentos nomeados como dicionário.
def exibir_informacoes(**dados):
    for chave, valor in dados.items():
        print(f"{chave}: {valor}")

#Funções Lambda
#São funções anônimas e simples que podem ser usadas em uma única linha. São definidas com a palavra-chave lambda.
exibir_informacoes(nome="Ana", idade=25, cidade="São Paulo")
dobro = lambda x: x * 2
print(dobro(5))  # Saída: 10


#Variáveis Globais: Definidas fora da função e acessíveis em todo o código.
x = "global"

def minha_funcao():
    x = "local"
    print(x)  # Saída: local

minha_funcao()
print(x)  # Saída: global


#Função para calcular o fatorial de um número:
def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n - 1)

print(fatorial(5))  # Saída: 120


#Função para verificar se um número é par:
def e_par(numero):
    return numero % 2 == 0

print(e_par(4))  # Saída: True
print(e_par(7))  # Saída: False


