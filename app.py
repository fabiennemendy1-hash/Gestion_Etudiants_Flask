from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Base de données temporaire pour la démo
etudiants = []

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = request.form.get('username')
        pwd = request.form.get('password')
        if user == 'admin' and pwd == 'estm2026':
            return redirect(url_for('dashboard'))
        return "Erreur : Identifiants incorrects !"
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html', etudiants=etudiants)

@app.route('/ajouter', methods=['GET', 'POST'])
def ajouter():
    if request.method == 'POST':
        etudiant = {
            'prenom': request.form.get('prenom'),
            'nom': request.form.get('nom'),
            'matricule': request.form.get('matricule'),
            'note': float(request.form.get('note') or 0)
        }
        etudiants.append(etudiant)
        return redirect(url_for('dashboard'))
    return render_template('ajouter.html')

@app.route('/bulletin/<int:id>')
def bulletin(id):
    eleve = etudiants[id]
    status = "ADMIS" if eleve['note'] >= 10 else "AJOURNÉ"
    return render_template('bulletin.html', eleve=eleve, status=status)

if __name__ == '__main__':
    app.run(debug=True)