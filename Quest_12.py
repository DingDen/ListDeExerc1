#Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58
alt = float(input("Digite sua altura em metros: "))
peso_ideal = (72.7*alt) - 58

print("Com base na sua altura que equivale a ", alt, "m, o seu peso ideal deve ser: ", peso_ideal, "Kg")
