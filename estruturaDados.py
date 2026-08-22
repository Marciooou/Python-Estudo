frutas = ["Banana", "Maçã", "Abacaxi"]

frutas.append ("Laranja")
print (frutas)
frutas.insert (1, "Uva")
print (frutas)
frutas.remove ("Banana")
print (frutas)
frutaRemovida = frutas.pop (2)
print(frutas)
print(frutaRemovida)
print ("========")
frutas.sort()
print(frutas)
frutas.reverse()
print(frutas)
print ("========")

# Lista de compreensão
numeros = [1,2,3,4,5]
quadrados = [x ** 2 for x in numeros if x % 2 == 0 ]
print (quadrados)

#TUPLAS
print ("========")
ponto = (1,2,3,2,4,2)

print(ponto.index(4))
print(ponto.count(2))

print ("========")

#DICIONARIOS
pessoa = {
    "nome":"João", 
    "idade":25, 
    "cidade":"Madri"
}
print(pessoa["nome"])
print(pessoa["idade"])
print(pessoa["cidade"])

print ("========")

#keys(): retorna uma visualização de todas as chaves do dicionario
#values(): retorna uma visualização de todos os valores do dicionario
#items(): retonrna uma visualização de todos os pares chave-valor do dicionario
#update(outro_dicionario): atualiza o dicionario com os pares chave-valor de outro dicionario

print(pessoa.keys())
print(pessoa.values())
print(pessoa.items())

pessoa.update({"profissão":"engenheiro"})
print(pessoa)