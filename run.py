# ce fichier sert un lancer l'application

from flask import Flask

app = Flask(__name__)

if __name__ == '__main__':
    app.run()