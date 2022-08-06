# Exercício 20
# O mesmo professor do sesafio anterior quer sortear a ordem de
# apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos
# quatro alunos e mostre a ordem sorteada.

from random import shuffle

a1 = input("Digite o primeiro aluno: ")
a2 = input("Digite o segundo aluno: ")
a3 = input("Digite o terceiro aluno: ")
a4 = input("Digite o quarto aluno: ")
lista = [a1, a2, a3, a4]
shuffle(lista)
print("A ordem de apresentação será ", lista)
