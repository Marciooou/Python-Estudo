primeiro_valor = int(input('Digite um valor: '))
segundo_valor = int(input('Digite outro valor: '))

if primeiro_valor > segundo_valor:
    print(f'{primeiro_valor=}  é maior que o {segundo_valor=}')
else: 
    print(f'{segundo_valor=}  é maior que o {primeiro_valor=}')


entrada = input('Digite [E] para entrar ou [S] para sair: ')
senha_digitada = input('Digite sua senha: ')
senha_permitida = '12345'

if (entrada == 'E' or entrada == 'e') and senha_digitada == senha_permitida:
    print('Entrou no sistema')
elif entrada == 'S':
    print('Saiu do sistema')
else: 
    print('Erro: Login ou senha errado')

print(True and True and True and False and True)
print(bool(1))


print (not True)
print (not False)