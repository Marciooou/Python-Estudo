horario = input('Digite o horario atual em numeros inteiros ')

try:
    hora = int(horario)

    if hora >=0 and hora <= 11:
        print('Bom dia')
    elif hora >= 12 and hora <=17:
        print('Boa tarde')
    elif hora >= 18 and hora <=23:
        print('Boa noite')
    else:
        print('Não existe essa hora')
except:
    print('Digite apenas números inteiros')