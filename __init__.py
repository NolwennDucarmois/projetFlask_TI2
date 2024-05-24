# ce fichier initialise l'application et charge la bd

from flask import Flask
from . import routes

app = Flask(__name__)
