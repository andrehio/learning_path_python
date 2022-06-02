# Função
# Curso: Raciocínio Lógico
# Pontifícia Universidade Católica do Paraná (PUC-PR)
'''
Elabore um programa que cadastre contatos de uma agenda telefônica. A função de cadastro
deve ser realizada dentro de uma função chamada inserir, que recebe como parâmetros o
nome e o telefone do contato, bem como a agenda de contatos. A função deve verificar se o
contato já existe e, em caso positivo, perguntar se o telefone deve ser modificado, retornando
true ou false, de acordo com a inclusão/modificação executada ou não na agenda.
'''

agenda_telefonica = {}


def inserir(nome, telefone, agenda):
    if nome in agenda:
        if input("Contato já cadastrado. Deseja alterar o telefone? (s/n) ") == "n":
            return False
    agenda[nome] = telefone
    return True


while True:
    nome = input("Digite o nome do contato: ")
    telefone = input("Digite o telefone do contato: ")
    if inserir(nome, telefone, agenda_telefonica):
        print("Contato adicionado ou atualizado com sucesso!")
    else:
        print("Falha ao tentar adicionar o contato!")
    if input("Gostaria de adicionar um novo contato? (s/n) ") == "n":
        break

print(agenda_telefonica)
