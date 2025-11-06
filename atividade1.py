# Pergunta o nome e guarda na variavel 'nome'
nome = input("Qual é o seu nome? ")

# Pergunta a idade do usuário
idade_texto = input("Qual é a sua idade? ")

# Converte a idade de texto para número 
idade_numero = int(idade_texto)

# Cria a lógica condicional
if idade_numero >= 18:
    # Mensagem para usuario maior de idade
    print(f"Olá, {nome}, você é maior de idade.")
else:
    # Mensagem pra usuario menor de idade
    print(f"Olá, {nome}, você é menor de idade.")
