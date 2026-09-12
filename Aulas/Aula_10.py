#loop

# condicao = True
# while condicao:
#     nome = input('Qual o seu nome: ')
#     print(f'Seu nome é {nome}')
    
#     if nome == 'fui':
#         break
    

#contador = 0

# while contador <= 9:
#     contador = contador + 1
#     print(contador)

# # while contador <= 99:
# #     contador += 1
    
# #     if contador == 6:
# #         print('Não vou mostrar o 6')
# #         continue
    

    
# #     if contador >=10 and contador <=30:
# #         print ('Não vou mostrar o ', contador)
# #         continue
    
# #     print(contador)

qtd_linhas = 5
qtd_colunas = 5

linha = 1
while linha <= qtd_linhas:
    coluna = 1
    while coluna <= qtd_colunas:
        print (linha,coluna)
        coluna += 1
    linha += 1 

print ('fim')