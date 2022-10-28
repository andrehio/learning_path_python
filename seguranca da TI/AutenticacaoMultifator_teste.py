'''
Pontifícia Universidade Católica do Paraná
Escola Politécnica
Disciplina: Algorithmic Reasoning
Author: Jhonatan Geremias - 02/07/2021
Autenticação Multifator - Desafio Banco de Tóquio
'''
import pyrebase
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import random

firebaseConfig = {
    "apiKey": "AIzaSyDNso_cj_DgJRUI9W_cB05n3xbovpPQ9WU",
    "authDomain": "fir-puc-sti.firebaseapp.com",
    "projectId": "fir-puc-sti",
    "databaseURL": "https://fir-puc-sti.firebaseio.com",
    "storageBucket": "fir-puc-sti.appspot.com",
    "messagingSenderId": "263870010434",
    "appId": "1:263870010434:web:e415896c56986be808c9db",
    "measurementId": ""
}

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()

input_email = str(input("Digite o email a ser autenticado: "))
input_codigo = str(input("Digite o código de autenticação: "))

server = "smtp.gmail.com"
port = 587
username = "prof.jgeremias@gmail.com"
passwordSMTP = "gcpdxhvyfqtnyfnb"

ok = True

while ok:
    print("1 - Cadastrar Usuário")
    print("2 - Verificar Email")
    print("3 - Autenticar Usuário")

    opcao = input("Selecione uma das opções:")

    if opcao == "1":
        user = input("Digite seu e-mail: ")
        password = input("Digite sua senha, com pelo menos 6 caracteres: ")
        status = auth.create_user_with_email_and_password(user, password)
        print("Email cadastrado: ",user)

    if opcao == "2":
        user = input("Digite seu e-mail: ")
        password = input("Digite sua senha, com pelo menos 6 caracteres: ")
        status = auth.sign_in_with_email_and_password(user, password)
        idToken = status["idToken"]
        auth.send_email_verification(idToken)
        print("Email de verificação enviado: ", user)

    if opcao == "3":
        user = input("Digite seu e-mail: ")
        password = input("Digite sua senha, com pelo menos 6 caracteres: ")
        status = auth.sign_in_with_email_and_password(user, password)
        idToken = status["idToken"]
        info = auth.get_account_info(idToken)
        users = info["users"]
        verifyEmail = users[0]["emailVerified"]

        if verifyEmail:
            print("Segundo Fator de Autenticao")
            codigo = random.randint(100,1000)
            mail_body = "Código de validação: %d "%codigo

            mensagem = MIMEMultipart()
            mensagem['From'] = username
            mensagem['To'] = user
            mensagem['Subject'] = "Código E-mail"
            mensagem.attach(MIMEText(mail_body, 'plain'))

            connection = smtplib.SMTP(server, port)
            connection.starttls()
            connection.login(username, passwordSMTP)
            connection.send_message(mensagem)
            connection.quit()

            codigoEmail = int(input("Entre com o código que foi enviado por e-mail: "))

            if codigo == codigoEmail:
                print("Usuário Autenticado!!!")
            else:
                print("Código Inválido!!")

        else:
            print("Email não verificado!")
