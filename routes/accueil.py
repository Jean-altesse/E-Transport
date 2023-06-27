from flask import Blueprint, render_template

bp = Blueprint('acceuil', __name__)

@bp.route('/')
def acceuil():
    return render_template('acceuil.html')