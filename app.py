from flask_sqlalchemy import SQLAlchemy , jsonify, request
from models.User import User
from models.voyage import Voyage

app = SQLAlchemy(__name__)


@app.route('/inscrit',methode=['GET','POST'])
def inscrit():
    if request.methode == 'POST':
        username = request.form.get('username')
    new_user = User(name = name)

    db.session.add(new_user)
    db.session.commmit()

@app.route('/login',methode=['GET','POST'])
def login():
    username = request.form.get('username')
    user = User.query.filter_by(user = user).first()
