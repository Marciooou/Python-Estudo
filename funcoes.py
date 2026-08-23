#FUNÇÕES

def saudacao():
    print ("Olá, mundo!")

saudacao()

#Parâmetros e argumentos
print("========")
def saudacao_p(nome):
    print(f"Olá, {nome}!")

saudacao_p("João")
saudacao_p("Maria")

#Valores de retorno

def soma(a, b):
    return a + b

resultado = soma(3, 4)
print (resultado)

#funções anônimas (lambda) - geralemnte usada quando se precisa apenas uma vez

quadrado = lambda x: x ** 2
print(quadrado(5))

numeros = [1,2,3,4]
dobrar = list (map(lambda x: x ** 2, numeros))
print (dobrar)

#variaveis local ou global

def funcao():
    variavel_local = 10
    print (variavel_local)

variavel_global = 20

def funcao2():
    print(variavel_global)

funcao()
funcao2()
print(variavel_global)


def calcular_media(*numeros):
    soma = sum(numeros)
    quantidade = len(numeros)
    media = soma / quantidade
    return media

print ("Media: ", calcular_media(10,7,8,10))

def somar_3(x):
    return x + 3

somar = lambda x: x + 3

print (somar_3(7))


def area_retangulo(base, altura):
    """
    Calcula a área de um retângulo.
    Args:
        base (float): a base do retangulo
        altura (float): a altura do retangulo
    Returns:
        float: area do retangulo
    """
    return base * altura
print(area_retangulo(4,3))

def somar_numeros(*numeross):
    total = 0
    for numero in numeross: #para cada numero em numeros
        total += numero
    return total 

print(somar_numeros(1,2,3))
print(somar_numeros(12,3))

numero = 7

for i in range(1, 11):
    resultado = numero * i
    print(resultado)