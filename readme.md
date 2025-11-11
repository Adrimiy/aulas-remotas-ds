# Projeto: Atividades de Python

Esse projeto contém quatro programas desenvolvidos em **Python** para praticar a lógica de programação.
Cada código faz uma tarefa diferente e serve como exercício de aprendizado.

---

## Descrição dos códigos

### Verificador de Maioridade (`atividade1.py`)
Esse programa pergunta o **nome** e a **idade** do usuário, e mostra se ele é **maior ou menor de idade**.

#### Lógica utilizada:
- Usa o comando `input()` para receber dados do usuário.  
- Converte o texto da idade em número com `int()`.  
- Utiliza uma **estrutura condicional `if`** para verificar se a idade é maior ou igual a 18.

---

### Tabuada (`atividade2.py`)
Esse programa pede ao usuário que ele digite um número e depois mostra a **tabuada completa de 1 a 10** do número digitado pelo usuário.

#### Lógica utilizada:
- Recebe um número com `input()` e converte para inteiro.  
- Usa um **laço `for`** com `range(1, 11)` para repetir de 1 até 10.  
- Em cada repetição, calcula o resultado e exibe formatado com `print()`.

---

### Calculadora (`funcao_calculadora.py`)
O programa pede ao usuário que ele digite dois números e escolha uma operação **(+, -, *, /)**, para realizar o calculo dos dois números que foram digitados pelo usuário.

#### Lógica utilizada:
- Recebe dois números digitados pelo usuário com `input()` e converte para decimal com `float()`
- Recebe também a operação desejada **(+, -, *, /)**.
- A função `calculadora()` usa estruturas condicionais **if / elif / else** para identificar qual operação foi escolhida.
- Executa o cálculo correspondente e retorna o resultado.
- O programa exibe o resultado final com `print()`.
- Caso a operação digitada não exista, mostra a mensagem **"Operação inválida!"**.

---

### Herança (`heranca_veiculos.py`)

O programa pede ao usuário que digite as informações de um carro (marca, modelo e número de portas) e exibe esses dados na tela.
Ele utiliza orientação a objetos com herança, onde a classe Carro herda características da classe Veiculo.

#### Lógica utilizada:

- Define uma classe pai **(Veiculo)** com os atributos marca e modelo.
- Define uma classe filha **(Carro)** que herda de Veiculo e adiciona o atributo numero_portas.
- Utiliza o método especial `__init__()` para inicializar os atributos das classes.
- A classe filha usa `super()` para chamar o construtor da classe pai e aproveitar seu código.
- O programa pede ao usuário que digite as informações do carro usando `input()`.
- Cria um objeto da classe **Carro** com os dados digitados.
- Exibe as informações completas do carro através do método `exibir_informacoes()`.

---
## Programas utilizados
- **Python 3.14**
- **Visual Studio Code**
- **GitHub** 

---

## Autor 
Desenvolvido por Adrielly Trindade Martins Paixão