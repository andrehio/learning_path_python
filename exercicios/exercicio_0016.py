# Exercício 16
# Crie um programa que leia um número real qualquer pelo teclado e mostre na
# tela a sua porção inteira

from math import trunc

num = float(input("Digete um número: "))
print("O número {} tem a parte inteira {}"
      " -- usando modulo math".format(num, trunc(num)))
print("O número {} tem a parte inteira {}"
      " -- usando int".format(num, int(num)))
