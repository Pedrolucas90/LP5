# nome = 'Pedro'
# print(f'Meu nome é: {nome}')

# nome = 'Marcelo'
# print(f'Meu nome é: {nome}')

# nomes = ['Pedro', 'Marcelo']

# print(nomes[0])
# print(nomes[1])

apostolos = ['Matheus', 'Tiago', 'Lucas', 'Judas', 'Pedro']

# # Percorrendo a lista posição por posição
# for apostolo in apostolos:
#     print(apostolo)

# Adicionando item no final da lista
print(apostolos)
apostolos.append('João')
print(apostolos)

# Adicionando item na posição desejada. Exemplo posição 2 
apostolos.insert(2,'Simão')
print(apostolos)

# Expandindo a lista com novos elementos 
cavaleiros = ['Seiya', 'Shiryu']
print(cavaleiros)

cavaleiros.extend(['Ikki', 'Yoga', 'Shun'])
print(cavaleiros)

#Excluindo iteins de uma lista 

cavaleiros.pop()
print(cavaleiros)

cavaleiros.pop(0)
print(cavaleiros)

# Excluindo por valor 

print(apostolos)

apostolos.remove('Judas')
print(apostolos)

alunos = ['Victor', 'Lucas', 'Gabriel', 'Lucas', 'Amanda', 'Daniel']
print(alunos)
# alunos.remove('Lucas')
# print(alunos)

for indice ,aluno in enumerate(alunos):
    if aluno == 'Lucas':
        alunos.pop(indice)
print(alunos)


numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
impares = []
pares = []

for indice ,numero in enumerate(numeros):
    if numero % 2 != 0:
        impares.append(numero) 
    elif numero % 2 == 0:
        pares.append(numero)

print(impares)
print(pares)


print(apostolos)
apostolos.sort()
print(apostolos)
apostolos.reverse()
print(apostolos)

print(cavaleiros)
cavaleiros.clear()
print(cavaleiros)

# print(pares)

# del pares
# print(pares)
