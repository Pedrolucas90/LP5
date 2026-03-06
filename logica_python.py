# Criando variaveis 

nome = 'Pedro'
sobrenome = 'Silva'
idade = 19
altura = 1.78
adulto = True

# Descrevendo no console.

print(nome)
print(sobrenome)
print(idade)
print(altura)
print(adulto)

# Concatenado informações 
print('Meu nome é' , nome)
print('Meu sobrenome é '+ sobrenome)
print('Meu nome completo é', nome, sobrenome)
print('Minha idade é {} e minha altura é {}'.format(idade, altura))


# Maneira moderna(baiana) de concatenar

print(f'Meu nome é {nome} e tenho {idade} de idade') 

# Verificando o tipo da variavel 
print(type(nome))
print(type(sobrenome))
print(type(idade))
print(type(altura))
print(type(adulto))

# Expressões numericas 

numero1 = 10
numero2 = 5

soma = numero1 + numero2
sub = numero1 - numero2
mult = numero1 * numero2
div = numero1 / numero2

print(f'A soma é {soma}')
print(f'A sub é {sub}')
print(f'A mult é {mult}')
print(f'A div é {div}')

expressão = numero1 / (numero2* numero2) + numero1

print(expressão)


# Outras operações 

Potencia = numero1**2
div_exata = numero1//4

print(div_exata)
print(Potencia)