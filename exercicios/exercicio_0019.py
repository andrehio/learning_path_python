# Exercício 19
# Um professor que sortear um dos seus quatro alunos para apagar o quadro.
# Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do
# escolhido.

from random import choice

a1 = input("Digite o primeiro aluno: ")
a2 = input("Digite o segundo aluno: ")
a3 = input("Digite o terceiro aluno: ")
a4 = input("Digite o quarto aluno: ")
aluno_escolhido = choice([a1, a2, a3, a4])
print("O aluno escolhido foi ", aluno_escolhido)
