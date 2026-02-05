from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# --- DONNÉES DE TEST ---
etudiants = [
    {'matricule': 'ESTM-2026-001', 'prenom': 'Awa', 'nom': 'NDIAYE', 'note': 16.5},
    {'matricule': 'ESTM-2026-002', 'prenom': 'Moussa', 'nom': 'DIALLO', 'note': 14.0},
    {'matricule': 'ESTM-2026-003', 'prenom': 'Fatou', 'nom': 'SOW', 'note': 09.5}
]

# --- 1. PAGE D'ACCUEIL (PORTAIL PUBLIC) ---
@app.route('/')
def index():
    # Cette fonction s'appelle 'index' pour ne pas créer de conflit avec 'login'
    return render_template('accueil.html')

# --- 2. PAGE DE CONNEXION ---
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        if username == 'admin' and password == 'estm2026':
            return redirect(url_for('dashboard'))
        else:
            error = "Identifiants invalides. Veuillez réessayer."
            
    return render_template('login.html', error=error)

# --- 3. TABLEAU DE BORD (ESPACE PRIVÉ) ---
@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html', etudiants=etudiants)

# --- 4. AJOUTER UN ÉTUDIANT ---
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

# --- 5. BULLETIN DE NOTES ---
@app.route('/bulletin/<int:id>')
def bulletin(id):
    try:
        eleve = etudiants[id]
        status = "ADMIS" if eleve['note'] >= 10 else "ÉCHEC"
        return render_template('bulletin.html', eleve=eleve, status=status)
    except IndexError:
        return "Étudiant introuvable", 404

if __name__ == '__main__':
    app.run(debug=True)