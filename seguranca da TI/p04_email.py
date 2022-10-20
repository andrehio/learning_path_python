import p04_autenticacao_multifator

import smtplib
import string
import random
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import pyrebase
from datetime import date

firebaseConfig = {
    "apiKey": "AIzaSyDNso_cj_DgJRUI9W_cB05n3xbovpPQ9WU",
    "authDomain": "fir-puc-sti.firebaseapp.com",
    "projectId": "fir-puc-sti",
    "databaseURL": "https://fir-puc-sti-default-rtdb.firebaseio.com",
    "storageBucket": "fir-puc-sti.appspot.com",
    "messagingSenderId": "263870010434",
    "appId": "1:263870010434:web:e415896c56986be808c9db",
    "measurementId": ""
}
global firebase, db
firebase = pyrebase.initialize_app(firebaseConfig)
db = firebase.database()


def auth_email():
    # insert
    input_email = str(input("Digite o email a ser autenticado: "))
    input_codigo = str(input("Digite o código de autenticação: "))
    data = {"email": input_email, "cod_auth": input_codigo,
            "date_auth": str(date.today()), "autenticado": False}
    db.child("users").push(data)

    envio_auth(input_email, input_codigo)


def envio_auth(input_email, input_codigo):
    try:
        server = "smtp.gmail.com"
        port = 587
        username = input_email
        password = input_codigo

        mail_from = input_email
        mail_to = input_email
        mail_subject = "Projeto 1 - Segurança da Tecnologia da Informação"
        cod_aleatorio = gerador_aleatorio()
        mail_body = "O código de verificação é: " + cod_aleatorio

        mensagem = MIMEMultipart()
        mensagem['From'] = mail_from
        mensagem['To'] = mail_to
        mensagem['Subject'] = mail_subject
        mensagem.attach(MIMEText(mail_body, 'plain'))

        connection = smtplib.SMTP(server, port)
        connection.starttls()
        connection.login(username, password)
        connection.send_message(mensagem)
        connection.quit()

        print("Por favor, verifique o código de verificação enviado no seu "
              "email.")
        while True:
            teste = str(input("\nDigite o código: "))
            if cod_aleatorio == teste:
                update_true(input_email, input_codigo)
                print("A autenticação foi realizada com sucesso.")
                break
            else:
                print("O código não é o mesmo!")
    except:
        print("A autenticação falhou.")


def update_true(input_email, input_codigo):
    db = firebase.database()
    users = db.child("users").get()
    for user in users.each():
        if (user.val()["email"] == input_email and user.val()["cod_auth"] ==
                input_codigo):
            db.child("users").child(user.key()).update(
                {"autenticado": True})


def encontrar_autenticado(input_email):
    db = firebase.database()
    users = db.child("users").get()
    for user in users.each():
        if (user.val()["email"] == input_email and
                bool(user.val()["autenticado"]) is True):
            return True


def gerador_aleatorio(tamanho=10):
    chars = string.ascii_uppercase + string.digits
    return "".join(random.choice(chars) for _ in range(tamanho))


if __name__ == '__main__':
    p04_autenticacao_multifator.select_menu()
