from flask import Flask
from config import email, mail_senha

app = Flask(__name__)
app.secret_key = 'setape'
app.config.from_object('config')

mail_settings = {
    "MAIL_SERVER": 'smtp.gmail.com',
    "MAIL_PORT": 465,
    "MAIL_USE_TLS": False,
    "MAIL_USE_SSL": True,
    "MAIL_USERNAME": email,
    "MAIL_PASSWORD": mail_senha
}

app.config.update(mail_settings)

from views import route