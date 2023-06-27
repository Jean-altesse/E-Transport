from flask import Blueprint, render_template, redirect, session
from models import user_register

bp = Blueprint('dashboard', __name__)

@bp.route('/dashboard')
def dashboard():
    # Vérification de la session de l'utilisateur connecté
    if 'user_id' in session:
        user_id = session['user_id']
        # Récupérer les informations de l'utilisateur connecté depuis la base de données
        user = user_register.query.get(user_id)
        return render_template('dashboard.html', user=user)
    else:
        # Redirection vers la page de connexion si l'utilisateur n'est pas connecté
        return redirect('/')

@bp.route('/logout')
def logout():
    # Déconnexion de l'utilisateur en supprimant les informations de la session
    session.pop('user_id', None)
    return redirect('/')
