import p04_autenticacao_multifator, p04_email
import pyrebase

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


def cadastro():
    print("")
    user = input("Digite seu e-mail: ")
    password = input("Digite sua senha, com pelo menos 6 caracteres: ")

    if p04_email.encontrar_autenticado(user):
        status = auth.create_user_with_email_and_password(user, password)
        print("")
        print("Resultado: ", status)
    else:
        print("")
        print("Este email não está autenticado.")


if __name__ == '__main__':
    p04_autenticacao_multifator.select_menu()