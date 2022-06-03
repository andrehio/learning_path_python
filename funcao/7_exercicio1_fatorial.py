# Função (Exercício de fixação 1)
# Curso: Raciocínio Lógico
# Pontifícia Universidade Católica do Paraná (PUC-PR)
'''
Exercício de fixação 1: Crie um programa que calcule, a partir de uma função, o fatorial de um
número. Exemplo: Fatorial de 5 => 5! = 5.4.3.2.1. Observação: por propriedade, 0! = 1.
Documente a função fatorial()
'''


def fatorial(numero):
    """
    Calcula o fatorial de um número

    :param numero: número-base para o cálculo do fatorial
    :return: resultado do cálculo do fatorial
    """
    fat = 1
    for i in range(numero):
        fat *= i + 1
    return fat


resultado = fatorial(5)
print(f"O resultado é {resultado}")
