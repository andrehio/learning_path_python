# Exercício 15
# Escreva um programa que pergunte a quantidade de km percorridos por um
# carro alugado e a quantidade de dias pelos quas ele foi alugado. Calcule o
# preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por km rodado.

d = int(input("Informe a quantidade de dias alugados: "))
k = float(input("Informe a o valor de km rodados: "))
print("O total a pagar é de R$", d * 60 + k * 0.15)
