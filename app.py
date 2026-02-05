from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Base de données fictive pour la démonstration
etudiants = [
    {'matricule': 'ESTM-001', 'prenom': 'Sokhna', 'nom': 'DIOP', 'note': 15.5},
    {'matricule': 'ESTM-002', 'prenom': 'Fabienne', 'nom': 'MENDY', 'note': 12.0}
]

@app.route('/')
def home():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Identifiants simples pour la démo
        if request.form['username'] == 'admin' and request.form['password'] == 'estm2026':
            return redirect(url_for('dashboard'))
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html', etudiants=etudiants)

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# 1. TA BASE DE DONNÉES (La liste qui s'affiche dans le tableau de bord)
etudiants = [
    {'matricule': 'ESTM-2026-001', 'prenom': 'Awa', 'nom': 'NDIAYE', 'note': 16.5},
    {'matricule': 'ESTM-2026-002', 'prenom': 'Moussa', 'nom': 'DIALLO', 'note': 14.0},
    {'matricule': 'ESTM-2026-003', 'prenom': 'Fatou', 'nom': 'SOW', 'note': 09.5}
]

# 2. ROUTE D'ACCUEIL (Redirige vers la connexion)
@app.route('/')
def index():
    return redirect(url_for('login'))

# 3. PAGE DE CONNEXION (Vérifie admin / estm2026)
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        if username == 'admin' and password == 'estm2026':
            return redirect(url_for('dashboard'))
        else:
            return render_template('login.html', error="Identifiants incorrects")
            
    return render_template('login.html')

# 4. TABLEAU DE BORD (C'est ici que 'etudiants' est envoyé au HTML)
@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html', etudiants=etudiants)

# 5. PAGE D'AJOUT D'ÉTUDIANT
@app.route('/ajouter', methods=['GET', 'POST'])
def ajouter():
    if request.method == 'POST':
        nouveau = {
            'matricule': request.form.get('matricule'),
            'prenom': request.form.get('prenom'),
            'nom': request.form.get('nom'),
            'note': float(request.form.get('note'))
        }
        etudiants.append(nouveau)
        return redirect(url_for('dashboard'))
    return render_template('ajouter.html')

# 6. PAGE DU BULLETIN
@app.route('/bulletin/<int:id>')
def bulletin(id):
    try:
        eleve = etudiants[id]
        status = "ADMIS" if eleve['note'] >= 10 else "ÉCHEC"
        return render_template('bulletin.html', eleve=eleve, status=status)
    except IndexError:
        return "Étudiant non trouvé", 404

if __name__ == '__main__':
    app.run(debug=True)