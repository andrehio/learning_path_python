# Exercício 9
# Faça um programa que leia um número inteiro qualquer e mostre na tela a
# sua tabuada.

entrada = input("Digite um número para ver sua tabuada: ")
if entrada.isnumeric():
    num = int(entrada)
    print("-" * 10)
    for i in range(10):
        print("{}  x {:2} = {}".format(num, i + 1, num * (i + 1)))
    print("-" * 10)
else:
    print("Digite um número!")
