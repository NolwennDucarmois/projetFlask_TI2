# ce fichier contiendra toutes les chemins d'accès vers les pages

from . import app, models
from flask import render_template, url_for, request  # render_template = va permettre de retourner les pages


@app.route('/')
@app.route('/accueil')
def accueil():
    liste = models.vue_instruments.query.all()
    return render_template('accueil.html', title='Mel''Instruments', liste_instru=liste)


@app.route('/instruments')
def instruments():
    liste = models.vue_instruments.query.all()  # on va retourner tous les instruments dans la vue
    return render_template('instruments.html', title='Mel''Instruments', liste_instru=liste)


@app.route('/infos')
def infos():
    id = request.args.get('id_instrument')
    liste = models.vue_instruments.query.filter_by(id_instrument=id)
    return render_template('infos.html', title='Mel''Instruments', infos=liste)


@app.route('/marques')
# j'ai constaté que je pouvais pas avoir plusieurs focntions par app.route
def marques():
    marques = models.vue_marque.query.all()
    liste = []
    for d in marques:
        instruments = models.vue_instruments.query.filter_by(nom_marque=d.nom_marque)
        instruments_list = [instrument.nom_instrument for instrument in instruments]
        liste.append({
            'nom_marque': d.nom_marque,
            'instruments': instruments_list
        })
    return render_template('marques.html', title='Mel''Instruments', marques=liste)
