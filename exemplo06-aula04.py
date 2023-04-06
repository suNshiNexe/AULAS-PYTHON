n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
#processamento
m = (n1+n2)/2
if m >= 6:
    print("Aprovado - Média", m)
else:
    print("Reprovado - Média", m)
