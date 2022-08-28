#João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. 
#Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 
#por quilo excedente. 
#João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso. 
#Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar. 
#Imprima os dados do programa com as mensagens adequadas.

peso_peixe = float(input("Insira o peso dos peixes: "))
excesso = peso_peixe - 50
multa = 4*excesso

if peso_peixe > 50.99:
	print("João deverá pagar uma multa de R$", multa, " porque o peso excedeu ", excesso, "Kg")

if peso_peixe <= 50.99:
	print("João não precisa pagar nenhuma multa, pois o peso medido foi ", peso_peixe, "Kg")
