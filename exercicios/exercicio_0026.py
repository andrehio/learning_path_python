# Exercício 26
"""
Crie um programa que leia uma frase pelo telado e mostre:
- quantas vezes aparece a letra "A"
- Em que posição ela aparece a primeira vez
- Em que posição ela aparece pela última vez.
"""

nome = input("Qual uma frase: ").strip()
nome_lower = nome.lower()
print("A letra A aparece {} vezes na frase".format(nome_lower.count("a")))
print("A primeira letra A apareceu na posição ", nome_lower.find("a") + 1)
print("A ultima letra A apareceu na posição ", nome_lower.rfind("a") + 1)
