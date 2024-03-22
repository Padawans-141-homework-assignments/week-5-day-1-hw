from app import db

class ygo_Model(db.Model):
    __tablename__ = 'fav_cards'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(42), nullable = False, unique = True) #unique
    effect = db.Column(db.String, nullable = False, unique = True) #unique
    attribute = db.Column(db.String(9), nullable = False)
    level_rank_link_rating = db.Column(db.Integer, nullable = False)
    type = db.Column(db.String, nullable = False)
    card_type = db.Column(db.String, nullable = False)
    atk = db.Column(db.Integer)

    defense = db.Column(db.Integer, nullable = True)
    summon_requirement = db.Column(db.String, nullable = True)

    def add_ygo(self):
        db.session.add(self)
        db.session.commit()

    def save_ygo(self):
        db.session.add(self)
        db.session.commit()

    def del_ygo(self):
        db.session.delete(self)
        db.session.commit()

    def from_ygo(self, dict):
        for k , v in dict.items():
            setattr(self, k, v)