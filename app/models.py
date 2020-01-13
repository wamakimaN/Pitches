from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin

class User(UserMixin,db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(20),index = True, unique=True,nullable = False)
    password = db.Column(db.String(60),nullable = False)
    email = db.Column(db.String(120),unique = True,index = True)
    ideas = db.relationship('Idea',backref = 'owner',lazy='dynamic')
    profile_pic = db.Column(db.String(20),nullable = False,default = 'default.jpg')

    def __repr__(self):
        return f'User ("{self.username}","{self.profile_pic}")'

class Idea(db.Model):
    __tablename__ = 'idea'

    id = db.Column(db.Integer,primary_key = True)
    title = db.Column(db.String(100),nullable = False)
    # date_posted = db.Column(db.string())
    body = db.Column(db.Text)
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'),nullable = False)
    


    def __repr__(self):
        return f'User ("{self.title}","{self.user_id}")'
