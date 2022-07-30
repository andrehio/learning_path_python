# Exercício 10
# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e
# mostre quantos dólares ela apode comprar.

entrada = input("Quanto dinheiro você tem na carteira? R$")
cotacao = input("Qual a cotação do dolar? ")
carteira = float(entrada)
print("Com R${} você pode comprar US${}".format(carteira, carteira * float(
                                                cotacao)))
