#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, 
#sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
#salário bruto.
#quanto pagou ao INSS.
#quanto pagou ao sindicato.
#o salário líquido. Calcule os descontos e o salário líquido
#salário bruto - descontos = salário líquido

gan_hora = float(input("Digite quanto você ganha por hora:\n"))
hora_mes = int(input("Digite o número de horas trabalhadas no mês:\n"))

sal_bruto = gan_hora*hora_mes
ir = (11/100)*sal_bruto
inss = (8/100)*sal_bruto
sind = (5/100)*sal_bruto
descontos = ir + inss + sind
sal_liq = sal_bruto - descontos

print("\t\tSalário Bruto: R$", sal_bruto)
print("\t\tIR(11%): R$", ir)
print("\t\tINSS(8%): R$", inss)
print("\t\tSindicato(5%): R$", sind)
print("\t\tSalário Líquido: R$", sal_liq)
