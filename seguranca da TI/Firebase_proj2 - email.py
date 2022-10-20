# Atividade Prática - Firebase
# Disciplina: Segurança da Tecnologia da Informação
# Projeto 2 - Autenticação com Gmail

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

server = "smtp.gmail.com"
port = 587
username = "ahdreki@gmail.com"
password = "fqrtfwyybilfdigw"

mail_from = "ahdreki@gmail.com"
mail_to = "ahdreki@gmail.com"
mail_subject = "Segurança da Tecnologia da Informação"
mail_body = "Teste do programa de autenticação por email"

mensagem = MIMEMultipart()
mensagem['From'] = mail_from
mensagem['To'] = mail_to
mensagem['Subject'] = mail_subject
mensagem.attach(MIMEText(mail_body, 'plain'))

connection = smtplib.SMTP(server, port)
connection.starttls()
connection.login(username,password)
connection.send_message(mensagem)
connection.quit()
