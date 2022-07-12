# Métodos
'''
Métodos para identificação de dados
'''


def imprimir(letras):
    print("São númericos?")
    for i in letras.keys():
        print("{0} é {1}".format(i, letras.get(i).isnumeric()))

    print("\nSão alfas?")
    for i in letras.keys():
        print("{0} é {1}".format(i, letras.get(i).isalpha()))

    print("\nSão alfanumericos?")
    for i in letras.keys():
        print("{0} é {1}".format(i, letras.get(i).isalnum()))

    print("\nSão maiúsculos?")
    for i in letras.keys():
        print("{0} é {1}".format(i, letras.get(i).isupper()))

    print("\nSão minúsculos?")
    for i in letras.keys():
        print("{0} é {1}".format(i, letras.get(i).islower()))


op = {
    "a": "\u0030", # unicode for 0
    "b": "\u00B2", # unicode for &sup2;
    "c": "10km2",
    "d": "-1",
    "e": "1.5",
    "f": "abc",
    "g": "ABC",
    "h": "AbC"
}

imprimir(op)
