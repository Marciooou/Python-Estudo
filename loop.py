frutas = ["Maçã", "Banana" , "Maracujá"]

for frutas in frutas:
    print(frutas)
    
contador = 0

# while é ideal para quando não tiver um numero certo de interaçoes
while contador<= 5:
    print (contador) 
    contador +=1
    
print ("===============")  

for numero in range(1, 6):
    print (numero *2)
    
print ("===============")  

contadorDois = 0  
while contadorDois <= 5:
    print (contadorDois *2)
    contadorDois += 1 

print ("===============")     
    
contadorTres = 0

while True:
    print(contadorTres)
    contadorTres += 1
    
    if contadorTres == 5:
        break

print ("===============")     

for i in range(10):
    if i % 2 == 0:
        continue
    print (i)
    
print ("===============")   

for i in range(5):
    pass