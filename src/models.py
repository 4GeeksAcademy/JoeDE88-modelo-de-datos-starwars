import os
import sys
from sqlalchemy import ForeignKey, Integer, String
from eralchemy2 import render_er
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:////tmp/test.db"
app.config["SQLALCHEMY_ECHO"] = True
db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True,unique=True,index=True,nullable=False)
    username = db.Column(db.String(50), nullable=False)
    firstname = db.Column(db.String(50))
    lastname = db.Column(db.String(50))
    email = db.Column(db.String(50), nullable=False)

class Post(db.Model):
    __tablename__ = 'post'
    id = db.Column(db.Integer, unique=True, primary_key=True)
    user_id = db.Column(db.Integer, ForeignKey('user.id'),nullable=False)

class Comment(db.Model):
    __tablename__ = 'comment'
    id = db.Column(db.Integer,primary_key=True)
    comment_text = db.Column(db.String(500), nullable=True)
    author_id = db.Column(db.Integer,ForeignKey('user.id'),nullable=False)
    post_id = db.Column(db.Integer,ForeignKey('post.id'),nullable=False)

class Media(db.Model):
    __tablename__ = 'media'
    id = db.Column(db.Integer,primary_key=True,nullable=False)
    type = db.Column(db.String(50),nullable=True)
    url = db.Column(db.String(100),nullable=True)
    post_id = db.Column(db.Integer,ForeignKey('post.id'),nullable=False)

class Follower(db.Model):
    __tablename__ = 'follower'
    user_from_id = db.Column(db.Integer,ForeignKey('post.id'),primary_key=True)
    user_to_id = db.Column(db.Integer,ForeignKey('post.id'),primary_key=True)


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(db.Model, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e