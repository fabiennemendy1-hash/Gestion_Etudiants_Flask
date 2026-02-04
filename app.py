from flask import Flask, render_template, request, redirect, url_for
from models import db, Etudiant, Note

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///gestion_scolaire.db'
db.init_app(app)

# 1. Le barème des 60 crédits
MATIERES_CONFIG = {
    'Informatique': 20,
    'Mathématiques': 15,
    'Anglais': 10,
    'Gestion': 15
}

# Création de la base au démarrage
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return render_template('login.html')

# 2. La route pour enregistrer une note
@app.route('/ajouter_note', methods=['POST'])
def ajouter_note():
    # On récupère les infos envoyées par le formulaire HTML
    etu_id = request.form.get('etudiant_id')
    matiere = request.form.get('matiere')
    valeur_note = float(request.form.get('note'))

    # On enregistre dans la base de données
    nouvelle_note = Note(valeur=valeur_note, matiere=matiere, etudiant_id=etu_id)
    db.session.add(nouvelle_note)
    db.session.commit()
    
    return redirect(url_for('dashboard'))

if __name__ == '__main__':
    app.run(debug=True)