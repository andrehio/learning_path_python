# Exercício 24
"""
Crie um programa que leia o nome de uma cidade e diga se ela começa ou nao
com o nome "SANTO".
"""

cid = input("Digite um número: ").strip()
cid_lower = cid.lower()
if cid_lower[:5] == "santo":
    print("Encontrado!")
else:
    print("Não encontrado!")
