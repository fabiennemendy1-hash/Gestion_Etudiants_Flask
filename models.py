from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Table des Utilisateurs (Login)
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(100))
    role = db.Column(db.String(20)) # Admin, Enseignant ou Etudiant

# Table des Étudiants
class Etudiant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    matricule = db.Column(db.String(20), unique=True)
    nom = db.Column(db.String(50))
    prenom = db.Column(db.String(50))
    filiere = db.Column(db.String(50))

# Table des Notes
class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    valeur = db.Column(db.Float)
    matiere = db.Column(db.String(50))
    etudiant_id = db.Column(db.Integer, db.ForeignKey('etudiant.id'))