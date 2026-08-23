import math
from math import sqrt
import random
import datetime

import moduloPersonalizado

from meu_pacote import modulo1 , modulo2

modulo1.funcao1()
modulo2.funcao2()




resultado = math.sqrt(25)
print(resultado)


resultado = sqrt (25)
print (resultado)

numero_aleatorio = random.randint(1,11)
print(numero_aleatorio)

data_atual = datetime.datetime.now()
print(data_atual)

moduloPersonalizado.saudar("Felipe")
resultado = moduloPersonalizado.calcular_soma(5,3)
print (resultado)