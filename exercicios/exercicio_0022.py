# Exercício 22
"""
Crie um programa que leia o nome completo de uma pessoa e mostre:
- O nome com todas as letras maiúsculas e minísculas.
- Quantas letras ao todo (sem considerar espaços).
- Quantas letras tm o primeiro nome.
"""


nome = input("Digeite seu nome completo: ")
print("Analisando o seu nome...")
print("Seu nome em maiúsculas é", nome.upper())
print("Seu nome em minúsculas é", nome.lower())
print("Seu nome tem ao todo {} letras".format(len(nome) - nome.count(" ")))
firstName = nome.split()[0]
print("Seu primeiro nome é {} e ele tem {} letras".format(firstName, len(firstName)))
