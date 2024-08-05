from models import db

class Role(db.Model):
    __tablename__ = "role"
    id = db.Column("id", db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)

    def save_role(name):
        role = Role(name=name)
        db.session.add(role)
        db.session.commit()
    
    @staticmethod
    def get_single_role(name):
        role = Role.query.filter(Role.name == name).first()
        return role  # Retorna o objeto Role completo, não apenas o ID
