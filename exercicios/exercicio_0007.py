# Exercício 7
# Desenvolva um programa que leia as duas notas de um aluno. calcule e
# mostre a sua média.

entrada1 = input("Digite a primeira nota do aluno: ")
entrada2 = input("Digite a segunda nota do aluno: ")
if entrada1.isnumeric() and entrada2.isnumeric():
    med = (float(entrada1) + float(entrada2)) / 2
    print("A média entre {} e {} é igual a {:.1f}".format(entrada1,
                                                          entrada2, med))
else:
    print("Digite um número!")
