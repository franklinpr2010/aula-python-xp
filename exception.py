try:
    numero = int(input("Digite um número: "))
    print(f"O dobro do número é {numero * 2}.")
except ValueError:
    print("Você deve digitar um número válido!")


try:
    arquivo = open("dados.txt", "r")
    conteudo = arquivo.read()
    print(conteudo)
except FileNotFoundError:
    print("O arquivo não foi encontrado.")
else:
    print("Leitura do arquivo foi um sucesso!")
finally:
    arquivo.close()  # Fecha o arquivo, independentemente do que aconteceu



#Capturando Várias Exceções
#Você pode capturar diferentes tipos de exceções com múltiplos blocos except:
try:
    x = int(input("Digite o numerador: "))
    y = int(input("Digite o denominador: "))
    resultado = x / y
    print(f"O resultado é {resultado}.")
except ValueError:
    print("Erro: Digite apenas números!")
except ZeroDivisionError:
    print("Erro: Divisão por zero não é permitida!")

#Lançando Exceções: raise
#Você pode levantar manualmente uma exceção usando a palavra-chave raise.
def verificar_idade(idade):
    if idade < 18:
        raise ValueError("Idade deve ser maior ou igual a 18.")
    return "Idade válida!"

try:
    print(verificar_idade(16))
except ValueError as erro:
    print(erro)


#Definindo Exceções Personalizadas
#Você pode criar suas próprias exceções para cenários específicos:
class MinhaExcecao(Exception):
    pass

def testar(valor):
    if valor < 0:
        raise MinhaExcecao("O valor não pode ser negativo!")

try:
    testar(-5)
except MinhaExcecao as e:
    print(e)
