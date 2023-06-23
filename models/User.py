from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)
class User(db.Model):
    pass
