


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

firebase = pyrebase.initialize_app(firebaseConfig)

db = firebase.database()

# # insert
# data = {"email":"eli@gmail.com", "cod_auth":"fqrtfwyybilfdigw",
#         "date_auth":str(date.today())}
# db.child("users").push(data)

# # update
# db.child("users").child("-NEqYGF7kdQMSa7u20Pa").update({
#    "date_auth":"2022-10-19"})

# # read all users
# users = db.child("users").get()
# i = 1
# for user in users.each():
#     print("*** usuário {} ***".format(i))
#     print("valores: ", user.val())
#     print("chave: ", user.key())
#     i += 1
#
# # update um dado especifico
# users = db.child("users").get()
# for user in users.each():
#     if user.val()["email"] == "ahdreki@gmail.com":
#         db.child("users").child(user.key()).update({
#     "date_auth":"2022-10-19"})

# read
users = db.child("users").order_by_child("email").equal_to(
    "ahdreki@gmail.com").get()
for user in users.each():
    print(user.val())
