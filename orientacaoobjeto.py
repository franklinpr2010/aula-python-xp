#Classe
class Animal:
    def __init__(self, nome, especie):
        self.nome = nome
        self.especie = especie

    def emitir_som(self):
        print(f"{self.nome} faz som!")

# Criando objetos
gato = Animal("Mia", "Gato")
cachorro = Animal("Bob", "Cachorro")

# Usando métodos
gato.emitir_som()  # Output: Mia faz som!
cachorro.emitir_som()  # Output: Bob faz som!

#Herança
class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def detalhes(self):
        print(f"Marca: {self.marca}, Modelo: {self.modelo}")
        print("A Marca é {} e o modelo é {}".format(self.marca, self.modelo))

class Carro(Veiculo):
    def __init__(self, marca, modelo, portas):
        super().__init__(marca, modelo)
        self.portas = portas

    def detalhes(self):
        super().detalhes()
        print(f"Portas: {self.portas}")

# Criando um objeto da classe Carro
meu_carro = Carro("Toyota", "Corolla", 4)
meu_carro.detalhes()

#Polimorfismo
class Forma:
    def calcular_area(self):
        pass

class Retangulo(Forma):
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def calcular_area(self):
        return self.largura * self.altura

class Circulo(Forma):
    def __init__(self, raio):
        self.raio = raio

    def calcular_area(self):
        return 3.14 * self.raio ** 2

formas = [Retangulo(4, 5), Circulo(3)]

for forma in formas:
    print(f"Área: {forma.calcular_area()}")


