# Atividade Prática - Firebase
# Disciplina: Segurança da Tecnologia da Informação
# Projeto 2 - Autenticação com Gmail

import p04_email, p04_cadastro_pyrebase

def menu():
    print("\n*** Pagina de acesso e autenticação ***")
    print("1. cadastrar usuario")
    print("2. autenticar")
    op = int(input("Escolha uma das opções: "))
    if 1 <= op <= 2:
        return op
    else:
        print("Opção inválida.")


def cadastro():
    print("\n*** Pagina de cadastro ***")
    print("1. autenticar email")
    print("2. cadastrar email e senha")
    print("3. voltar")
    op = int(input("Escolha uma das opções: "))
    if 1 <= op <= 3:
        return op
    else:
        print("Opção inválida.")


def select_menu():
    while True:
        op = menu()
        if 1 <= op <= 2:
            if op == 1:  # cadastrar usuario
                select_cadastro()
            elif op == 2:
                pass


def select_cadastro():
    op = cadastro()
    if 1 <= op <= 3:
        if op == 1:  # autenticar email
            p04_email.auth_email()
        elif op == 2:  # cadastrar email e senha
            p04_cadastro_pyrebase.cadastro()
        elif op == 3:  # voltar
            pass


# Inicio do programa

