# Questão 31:

numero = int(input("Digite um número de 1 a 5: "))

if numero == 3:
    print("O número é igual a 3")
else:
    print("O número não é 3")

# Questão 32: pular esta

# Questão 33:

valor = float(input("Digite o valor do produto: "))

desconto = valor * 0.10
valor_final = valor - desconto

print(f"Valor com desconto: R$ {valor_final}")

# Questão 34:

numero = int(input("Digite um número: "))

if numero > 0:
    print("Positivo")
elif numero < 0:
    print("Negativo")
else:
    print("Zero")

# Questão 35:

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

if num1 * num2 == 20:
    print("A multiplicação é igual a 20")
else:
    print("A multiplicação não é 20")

# Questão 36:

mes = int(input("Digite um número de 1 a 12: "))

if mes == 1:
    print("Janeiro")
elif mes == 2:
    print("Fevereiro")
elif mes == 3:
    print("Março")
elif mes == 4:
    print("Abril")
elif mes == 5:
    print("Maio")
elif mes == 6:
    print("Junho")
elif mes == 7:
    print("Julho")
elif mes == 8:
    print("Agosto")
elif mes == 9:
    print("Setembro")
elif mes == 10:
    print("Outubro")
elif mes == 11:
    print("Novembro")
elif mes == 12:
    print("Dezenbro")

# Questão 37:

numero = int(input("Digite um número: "))

if numero % 2 == 0 or numero % 5 == 0:
    print("É múltiplo de 2 ou de 5")
else:
    print("Não é múltiplo de 2 nem de 5")

# Questão 38:


altura = float(input("Digite sua altura em metros: "))

if altura > 1.75:
    print("Altura acima de 1.75m")
else:
    print("Altura igual ou abaixo de 1.75m")

# Questão 39:

senha = input("Digite a senha: ")

if senha == "1234":
    print("Acesso permitido")
else:
    print("Senha incorreta")

# Questão 40:

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

if num1 == num2 == num3:
    print("Todos os números são iguais")
else:
    print("Os números não são todos iguais")
