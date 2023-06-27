from flask import Blueprint, render_template, request, redirect, session
from models import user_login

bp = Blueprint('connexion', __name__)

@bp.route('/')
def home():
    return render_template('connexion.html')

@bp.route('/connexion', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']

    # Vérification des informations de connexion
    user = user_login.query.filter_by(email=email).first()
    if user and user.password == password:
        # Connexion réussie, enregistrement de l'utilisateur dans la session
        session['user_id'] = user.id
        return redirect('/dashboard')
    else:
        # Informations de connexion invalides, affichage d'un message d'erreur
        return render_template('connexion.html', error='Invalid email or password')
