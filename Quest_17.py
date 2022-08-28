#Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
#Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados 
#e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
#Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
#comprar apenas latas de 18 litros;
#comprar apenas galões de 3,6 litros;
#misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.

a = float(input("Digite o tamanho, em metros quadrados, da área a ser pintada: "))
lit = a/6
lata = int(lit/18)
gal = int(lit/3.6)
latagal = int(lit/23.76)

if lit%18 != 0:
	lata = lata+1
	preco_tot_lata = lata*80
  
if lit%3.6 != 0:
	gal = gal+1
	preco_tot_gal = gal*25
  
if lit%23.76 != 0:     #Mistura = 18 + 3.6 + 10% de folga = 21.6 + 21.6*10% = 23.76 Litros 
	latagal = latagal+1
	preco_tot_latagal = latagal*105

print("\tConsiderando apenas uma compra de latas de tinta, a quantidade de latas a serem compradas equivale a ", lata, f" e o preço total é R${preco_tot_lata:.2f}")
print("\tConsiderando apenas uma compra de galões de tinta, a quantidade de galões a serem compradas equivale a ", gal, f" e o preço total é R${preco_tot_gal:.2f}")
print("\tConsiderando uma mistura entre latas e galões, a quantidade dessa mistura a ser comprada equivale a ", latagal, f" e o preço total é R${preco_tot_latagal:.2f}")
