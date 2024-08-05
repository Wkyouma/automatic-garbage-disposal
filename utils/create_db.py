from flask import Flask
from models import *

def create_db(app: Flask):
    with app.app_context():
        db.drop_all()
        db.create_all()
        Role.save_role("admin")
        Role.save_role("estatico")
        Role.save_role("operador")
        User.save_user("admin", "admin", "admin", "senha_admin")  # Substitua "senha_admin" pela senha desejada
