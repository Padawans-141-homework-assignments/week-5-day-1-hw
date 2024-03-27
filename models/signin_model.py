from werkzeug.security import generate_password_hash, check_password_hash
from app import db

class make_usr_model(db.Model):
    
    #names the table
    __tablename__ = 'users'

    db_id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(50), nullable = False, unique = True)
    email = db.Column(db.String, nullable = False, unique = True)
    password_hash = db.Column(db.String, nullable = False)
    first_name = db.Column(db.String(25))
    last_name = db.Column(db.String(25))

    #adds and commits local information
    def add_usr(self):
        db.session.add(self)
        db.session.commit()

    #saves local information to the database
    def save_usr(self):
        db.session.add(self)
        db.session.commit()

    #deletes information from the database
    def del_usr(self):
        db.session.delete(self)
        db.session.commit()

    #forms the requests for the database
    def from_usr(self, dict):
        for k, v in dict.items():
            if k != 'password':
                setattr(self, k, v)	##sets attribute
            else:
                setattr(self, 'password_hash', generate_password_hash(v))

    def check_usr_password(self, password):
        return check_password_hash(self.password_hash, password)