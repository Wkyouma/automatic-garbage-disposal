from models.db import db
from models.iot.lixeira import Lixeira
from datetime import datetime

class Read(db.Model):
    __tablename__ = "read"
    id = db.Column("id", db.Integer, primary_key=True)
    read_datetime = db.Column(db.DateTime())
    lixeira_id = db.Column(db.Integer, db.ForeignKey(Lixeira.id))
    peso = db.Column(db.Float)
    altura = db.Column(db.Float)

    def save_read(lixeira_id, peso, altura):
        lixeira = Lixeira.query.filter(Lixeira.id == lixeira_id)
        if lixeira is not None:
            read = Read(read_datetime=datetime.now(), lixeira_id=lixeira_id, peso=float(peso), altura=float(altura))
            db.session.add(read)
            db.session.commit()
