# Exercício 6
# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz
# quadrada.

entrada = input("Digite um número: ")
if entrada.isnumeric():
    num = int(entrada)
    print("O dobro de {0} vale {1}. \nO triplo de {0} vale {2}. \nA raiz "
          "quadrada de {0} é igual a {3:.2f}".format(num, num * 2, num * 3,
                                                     num ** (1 / 2)))
else:
    print("Digite um número!")
