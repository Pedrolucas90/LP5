# condicinal if 

# acompanhada = 'Sim'
# idade = 15

# if idade <= 0:
#     print("Idade invalida") 
# elif idade <= 17:
#     print("Você e menor de idade")
# else: 
#     print("Você e maior de idade!")


# if idade >=18:
#     print("Você pode assistir o filme")
# elif (idade >= 15 and idade <=17) and acompanhada == 'Sim':
#     print("Você pode assistir o filme")
# else: 
#     print("Você não pode assistir o filme")


print('opção desejada é 0 cadastrar')
print('opção desejada é 1 editar')
print('opção desejada é 2 excluir')

opcao=int(input('O que deseja  realizar '))

match opcao:
    case 0:
        print("Você escolheu cadastrar")
    case 1:
        print("Você escolheu editar")
    case 2:
        print("Você escolheu excluir")
    case _:
        print("opção invalida!")
