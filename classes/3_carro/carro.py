# Classe (Exemplo de aplicação 3)
# Curso: Raciocínio Lógico
# Pontifícia Universidade Católica do Paraná (PUC-PR)
'''
Exemplo de aplicação 3: Elaborar um programa para consultar o IPVA
Aplicar a boa prática de criar função de get e set
'''

from datetime import date


class Carro:

    def __init__(self, modelo, marca, ano, combustivel, quilometragem):
        self.__modelo = modelo
        self.__marca = marca
        self.__ano = ano
        self.__combustivel = combustivel
        self.__quilometragem = quilometragem

    def getModelo(self):
        return self.__modelo

    def setModelo(self, modelo):
        self.__modelo = modelo

    def getMarca(self):
        return self.__marca

    def setMarca(self, marca):
        self.__marca = marca

    def getAno(self):
        return self.__ano

    def setAno(self, ano):
        self.__ano = ano

    def getCombustivel(self):
        return self.__combustivel

    def setCombustivel(self, combustivel):
        self.__combustivel = combustivel

    def getQuilometragem(self):
        return self.__quilometragem

    def setQuilometragem(self, quilometragem):
        self.__quilometragem = quilometragem

    def consultarIsencaoIPVA(self):
        data_atual = date.today()
        ano_atual = int(data_atual.year)
        idadeVeiculo = ano_atual - self.__ano

        if idadeVeiculo > 20:
            print("Este veículo é isento de IPVA")
        else:
            if idadeVeiculo == 20:
                print("Seu veículo será isento no próximo ano")
            else:
                print("Seu veículo será isento em %d ano(s).", 20 - idadeVeiculo)
                print("Consulte o IPVA no Detran do seu estado")

# teste de carro 1
carro1 = Carro("Fusca", "Volkswagen", 1956, "Gasolina", 400000)
print(carro1.getModelo())
carro1.consultarIsencaoIPVA()

# teste de carro 2
print("")
carro2 = Carro("Polo", "Volkswagen", 2019, "Flex", 15000)
print(carro2.getModelo())
carro2.consultarIsencaoIPVA()
print("quilometragem " + str(carro2.getQuilometragem()))
carro2.setQuilometragem(20000)
print("quilometragem " + str(carro2.getQuilometragem()))
