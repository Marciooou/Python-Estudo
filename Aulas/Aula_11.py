frase = 'O Python é uma linguagem de programação '\
    'multiparadigma. ' \
    'Python foi criado por Guido van Rossum. '
    
# print(frase.count(''))

i = 0
apareceu_mais_vezes = 0
letra_que_apareceu_mais = ''

while i < len(frase):
    letra_atual = frase[i] 
    if letra_atual == ' ':
        i += 1
        continue
    quantas_vezes = frase.count(letra_atual)
    
    if apareceu_mais_vezes < quantas_vezes:
        apareceu_mais_vezes = quantas_vezes
        letra_que_apareceu_mais = letra_atual
    
    i += 1
    
print (letra_que_apareceu_mais)