numero = input('Digite um número inteiro: ')

if numero.isdigit():
    numero_int = int(numero)
    par_impar = numero_int % 2 == 0
    if par_impar:
        print (f'1O número {numero_int} é par')
    else:
        print (f'O número {numero_int} é impar')
else: 
    print('Você não digitou um número')