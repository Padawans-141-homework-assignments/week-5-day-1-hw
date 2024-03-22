from app import db

class gen_Model(db.Model):
    __tablename__ = 'ps_generations'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(25), nullable = False, unique = True)
    price = db.Column(db.Integer, nullable = False)
    global_release_date = db.Column(db.Integer, nullable = False, unique = False)

    def add_gen(self):
        db.session.add(self)
        db.session.commit()

    def save_gen(self):
        db.session.add(self)
        db.session.commit()

    def del_gen(self):
        db.session.delete(self)
        db.session.commit()

    def from_gen(self, dict):
        for k , v in dict.items():
            setattr(self, k, v)