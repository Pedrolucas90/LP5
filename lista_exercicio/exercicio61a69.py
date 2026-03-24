# Questão 61:

lista = [1, 2, 3, 4, 5]

for numero in lista:
    print(numero)

# Questão 62:

nomes = []

for i in range(3):
    nome = input("Digite um nome: ")
    nomes.append(nome)

print("Lista de nomes:", nomes) 

# Questão 63:

numeros = []

for i in range(5):
    numero = int(input("Digite um número: "))
    numeros.append(numero)


print("Lista dos numeros:", numeros, "Com a soma total em:", sum(numeros)) 


# Questão 64:

lista = []

for i in range(10):
    num = int(input("Digite um número: "))
    lista.append(num)

print("Lista:", lista)

for num in lista:
    if num % 3 == 0:
        print("Múltiplo de 3:", num)

# Questão 65:

numeros = []

for i in range(5):
    num = int(input("Digite um número: "))
    numeros.append(num)

print("Maior:", max(numeros))
print("Menor:", min(numeros))


# Questão 66:

nomes = []

while True:
    print("1 - Cadastrar")
    print("2 - Atualizar")
    print("3 - Excluir")
    print("4 - Listar")
    print("0 - Sair")

    opcao = input("Escolha a opcão desejada: ")

    if opcao == "1":
        nome = input("Digite o nome: ")
        nomes.append(nome)
        print("Cadastrado com sucesso!")

    elif opcao == "2":
        print(nomes)
        i = int(input("Digite o índice para atualizar: "))
        nomes[i] = input("Novo nome: ")
        print("Atualizado!")

    elif opcao == "3":
        print(nomes)
        i = int(input("Digite o índice para excluir: "))
        nomes.pop(i)
        print("Excluído!")

    elif opcao == "4":
        print("Lista:", nomes)

    elif opcao == "0":
        break

    else:
        print("Opção inválida!")


# Questão 67:

tabuleiro = [" " for _ in range(9)]

def mostrar():
    print(f"{tabuleiro[0]} | {tabuleiro[1]} | {tabuleiro[2]}")
    print("--+---+--")
    print(f"{tabuleiro[3]} | {tabuleiro[4]} | {tabuleiro[5]}")
    print("--+---+--")
    print(f"{tabuleiro[6]} | {tabuleiro[7]} | {tabuleiro[8]}")

jogador = "X"

for _ in range(9):
    mostrar()
    pos = int(input(f"Jogador {jogador}, escolha (0-8): "))

    if tabuleiro[pos] == " ":
        tabuleiro[pos] = jogador
        jogador = "O" if jogador == "X" else "X"
    else:
        print("Posição ocupada!")


# Questão 68:


import random

alunos = []

def gerar_matricula():
    return random.randint(1, 9999)

def cadastrar():
    nome = input("Nome: ")
    email = input("Email: ")
    nasc = input("Data de nascimento: ")
    
    aluno = {
        "matricula": gerar_matricula(),
        "nome": nome,
        "email": email,
        "nascimento": nasc
    }
    
    alunos.append(aluno)
    print("Aluno cadastrado!")

def listar():
    for a in alunos:
        print(a)

while True:
    print("\n1-Cadastrar 2-Listar 0-Sair")
    op = input("Opção: ")

    if op == "1":
        cadastrar()
    elif op == "2":
        listar()
    elif op == "0":
        break

# Questão 69:


def mostrar(tab):
    print(f"{tab[0]} | {tab[1]} | {tab[2]}")
    print("--+---+--")
    print(f"{tab[3]} | {tab[4]} | {tab[5]}")
    print("--+---+--")
    print(f"{tab[6]} | {tab[7]} | {tab[8]}")

def verificar(tab):
    combinacoes = [
        (0,1,2),(3,4,5),(6,7,8),
        (0,3,6),(1,4,7),(2,5,8),
        (0,4,8),(2,4,6)
    ]
    
    for a,b,c in combinacoes:
        if tab[a] == tab[b] == tab[c] != " ":
            return tab[a]
    
    return None

while True:
    tab = [" "] * 9
    jogador = "X"

    for rodada in range(9):
        mostrar(tab)
        pos = int(input(f"Jogador {jogador}, escolha (0-8): "))

        if tab[pos] != " ":
            print("Posição ocupada!")
            continue

        tab[pos] = jogador

        vencedor = verificar(tab)
        if vencedor:
            mostrar(tab)
            print(f"Jogador {vencedor} venceu!")
            break

        jogador = "O" if jogador == "X" else "X"
    else:
        mostrar(tab)
        print("Empate!")

    if input("Jogar novamente? (s/n): ") != "s":
        break