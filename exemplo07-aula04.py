import math
numero = int(input("Digite um número inteiro: "))

if numero > 0:
    raiz = math.sqrt(numero) #Essa variável só existe dentro do bloco if
    print("A raiz quadrada desse número é: ", raiz)
else:
    print("O número não é positivo, não existe raiz.")


