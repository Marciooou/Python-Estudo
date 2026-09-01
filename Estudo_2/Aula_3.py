#Conversão de tipos

#Tupos imutáveis e primitivos:
#str, int. float, booleano
print(int('1') + 1)
print(bool(" oi "))
print(str(12) + 'b')

#Variáveis

nome = 'Márcio'
sobrenome = 'Ramos'
idade = 20
ano_nascimento = 2026 - idade
maior_de_idade = idade >= 18
alutra_em_metros = 1.80

print ('Nome:', nome)
print ('Sobrenome:', sobrenome)
print ('Idade:', idade)
print ('Ano de nascimento:', ano_nascimento)
print ('É maior de idade?', maior_de_idade)
print ('Altura:', alutra_em_metros)

#Precendência entre operadores

peso = 92
imc = peso / (alutra_em_metros ** 2 )
print(imc)
print(f'{nome} tem {alutra_em_metros:.2f} de altura e pesa {peso} seu imc é {imc:.2f}')

#Formatação com .format
print ('===================')
a = 'A'
b = 'B'
c = 'C'
formato =  'a={letraa}'.format(letraa =a, letra2 =b, letra = c)

print(formato)

#Imput 
#name = input('Qual seu nome? ')
numero_1 = input('Digite um número: ')
numero_2 = input('Digite outro número')
soma = int(numero_1) + int(numero_2)

print(f'A soma dos números é {soma}')

#condição 
