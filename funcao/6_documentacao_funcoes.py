# Função (Documentando funções)
# Curso: Raciocínio Lógico
# Pontifícia Universidade Católica do Paraná (PUC-PR)
'''
Padrão de documentação PEP 257 – Docstring Conventions
'''


def delta(a, b, c): # função conforme o padrão PEP 257
    """
    Calcula o valor de delta utilizado no cálculo de raízes de polinômios de segundo grau.

    :param a: Valor do primeiro termo do polinômio.
    :param b: Valor do segundo termo do polinômio.
    :param c: Valor do termo independente do polinômio.
    :return: Retorna as raízes calculadas e um booleano, indicando se o cálculo foi bem-sucedido.
    """
    return b * b - 4 * a * c


def bhaskara(a, b, c):
    d = delta(a, b, c)
    if d < 0:
        print("As raízes são imaginárias")
        return 0, 0, False
    else:
        x1 = (-b + d ** 0.5) / 2 * a
        x2 = (-b - d ** 0.5) / 2 * a
        return x1, x2, True


result1 = bhaskara(1, 3, 1)
if result1[2]:
    print(f"As raízes são {result1[0]} e {result1[1]}")

result2 = bhaskara(1, 2, 1)
if result2[2]:
    print(f"As raízes são {result2[0]} e {result2[1]}")

result3 = bhaskara(1, 1, 1)
if result3[2]:
    print(f"As raízes são {result3[0]} e {result3[1]}")
