from flask import Blueprint, render_template

bp = Blueprint('connexion', __name__)

@bp.route('/')
def connexion():
    return render_template('connexion.html')