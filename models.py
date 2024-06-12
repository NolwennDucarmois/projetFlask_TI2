from . import app, db
from flask_sqlalchemy import SQLAlchemy


class vue_instruments(db.Model):
    id_instrument = db.Column(db.Integer, primary_key=True)
    reference_instrument = db.Column(db.Text(), nullable=False)
    nom_instrument = db.Column(db.Text(), nullable=False)
    couleur_instrument = db.Column(db.Text(), nullable=False)
    prix_instrument = db.Column(db.Float(15), nullable=False)
    image_instrument = db.Column(db.Text(), nullable=False, default='default.jpg')
    id_marque = db.Column(db.Integer)
    nom_marque = db.Column(db.Text(), nullable=False)
    id_categorie = db.Column(db.Integer)
    nom_categorie = db.Column(db.Text(), nullable=False)

    def __repr__(self):  # méthode qui va afficher les données
        return f'{self.id_instrument} : {self.reference_instrument} : {self.nom_instrument} : {self.couleur_instrument} : {self.prix_instrument} : {self.image_instrument} : {self.id_marque} : {self.nom_marque} : {self.id_categorie} : {self.nom_categorie}'


class vue_marque(db.Model):
    id_marque = db.Column(db.Integer, primary_key=True);
    nom_marque = db.Column(db.Text(), nullable=False)
    id_instrument = db.Column(db.Integer)
    reference_instrument = db.Column(db.Text(), nullable=False)
    nom_instrument = db.Column(db.Text(), nullable=False)
    couleur_instrument = db.Column(db.Text(), nullable=False)
    prix_instrument = db.Column(db.Float(15), nullable=False)
    image_instrument = db.Column(db.Text(), nullable=False, default='default.jpg')
    id_categorie = db.Column(db.Integer)

    def __repr__(self):
        return f'{self.id_marque} : {self.nom_marque} : {self.id_instrument} : {self.reference_instrument} : {self.nom_instrument} : {self.couleur_instrument} : {self.prix_instrument} : {self.image_instrument} : {self.id_categorie}'
