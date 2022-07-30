# Exercício 8
# Escreva um programa que leia um valor em metros e o exiba convertido em
# km, hm, dam, dm, cm, mm.

entrada = input("Digite um valor em metros: ")
if entrada.isnumeric():
    num = float(entrada)
    print("A medida de {}m corresponde a...".format(num))
    print("{}km".format(num * 0.001))
    print("{}hm".format(num * 0.01))
    print("{}dam".format(num * 0.1))
    print("{}dm".format(num * 10))
    print("{}cm".format(num * 100))
    print("{}cm".format(num * 1000))
else:
    print("Digite um número!")
