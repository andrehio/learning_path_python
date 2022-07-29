# Exercício 5
# Faça um programa que leia um número inteiro e mostre na tela o seu
# sucessor e o seu antecessor.

entrada = input("Digite um número: ")
if entrada.isnumeric():
    num = int(entrada)
    print("Analisando o valor {}, seu antecessor é {} e o sucessor é {"
          "}".format(num, num - 1, num + 1))
else:
    print("Digite um número!")
