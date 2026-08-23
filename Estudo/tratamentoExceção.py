#Try
try:
    resultado = 10 / 5
    print(resultado)
except ZeroDivisionError:
    print("Erro: Divisão por zero")
except ValueError:
    print("Erro: Valor inválido")

#Finally - sempre executado, independente de uma exceção ou não. Usado para limpar ou liberar recursos

try:
    arquivo = open("arquivo.txt", "r")
except FileNotFoundError:
    print("Erro: Arquivo não encontrado")
# finally:
#     arquivo.close

#Personalizada

def permissao(idade):
    if idade<18:
        raise Exception("menor de idade")

try:
    permissao(15)
except Exception as e: 
    print(f"Erro: {str(e)}")

