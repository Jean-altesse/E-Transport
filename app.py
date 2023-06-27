# from flask import Flask ,render_template
# from models.User import db
# from routes.main import *
# from routes import login_routes, dashboard_routes

# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'  # Configuration de la base de données SQLite
# db.init_app(app)

# app.register_blueprint(login_routes.bp)
# app.register_blueprint(dashboard_routes.bp)


# if __name__ == '__main__':
#     app.run()

from flask import Flask, render_template
from routes.main import bp as main_bp
from routes import accueil, compagnies, historiques, a_propos, inscription, connexion


app = Flask(__name__)
app.register_blueprint(main_bp)
app.register_blueprint(accueil.bp)
app.register_blueprint(compagnies.bp)
app.register_blueprint(historiques.bp)
app.register_blueprint(a_propos.bp, url_prefix='/a_propos')  # Enregistrement avec le préfixe '/a_propos'
app.register_blueprint(inscription.bp, url_prefix='/inscription') 
app.register_blueprint(connexion.bp, url_prefix='/connexion')

if __name__ == '__main__':
    app.run()

















# from flask_sqlalchemy import SQLAlchemy , jsonify, request
# from models.User import User
# from models.voyage import Voyage

# app = SQLAlchemy(__name__)


# @app.route('/inscrit',methode=['GET','POST'])
# def inscrit():
#     if request.methode == 'POST':
#         username = request.form.get('username')
#     new_user = User(name = name)

#     db.session.add(new_user)
#     db.session.commmit()

# @app.route('/login',methode=['GET','POST'])
# def login():
#     username = request.form.get('username')
#     user = User.query.filter_by(user = user).first()


# from flask import Flask, render_template, request
# from flask_sqlalchemy import SQLAlchemy


# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'  # Configuration de la base de données SQLite
# db = SQLAlchemy(app)

# @app.route('/process_form', methods=['POST'])
# def process_form():
#     if request.method == 'POST':
#         email = request.form['email']
#         phone = request.form['phone']
#         password = request.form['password']
#         first_name = request.form['name']
#         last_name = request.form['last_name']
#         gender = request.form['radiogroup1']
#         terms_accepted = 'cb1' in request.form  # Vérifier si la case à cocher a été cochée

#         # Faites quelque chose avec les données récupérées du formulaire

#         return render_template('confirmation.html')  # Afficher une page de confirmation
#     else:
#         return render_template('form.html')  # Afficher le formulaire initial

# if __name__ == '__main__':
#     app.run()
