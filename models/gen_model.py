from app import db

#Model for the ps generations resource
class gen_Model(db.Model):

    #sets the table name
    __tablename__ = 'ps_generations'

    #sets the outline for the database
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(25), nullable = False, unique = True)
    price = db.Column(db.Integer, nullable = False)
    global_release_date = db.Column(db.Integer, nullable = False, unique = False)

    #adds and commits local information
    def add_gen(self):
        db.session.add(self)
        db.session.commit()

    #saves local information to the database
    def save_gen(self):
        db.session.add(self)
        db.session.commit()

    #deletes information from the database
    def del_gen(self):
        db.session.delete(self)
        db.session.commit()

    #forms the requests for the database
    def from_gen(self, dict):
        for k , v in dict.items():
            setattr(self, k, v)