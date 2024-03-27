from app import db

#Model for the ygo card resource
class ygo_Model(db.Model):

    #sets table name
    __tablename__ = 'fav_cards'

    #sets the outline for the database table
    db_id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(42), nullable = False, unique = True) #unique
    effect = db.Column(db.String, nullable = False, unique = True) #unique
    attribute = db.Column(db.String(9), nullable = False)
    level_rank_link_rating = db.Column(db.Integer, nullable = False)
    type = db.Column(db.String, nullable = False)
    card_type = db.Column(db.String, nullable = False)
    atk = db.Column(db.Integer)

    defense = db.Column(db.Integer, nullable = True)
    summon_requirement = db.Column(db.String, nullable = True)

    #adds and commits local information
    def add_ygo(self):
        db.session.add(self)
        db.session.commit()

    #saves local information to the database
    def save_ygo(self):
        db.session.add(self)
        db.session.commit()

    #deletes information from the database
    def del_ygo(self):
        db.session.delete(self)
        db.session.commit()

    #forms the requests for the database
    def from_ygo(self, dict):
        for k , v in dict.items():
            setattr(self, k, v)