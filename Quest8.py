#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.
dinhora = float(input("Digite o valor que você ganha por hora:\n"))
numes = int(input("Digite o número de horas que você trabalha no mês:\n"))

salario_total = dinhora*numes

print("\tO total do seu salário nesse mês equivale a R$", salario_total)
