# Exercício 13
# Crie um programa que leia o salário de um funcionário e mostre seu novo
# salário com 15% de aumento.

s = float(input("Qual é o salário do funcionário? R$"))
new_s = s * 1.15
print("Um funcionário que ganhava R${:.2f}, com 15% de aumento, passa a "
      "receber R${:.2f}".format(s, new_s))

