from flask import Blueprint, render_template

bp = Blueprint('historiques', __name__)

@bp.route('/')
def historiques():
    return render_template('historiques.html')