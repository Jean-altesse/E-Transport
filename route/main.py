from flask import render_template, request
from models.User import db, User

# Assurez-vous que le fichier models.user est importé pour que les modèles soient disponibles

def form():
    return render_template('form.html')

def process_form():
    if request.method == 'POST':
        email = request.form['email']
        phone = request.form['phone']
        password = request.form['password']
        first_name = request.form['name']
        last_name = request.form['last_name']

        # Création d'une instance du modèle de données
        user = User(email=email, phone=phone, password=password, first_name=first_name, last_name=last_name)

        # Enregistrement de l'instance dans la base de données
        db.session.add(user)
        db.session.commit()

        return render_template('confirmation.html', email=email, first_name=first_name, last_name=last_name)
    else:
        return render_template('form.html')
