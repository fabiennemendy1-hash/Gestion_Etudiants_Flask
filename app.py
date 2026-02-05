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

@app.route('/ajouter', methods=['GET', 'POST'])
def ajouter():
    if request.method == 'POST':
        nouvel_eleve = {
            'matricule': request.form['matricule'],
            'prenom': request.form['prenom'],
            'nom': request.form['nom'],
            'note': float(request.form['note'])
        }
        etudiants.append(nouvel_eleve)
        return redirect(url_for('dashboard'))
    return render_template('ajouter.html')

@app.route('/bulletin/<int:id>')
def bulletin(id):
    eleve = etudiants[id]
    status = "ADMIS" if eleve['note'] >= 10 else "AJOURNÉ"
    return render_template('bulletin.html', eleve=eleve, status=status)

if __name__ == '__main__':
    app.run(debug=True)