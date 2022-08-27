#Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius. C = 5 * ((F-32) / 9).
fah = float(input("Digite o valor da temperatura em graus Fahrenheit: "))
cel = 5*((fah-32)/9)

print("A conversão de ", fah, " graus Fahrenheit equivale a ", cel, " graus Celsius")
