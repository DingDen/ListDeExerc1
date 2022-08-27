#Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
# o produto do dobro do primeiro com metade do segundo.
# a soma do triplo do primeiro com o terceiro.
# o terceiro elevado ao cubo.

n1 = int(input("Insira um número inteiro:\n"))
n2 = int(input("Insira outro número inteiro:\n"))
f1 = float(input("Insira um número real:\n"))

p1 = (2*n1)*(n2/2)
p2 = (3*n1)+f1
p3 = f1**3

print("\tPrimeira proposição: ", p1)
print("\tSegunda proposição: ", p2)
print("\tTerceira proposição: ", p3)
