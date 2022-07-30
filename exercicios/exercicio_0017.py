# Exercício 17
# Crie um programa que leia o comprimenro do cateto opposto e do cateto
# adjacente de um triângulo retângulo, calcule e mostre o comprimento da
# hipotenusa.

from math import sqrt, pow, hypot

co = float(input("Comprimento do cateto oposto: "))
ca = float(input("Comprimento do cateto adjacente: "))
h1 = (ca ** 2 + co ** 2) ** (1/2)
h2 = sqrt(pow(ca, 2) + pow(co, 2))
h3 = hypot(ca, co)
print("A hipotenusa vai medir %.2f (formula simples)" % h1)
print("A hipotenusa vai medir %.2f (modulos sqrt e pow)" % h2)
print("A hipotenusa vai medir %.2f (modulo hypot)" % h3)
