#Try: -> tenta executar o codigo
#except: -> ocrreu erro tentando executar o codigo
numero_str = input('Digite um número que deseja dobrar: ')
try:
    print('STR:', numero_str)
    numero_float = float(numero_str)
    print('Float: ', numero_float)
    print(f'O dobro de {numero_str} é {numero_float * 2}')
except:
    print('Isso não é um número')