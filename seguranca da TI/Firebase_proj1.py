# Atividade Prática - Firebase
# Disciplina: Segurança da Tecnologia da Informação
# Projeto 1 - Uso do Firebase para autenticação

import pyrebase

firebaseConfig = {
    "apiKey": "AIzaSyDNso_cj_DgJRUI9W_cB05n3xbovpPQ9WU",
    "authDomain": "fir-puc-sti.firebaseapp.com",
    "projectId": "fir-puc-sti",
    "databaseURL": "https://" + "fir-puc-sti" + ".firebaseio.com",
    "storageBucket": "fir-puc-sti.appspot.com",
    "messagingSenderId": "263870010434",
    "appId": "1:263870010434:web:e415896c56986be808c9db",
    "measurementId": ""
}

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()

user = input("Digite seu e-mail: ")
password = input("Digite sua senha, com pelo menos 6 caracteres: ")

#criar usuário
#status = auth.create_user_with_email_and_password(user,password)

#login
status = auth.sign_in_with_email_and_password(user,password)
idToken = status["idToken"]

print("Resultado: ", status)
print("Token: ", idToken)
print("Info: ", auth.get_account_info(idToken))
