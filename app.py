from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

etudiants = [
    {'matricule': 'RT-2026-001', 'prenom': 'Abdou', 'nom': 'SARR', 'note': 14.5, 'filiere': 'Réseaux & Télécoms'},
    {'matricule': 'CPTA-2026-012', 'prenom': 'Fatou', 'nom': 'BA', 'note': 12.0, 'filiere': 'Comptabilité'},
    {'matricule': 'CIM-2026-045', 'prenom': 'Moussa', 'nom': 'DIALLO', 'note': 15.75, 'filiere': 'Communication & Multimédia'},
    {'matricule': 'DRT-2026-009', 'prenom': 'Awa', 'nom': 'GUEYE', 'note': 9.5, 'filiere': 'Droit des Affaires'}
]

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] == 'admin' and request.form['password'] == 'estm2026':
            return redirect(url_for('dashboard'))
        else:
            error = "Identifiants invalides."
    return render_template('login.html', error=error)

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html', etudiants=etudiants)

@app.route('/ajouter', methods=['GET', 'POST'])
def ajouter():
    if request.method == 'POST':
        nouvel_etudiant = {
            'matricule': request.form['matricule'].upper(),
            'prenom': request.form['prenom'].capitalize(),
            'nom': request.form['nom'].upper(),
            'filiere': request.form['filiere'],
            'note': float(request.form['note'])
        }
        etudiants.append(nouvel_etudiant)
        return redirect(url_for('dashboard'))
    return render_template('ajouter.html')

@app.route('/bulletin/<int:id>')
def bulletin(id):
    try:
        eleve = etudiants[id]
        status = "ADMIS" if eleve['note'] >= 10 else "AJOURNÉ"
        return render_template('bulletin.html', eleve=eleve, status=status)
    except IndexError:
        return "Étudiant non trouvé", 404

if __name__ == '__main__':
    app.run(debug=True, port=5000)