# Classe Pai
class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def exibir_informacoes(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}"


# Classe Filha
class Carro(Veiculo):
    def __init__(self, marca, modelo, numero_portas):
        super().__init__(marca, modelo)
        self.numero_portas = numero_portas

    def exibir_informacoes(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}, Portas: {self.numero_portas}"


# Entrada dos dados digitados pelo usuário
marca = input("Digite a marca do carro: ")
modelo = input("Digite o modelo do carro: ")
numero_portas = int(input("Digite o número de portas: "))

# Criação do objeto com base nos dados digitados
carro1 = Carro(marca, modelo, numero_portas)

# Exibição do resultado
print("\nInformações do veículo:")
print(carro1.exibir_informacoes())
