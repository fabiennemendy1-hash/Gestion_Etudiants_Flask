from flask import Flask, render_template, request, redirect, url_for
from models import db, Etudiant, Note

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///gestion_scolaire.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

# Le barème officiel de votre projet
MATIERES_CONFIG = {
    'Informatique': 20,
    'Mathématiques': 15,
    'Anglais': 10,
    'Gestion': 15
}

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return render_template('login.html')

# ROUTE POUR LE DASHBOARD (Rôle du Dév 4)
@app.route('/dashboard')
def dashboard():
    etudiants = Etudiant.query.all()
    return render_template('dashboard.html', etudiants=etudiants)

# ROUTE POUR LE BULLETIN (Rôle du Dév 5 - Calcul des 60 crédits)
@app.route('/bulletin/<int:etu_id>')
def bulletin(etu_id):
    etu = Etudiant.query.get(etu_id)
    notes = Note.query.filter_by(etudiant_id=etu_id).all()
    
    total_credits = 0
    for n in notes:
        if n.valeur >= 10:
            total_credits += MATIERES_CONFIG.get(n.matiere, 0)
            
    admis = total_credits >= 60
    return render_template('bulletin.html', etudiant=etu, notes=notes, total=total_credits, admis=admis)

# ROUTE POUR AJOUTER UNE NOTE (Rôle du Dév 2)
@app.route('/ajouter_note', methods=['POST'])
def ajouter_note():
    etu_id = request.form.get('etudiant_id')
    matiere = request.form.get('matiere')
    valeur = float(request.form.get('note'))
    
    nouvelle_note = Note(valeur=valeur, matiere=matiere, etudiant_id=etu_id)
    db.session.add(nouvelle_note)
    db.session.commit()
    return redirect(url_for('dashboard'))

if __name__ == '__main__':
    app.run(debug=True)