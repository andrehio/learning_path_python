from random import randint


class Dado:

    def __init__(self, faces=6):
        self.__faces = faces if faces > 2 else -1

    def valor_jogada(self):
        return self.__calcular_jogada()

    def __calcular_jogada(self):
        if self.__faces == -1:
            return "Inválido"
        else:
            return randint(1, self.__faces)