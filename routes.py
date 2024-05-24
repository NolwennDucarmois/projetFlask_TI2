# ce fichier contiendra toutes les chemins d'accès vers les pages

from . import app, models
from flask import render_template, url_for  # va permettre de retourner les pages


@app.route('/')
@app.route('/accueil')
def accueil():
    return render_template('accueil.html', title='Mel''Instruments')


@app.route('/instruments')
def instruments():
    liste = models.vue_instruments.query.all()  # on va retourner tous les instruments dans la vue
    return render_template('instruments.html', title='Mel''Instruments', liste_instru=liste)
