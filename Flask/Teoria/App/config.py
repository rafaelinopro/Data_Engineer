<<<<<<< HEAD
from flask import Flask
from config import *

DEBUG = True # activa la depuración en Flask
BCRYPT_LOG_ROUNDS = 12 # configuración para la extensión Flask-Bcrypt
MAIL_FROM_EMAIL = "micorreo@gmail.com"
FLASK_APP = "run.py"

SECRET_KEY = "Sm9obiBTY2hyb20ga2lja3MgYXNz"
STRIPE_API_KEY = "SmFjb2IgS2FwbGFuLU1vc3MgaXMgYSBoZXJv"
SQLALCHEMY_DATABASE_URI = (
"postgresql://user:TWljaGHFgiBCYXJ0b3N6a2lld2ljeiEh@localhost/databasename")
=======
DEBUG = True
BCRYPT_LOG_ROUNDS = 12 # configuración para la extensión Flask-Bcrypt
MAIL_FROM_EMAIL = "micorreo@gmail.com"
FLASK_APP = "app.py"
>>>>>>> 3e0e813e0ebe30255faa2393e2c8cb8cd4ac0000
