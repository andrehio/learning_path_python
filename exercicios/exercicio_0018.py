# Exercício 18
# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do
# seno, cosseno e tandente desse ângulo.

import math

ang = float(input("Digite o ângulo que você deseja em graus: "))
rad = math.radians(ang)
print("O ângulo de {}º tem o SENO de {:.2f}".format(ang, math.sin(rad)))
print("O ângulo de {}º tem o COSSENO de {:.2f}".format(ang, math.cos(rad)))
print("O ângulo de {}º tem a TANGENTE de {:.2f}".format(ang, math.tan(rad)))
