# Função (Exercício de fixação 3)
# Curso: Raciocínio Lógico
# Pontifícia Universidade Católica do Paraná (PUC-PR)
'''
Exercício de fixação 3: Crie um programa que receba uma lista de números e retorne a média.
Documente a função media()
'''


def media(*numeros):
    """
    Calcula a média dos números passados para a função

    :param numeros: lista de números
    :return: valor da média calculada
    """
    soma = 0
    for numero in numeros:
        soma += numero
    return soma / len(numeros)


resultado = media(2, 5, 9, 4, 11)
print(f"O valor da média é {resultado}")
