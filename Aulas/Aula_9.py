# v1 = 'a'
# v2 = 'b'

# print(id(v1))
# print(id(v2))

"""
FLAG : normalmente guarda true ou false
"""

usuario_logado = True

if usuario_logado:
    print('Pode acessar o sisteam')
else:
    print('Login necessario')

"""
NONE: não tem valor no momento

"""
print('=====================')
"""
IS: verifica se duas referencias apontam para o mesmo objeto
"""
lista1 = [1,2,3]
lista2 = [1,2,3]

print(lista1 == lista2)

#porem no is
print('Porem no is: ')
print (lista1 is lista2)
print('Pois não esta na mesma memoria')

"""
IS NOT: contratio do is
"""
