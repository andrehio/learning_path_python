# Exercício 12
# Crie um programa que leia o preço de um produto e mostre seu novo preço
# com um dado desconto.

p = float(input("Qual o preço do produto? R$"))
d = float(input("Qua o desconto do produto (%): "))
pfinal = p * (1 - d/100)
print("O produto que custava R${:.2f}, na promoção com desconto de {}% vai "
      "custar R${:.2f}".format(p, d, pfinal))

