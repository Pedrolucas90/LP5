# Questão 11:

nome = input("Digite seu nome: ")
print(f"Seja bem-vindo(a), {nome}")


# Questão 12:

transporte = input("Escolha um transporte (carro, bicicleta, a pé): ")

if transporte == "carro":
    print("Velocidade média: 75 km/h")
elif transporte == "bicicleta":
    print("Velocidade média: 15 km/h")
elif transporte == "a pé":
    print("Velocidade média: 3 km/h")

# Questão 13:

mes = int(input("Digite o mês (1 a 12): "))

if mes in [12, 1, 2]:
    print("A estação do mês e verão")
elif mes in [3, 4, 5]:
    print("A estação do mês e outono")
elif mes in [6, 7, 8]:
    print("A estação do mês e inverno")
elif mes in [9, 10, 11]:
    print("A estação do mês e primavera")

    
# Questão 14:

n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))

if n1 + n2 > 100:
    print("A soma é maior que 100")
else:
    print("A soma não é maior que 100")


# Questão 15:

idade = int(input("Digite sua idade: "))

if 13 <= idade <= 17:
    print("Você é adolescente")
else:
    print("Você não é adolescente")

# Questão 16:

combustivel = input("Digite o tipo de combustível (gasolina, etanol, diesel): ")

if combustivel == "gasolina":
    print("Preço: R$ 7,00 por litro")
elif combustivel == "etanol":
    print("Preço: R$ 5,80 por litro")
elif combustivel == "diesel":
    print("Preço: R$ 9,00 por litro")


# Questão 17:

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

print("Soma:", num1 + num2)
print("Subtração:", num1 - num2)
print("Multiplicação:", num1 * num2)

if num2 != 0:
    print("Divisão:", n1 / n2)
else:
    print("Divisão: não é possível dividir por zero")

# Questão 18:

n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
n3 = float(input("Digite o terceiro número: "))

if n1 > 0 and n2 > 0 and n3 > 0:
    print("Todos os números são positivos")
else:
    print("Nem todos os números são positivos")

# Questão 19:

fruta = input("Digite o nome de uma fruta: ")

if fruta == "maçã" or fruta == "maca":
    print("É uma maçã")
else:
    print("Não é uma maçã")


# Questão 20:

celsius = float(input("Digite a temperatura em Celsius: "))

fahrenheit = (celsius * 9/5) + 32

print(f"Temperatura em Fahrenheit: {fahrenheit}")

