# Exercício 25
"""
Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no
nome.
"""

nome = input("Qual é o seu nome completo: ").strip()
nome_lower = nome.lower()
# forma 1
if nome_lower.find("silva") != -1:
    print("Encontrado!")
else:
    print("Não encontrado!")

# forma 2
if "silva" in nome:
    print("Encontrado!")
else:
    print("Não encontrado!")
