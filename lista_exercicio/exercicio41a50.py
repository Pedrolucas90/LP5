# Questão 41:


numero = int(input("Digite um número inteiro positivo: "))

for i in range(1, numero + 1):
    print(i)

# Questão 42:

soma = 0

for i in range(5):
    numero = int(input("Digite um número: "))
    soma += numero

print("Soma total:", soma)

# Questão 43:

vezes = int(input("Quantas vezes deseja repetir a mensagem? "))

for i in range(vezes):
    print("Olá, mundo!")


# Questão 44:

for i in range(10):
    numero = int(input("Digite um número: "))
    
    if numero % 2 == 0:
        print("Número par:", numero)


# Questão 45:


maior = None

for i in range(5):
    numero = float(input("Digite um número: "))
    
    if maior is None or numero > maior:
        maior = numero

print("Maior número:", maior)


# Questão 46:

soma = 0

for i in range(10):
    numero = float(input("Digite um número: "))
    soma += numero

media = soma / 10

print("A média é:", media)

# Questão 47:

numero = int(input("Digite um número: "))

for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")


# Questão 48:

palavra = input("Digite uma palavra: ")

for letra in palavra:
    print(letra)


# Questão 49:

maior = 0

for i in range(7):
    numero = int(input("Digite um número: "))
    
    if numero > 10:
        maior += 1

print("Quantidade de números maiores que 10:", maior)


# Questão 50:

numero = int(input("Digite um número: "))

for i in range(numero, 0, -1):
    print(i)