from math import sqrt


class Quadrado:

    def __init__(self, lado):
        self.__lado = lado if lado >= 0 else 0

    def calc_perimetro(self):
        return self.__lado * 4

    def calc_area(self):
        return self.__lado ** 2

    def calc_diagonal(self):
        return self.__lado * sqrt(2)  # calcula raiz quadrada

    def imprimir(self):
        print("Quadrado de lado", self.__lado)