from . import db
from flask_login import UserMixin

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    posts = db.relationship('Post', backref='author', lazy=True , cascade="all, delete-orphan")
    comments = db.relationship('Comment', backref='user', lazy=True, cascade="all, delete-orphan")
    likes = db.relationship('Like', backref='user', lazy=True, cascade="all, delete-orphan")

    username = db.Column( db.String(150),unique=True, nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column( db.String(255), nullable=False )

    profile_pic = db.Column(db.String(255), 
        default='images/Default-Profile-Picture.png')
    

    name = db.Column(db.String(100))
    age = db.Column(db.Integer)
    gender = db.Column(db.String(20))
    place = db.Column(db.String(100))
    interests = db.Column(db.String(300))
    specify = db.Column(db.String(300))
    cuisine = db.Column(db.String(100))
    favourite_place = db.Column(db.String(150))
    about_me = db.Column(db.Text)
    profile_description = db.Column(db.Text)

    
 
class Post(db.Model):
        id = db.Column(db.Integer, primary_key=True)

        title = db.Column(db.String(200))
        content = db.Column(db.Text)

        image = db.Column(db.String(255))

        user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

        likes = db.relationship('Like',backref='post', lazy=True, cascade="all, delete-orphan")
        comments = db.relationship('Comment',backref='post', lazy=True, cascade="all, delete-orphan")


class Like(db.Model):
            id = db.Column(db.Integer, primary_key=True)

            user_id = db.Column(
            db.Integer,
            db.ForeignKey('user.id'))

            post_id = db.Column(
            db.Integer,
            db.ForeignKey('post.id'))


class Comment(db.Model):
            id = db.Column(db.Integer, primary_key=True)

            text = db.Column(db.Text)

            user_id = db.Column(
            db.Integer,
            db.ForeignKey('user.id'))

            post_id = db.Column(
            db.Integer,
            db.ForeignKey('post.id'))


