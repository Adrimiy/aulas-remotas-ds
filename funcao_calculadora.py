def calculadora(numero1, numero2, operacao): # Operações para o calculo ser realizado
    if operacao == "+":
        return numero1 + numero2
    elif operacao == "-":
        return numero1 - numero2
    elif operacao == "*":
        return numero1 * numero2
    elif operacao == "/":
       
        if numero2 != 0: # Ve se o segundo número digitado é diferente de zero
            return numero1 / numero2
        else:
            return "Erro: divisão por zero!"
    else:
        return "Operação inválida!"

# Entrada de dados digitados pelo usuário
numero1 = float(input("Digite um número: "))
numero2 = float(input("Digite um segundo número: "))
operacao = input("Escolha uma operação (+, -, *, /): ")

# Resultado
print("Resultado:", calculadora(numero1, numero2, operacao))
