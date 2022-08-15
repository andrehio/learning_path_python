# Exercício 23
"""
Crie um programa que leia um número de 0 a 9999 e mostre na tela cada um dos
digitos separados.
"""

num_int = int(input("Digite um número: "))
if 0 <= num_int <= 9999:
    num = str(num_int)
    try:
        if num[0] != "0":
            print("Unidade:", num[0])
        if num[1] != "0":
            print("Dezena:", num[1])
        if num[2] != "0":
            print("Dezena:", num[2])
        if num[3] != "0":
            print("Milhar:", num[3])
    except:
        pass
