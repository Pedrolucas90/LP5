# WHILE 

# cont = 0

# while True:
#     cont = cont + 1
#     print(cont)
#     if cont >= 100:
#         break

# sair = 'não'
# while sair != 'sim':

print('0 - cadastrar')
print('1 - editar')
print('2 - excluir')

opcao = int(input('O que deseja  realizar '))

match opcao:
    case 0:
        print("Você escolheu cadastrar")
        sair = input('Deseja sair, sim ou não? ')
    case 1:
        print("Você escolheu editar")
        sair = input('Deseja sair, sim ou não? ')
    case 2:
        print("Você escolheu excluir")
        sair = input('Deseja sair, sim ou não? ')
    case _:
        print("opção invalida!")
        sair = input('Deseja sair, sim ou não? ')

# FOR para REPERIÇÕES pre definidas de vezes. 

# for numero in range(1,11):
#     print(numero) 


# percorrendo listas 

# frutas = ["Uva","Maçã", "Gabriel", "kiwi"]

# for fruta in frutas: 
#     print(fruta)

# nome = "Pedro"

# for letra in nome: 
#     print(letra)