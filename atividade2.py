# Pede ao usuário um número e o converte para inteiro
numero_str = input("Digite um número para ver a tabuada: ")
numero = int(numero_str)

print(f"---Tabuada do {numero}---")

# Cria um loop 'for' que vai de 1 até 10
# A variável 'i' vai assumir o valor de 1, depois 2, depois 3... até 10
for i in range(1, 11):
# Calcula o resultado da multiplicação
    resultado = numero * i
# Imprime o resultado formatado
    print(f"{numero} x {i} = {resultado}")