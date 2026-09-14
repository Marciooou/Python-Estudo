#for --> sabe onde termina
#While --> quando não sei o numero de repetições 

texto = 'Documento'
nova_letra = ''
for letras in texto:
    nova_letra += f'*{letras}'
    print(letras)
print(nova_letra + '*')

numeros = range(0,10,2)

for numero in numeros:
    print(numero)
    
for i in range(10):
    if i == 2:
        print('i é 2, pulando...')
        continue
    if i == 8:
        print('i é 8, seu else não executará')
        break
    for j in range (1,3):
        print(i, j)
else:
    print('For completo com sucesso!')