from models.db import db

class Lixeira(db.Model):
    __tablename__ = "lixeira"
    id = db.Column("id", db.Integer, primary_key=True)
    topic = db.Column(db.String(50))
    reads = db.relationship("Read", backref="lixeira", lazy=True)

    def save_lixeira(topico):
        lixeira = Lixeira(topic=topico)
        db.session.add(lixeira)
        db.session.commit()