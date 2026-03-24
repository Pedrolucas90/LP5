# Questão 1: 

numero = int(input("Digite um número de 1 a 3: "))

if numero == 1:
    print("um")
elif numero == 2:
    print("dois")
elif numero == 3:
    print("três")


# Questão 2: 

numero = int(input("Digite um número: "))

if numero > 10:
    print("O número é maior que 10")
else:
    print("O número não é maior que 10")



# Questão 3: 

numero = int(input("Digite um número de 1 a 7 correspondete ao dia da semana: "))

if numero == 1:
    print("domingo")
elif numero == 2:
    print("segunda")
elif numero == 3:
    print("terça")
elif numero == 4:
    print("quarta")
elif numero == 5:
    print("quinta")
elif numero == 6:
    print("sexta")
elif numero == 7:
    print("sábado")


# Questão 4: 

cor = (input("Escolha uma cor (vermelho, verde, azul): "))

if cor == "vermelho":
    print("Você escolheu a cor vermelho!")
elif cor == "verde":
    print("Você escolheu a cor verde!")
elif cor == "azul":
    print("Você escolheu a cor azul!")


# Questão 5: 

numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))

if numero1 % 2 == 0 and numero2 % 2 == 0:
    print("Ambos são pares")
elif numero1 % 2 == 0 or numero2 % 2 == 0:
    print("Apenas um dos números é par")
else:
    print("Nenhum dos números é par")


# Questão 6: 

print('0 - soma')
print('1 - subtrair')
print('2 - multiplicar')
print('3 - dividir')

opcao = int(input('O que deseja  realizar: '))

match opcao:
    case 0:
        print("Você escolheu somar!")
    
    case 1:
        print("Você escolheu subtrair")
   
    case 2:
        print("Você escolheu mutiplicar")
        
    case 3:
        print("Você escolheu dividir")
    
    case _:
        print("opção invalida!")

num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))

match opcao:
    case 0:
        resultado = num1 + num2
        print(f"Resultado da soma é: {resultado}")

    case 1:
        resultado = num1 - num2
        print(f"Resultado da subtração é: {resultado}")

    case 2:
        resultado = num1 * num2
        print(f"Resultado da multiplicação é: {resultado}")
        
    case 3:
        if num2 != 0:
            resultado = num1 / num2
            print(f"Resultado da divição é: {resultado}")

    case _:
        print("Opção invalida!")


# Questão 7: 

nota = int(input("Digite uma nota de 0 a 10: "))

if nota < 0 > 10:
    print("Nota inválida")
elif nota <= 5:
    print("Baixa")
elif nota <= 6:
    print("Média")
else:
    print("Alta")


# Questão 8: 

estado = input("Digite seu estado civil (solteiro, casado, divorciado, viúvo): ")

if estado == "solteiro":
    print("Você é solteiro(a).")
elif estado == "casado":
    print("Você é casado(a).")
elif estado == "divorciado":
    print("Você é divorciado(a).")
elif estado == "viuvo":
    print("Você é viuvo(a).")
else:
    print("Estado civil invalido.")

# Questão 9: 

numero = int(input("Digite um número: "))

if numero % 2 == 0:
    print("O número é par")
else:
    print("O número é ímpar")

# Questão 10: 

idade = int(input("Digite sua idade: "))

if idade <= 0:
    print("Idade invalida") 
elif idade >= 17:
    print("Você e menor de idade")
else: 
    print("Você e maior de idade!")


