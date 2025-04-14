texto1 = 'Olá, mundo!'
texto2 = "Python é incrível!"
print(texto1, texto2)

texto_multilinha = '''Este é um
texto que ocupa
várias linhas.'''
print(texto_multilinha)

texto = "Python"
print(texto[0])  # Saída: P (primeiro caractere)
print(texto[-1])  # Saída: n (último caractere)
print(texto[1:4])  # Saída: yth (corte do índice 1 ao 3)

texto = "PYTHON"
print(texto.lower())  # Saída: python

print(texto.upper())  # Saída: PYTHON

#remove espaços
texto = "  Olá!  "
print(texto.strip())  # Saída: Olá!

texto = "Eu gosto de Java."
print(texto.replace("Java", "Python"))  # Saída: Eu gosto de Python.

#split(): Divide a string em uma lista, com base em um delimitador.
texto = "Maçã, Banana, Laranja"
frutas = texto.split(", ")
print(frutas)  # Saída: ['Maçã', 'Banana', 'Laranja']

#interpolação de string
nome = "João"
idade = 25
print(f"{nome} tem {idade} anos.")  # Saída: João tem 25 anos.

primeira = "Olá, "
segunda = "mundo!"
mensagem = primeira + segunda
print(mensagem)  # Saída: Olá, mundo!

texto = "Python"
print(len(texto))  # Saída: 6
print("Py" in texto)  # Saída: True

