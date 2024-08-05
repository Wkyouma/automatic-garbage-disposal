from models.db import db
from models.user.role import Role
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model, UserMixin):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    role_id = db.Column(db.Integer, db.ForeignKey(Role.id))
    username = db.Column(db.String(50))
    email = db.Column(db.String(100))  # Adicione este campo para o email
    password = db.Column(db.String(255))

    @staticmethod
    def get_user(user_id):
        return User.query.get(int(user_id))
    
    @staticmethod
    def save_user(role_type_, username, email, password):  # Adicione o campo "email" aqui
        role = Role.get_single_role(role_type_)
        user = User(role_id=role.id, username=username, email=email, password=generate_password_hash(password))
        db.session.add(user)
        db.session.commit()

    @staticmethod
    def validate_user(email, password):
        user = User.query.filter_by(username=email).first()  # Corrija aqui
        if user is None or not check_password_hash(user.password, password):
            return None
        else:
            return user
