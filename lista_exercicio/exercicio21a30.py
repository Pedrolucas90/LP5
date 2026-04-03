# Questão 21:

numero = int(input("Digite um número: "))

if numero > 10:
    print("O número é maior que 10")
elif numero == 10: 
    print("O número é igual a 10")
else:
    print("O número é menor que 10")

# Questão 22:

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))

if n1 > n2:
    print("O primeiro número é maior")
else:
    print("O primeiro número não é maior")


# Questão 23:

palavra = input("Digite uma palavra: ")

if palavra == "python":
    print("Você digitou Python!")
else:
    print("Não é Python")

# Questão 24:

cidade = input("Digite o nome de uma cidade: ")

if cidade == "brasilia":
    print("É a capital do Brasil")
else:
    print("Não é a capital do Brasil")

# Questão 25:

numero = int(input("Digite um número de 0 a 20: "))

if 10 <= numero <= 15:
    print("Está entre 10 e 15")
else:
    print("Não está entre 10 e 15")

# Questão 26:

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

if num1 % 5 == 0 and num2 % 5 == 0:
    print("Ambos são múltiplos de 5")
else:
    print("Nem ambos são múltiplos de 5")

# Questão 27:

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))

maior = max(num1, num2, num3)

print("O maior número é:", maior)

# Questão 28:

palavra = input("Digite uma palavra: ")

if len(palavra) > 5:
    print("A palavra tem mais de 5 letras")
else:
    print("A palavra tem 5 letras ou menos")

# Questão 29:

numero = int(input("Digite um número: "))

if numero % 3 == 0:
    print("É múltiplo de 3")
else:
    print("Não é múltiplo de 3")

# Questão 30:

idade = int(input("Digite sua idade: "))

if idade >= 16:
    print("Você pode votar")
else:
    print("Você não pode votar")