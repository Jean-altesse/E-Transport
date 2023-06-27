from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class UserLogin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    # Ajoutez d'autres attributs nécessaires pour la connexion
