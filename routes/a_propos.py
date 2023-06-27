from flask import Blueprint, render_template

bp = Blueprint('a_propos', __name__)

@bp.route('/')
def a_propos():
    return render_template('a_propos.html')