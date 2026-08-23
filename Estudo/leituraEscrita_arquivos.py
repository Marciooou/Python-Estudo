#Leitura
#primeiro abre com o open( "dados.txt", "r" -> modo leitura)
arquivo = open("dados.txt", "r")
conteudo = arquivo.read() # -> ler
print (conteudo)
arquivo.close()

#Escrita
arquivo = open("dados.txt", "w")
arquivo.write("Olá, mundo!")
arquivo.close()

with open ("dados.txt", "r") as arquivo:
    conteudo = arquivo.read()
    print(conteudo)