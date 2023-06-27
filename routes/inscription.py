from flask import Blueprint, render_template

bp = Blueprint('inscription', __name__)

@bp.route('/')
def inscription():
    return render_template('inscription.html')