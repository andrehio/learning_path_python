# Função
'''
Elabore um programa que cadastre contatos de uma agenda telefônica.
A função de cadastro deve ser realizada dentro de uma função chamada inserir,
que recebe como parâmetros o nome e o telefone do contato,
bem como a agenda de contatos.
'''

agenda_telefonica = {}


def inserir(nome, telefone, agenda):
    agenda[nome] = telefone


while True:
    nome = input("Digite o nome do contato: ")
    telefone = input("Digite o telefone do contato: ")
    inserir(nome, telefone, agenda_telefonica)
    if input("Gostaria de adicionar um novo contato? (s/n) ") == "n":
        break

print(agenda_telefonica)