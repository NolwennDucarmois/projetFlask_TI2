# ce fichier initialise l'application et charge la bd

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)  # création d'un objet Flask

# clé étrangère générée dans la console python
app.config['SECRET_KEY'] = '57c0c963042963035c5454033ff75bb2'

# pour supprimer les notifications inutiles venu de la bd
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# lien avec la db
app.config["SQLALCHEMY_DATABASE_URI"] ='postgresql://anonyme:admin@localhost/projetTI'

# Instanciation d'un objet SQLAlchemy
db = SQLAlchemy(app)

from . import routes
