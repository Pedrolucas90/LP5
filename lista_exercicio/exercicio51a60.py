# Questão 51:

soma = 0

while True:
    numero = int(input("Digite um número (0 para parar): "))
    
    if numero == 0:
        break
    
    soma += numero

print("Soma total dos numeros inseridos:", soma)


# Questão 52:

senha = ""

while senha != "1234":
    senha = input("Digite a senha: ")

print("Acesso permitido!")


# Questão 53:

numero = int(input("Digite um número: "))

while numero > 0:
    print(numero)
    numero -= 1

# Questão 54:

while True:
    numero = int(input("Digite um número: "))
    
    if numero < 0:
        break


# Questão 55:

numero = int(input("Digite um número maior que 100: "))

while numero <= 100:
    numero = int(input("Número inserio e menor que 100! Digite novamente: "))

print("Número válido!")

 
# Questão 56:

vezes = int(input("Quantas vezes deseja repetir a mensagem? "))
contador = 0

while contador < vezes:
    print("Olá, mundo!")
    contador += 1


# Questão 57:


numero_secreto = 10 
palpite = 0

while palpite != numero_secreto:
    palpite = int(input("Adivinhe o número (1 a 10): "))

print("Parabéns! Você acertou!")

# Questão 58:

palavra = ""

while palavra != "sair":
    palavra = input("Digite uma palavra ou 'sair' para encerrar: ")


# Questão 59:

while True:
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    
    if num1 > num2:
        print("Correto! O primeiro é maior.")
        break
    else:
        print("Tente novamente.")


# Questão 60:

numero = int(input("Digite um número: "))

i = 1

while i <= numero:
    if numero % i == 0:
        print(i)
    i += 1
