palavra_secreta = 'computador'
letras_acertadas = ''
tentativa = 0
while True:
    letra_digitada = input('Tente adivinhar a palavra. Digite uma letra: ')
    tentativa += 1
    if len(letra_digitada) > 1:
        print('Digite apenas uma letra.')
        continue
    
    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada
    
    palavra_formada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'
    print('Palavra foramada: ', palavra_formada)
    if palavra_formada == palavra_secreta:
        print('Você ganhou! Parabéns')
        print('Tentativas: ', tentativa)
        letras_acertadas = ''
        tentativa = 0
        break