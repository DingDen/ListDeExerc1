#Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps)
#calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).

tam = float(input("Digite o tamanho do arquivo, em MB:\n"))
velink = float(input("Digite a velocidade do link de internet, em Mbps:\n"))

temp_download = (tam/velink)/60

print("\tO tempo, em minutos, aproximado do download desse arquivo usando esse link equivale a: ", temp_download, "minutos")
