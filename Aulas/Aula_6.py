# nome = 'Otávio'

# print(nome[4])
# print(nome[-2])

# print('v' in nome)
# print('Otá' not in nome)

# name = input('Digite seu nome: ')
# encontrar = input('Digite oque deseja encontrar no seu nome: ')

# if encontrar in name:
#     print (f'{encontrar} está em {name}')
# else:
#     print (f'{encontrar} não está em {name}')

##=====================
##Interpolação
##=====================

# nome = 'Luiz'
# preco = 1000.548745
# variavel = '%s, o preço é R$%.2f' % (nome, preco)
# print(variavel)
# print('O hexadecimal de %d é %x' % (100,100))

##=====================
##formatação string
##=====================

# variavel = 'ABC'  
# print (f'{variavel}')
# print (f'{variavel:>10}')
# print (f'{variavel:B^10}.')

##=====================
##fatiamento de string
##=====================
#len conta caracteres
variavel = 'Olá mundo'
print(variavel[0:9:2])
