#Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
#Para homens: (72.7*h) - 58
#Para mulheres: (62.1*h) - 44.7

p = input("Digite M se você é mulher ou H se você é homem: ")

h = float(input("Digite sua altura em metros: "))

h_hom = (72.7*h) - 58
h_mul = (62.1*h) - 44.7

if p == "M":
	print("Com base na sua altura que equivale a ", h, "m, o seu peso ideal deve ser: ", h_mul, "Kg")

if p == "H":
	print("Com base na sua altura que equivale a ", h, "m, o seu peso ideal deve ser: ", h_hom, "Kg")
