from flask import Blueprint, render_template

bp = Blueprint('compagnies', __name__)

@bp.route('/')
def compagnies():
    return render_template('compagnies.html')