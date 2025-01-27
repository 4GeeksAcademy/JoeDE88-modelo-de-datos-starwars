import os
import sys
import enum
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
    username = db.Column(db.String(50), nullable=False,unique=True)
    firstname = db.Column(db.String(50),nullable=False)
    lastname = db.Column(db.String(50),nullable=False)
    email = db.Column(db.String(50), nullable=False,unique=True)

class FavoriteTypeEnum(enum.Enum):
    Planets = "planets"
    People = "people"
    Films = "films"

class Favorites(db.Model):
    __tablename__ = 'favorites'
    id = db.Column(db.Integer,unique=True, primary_key=True,index=True)
    user_id = db.Column(db.Integer, ForeignKey('user.id'),nullable=False)
    external_id = db.Column(db.Integer,nullable=False)
    name = db.Column(db.String(50), unique=True,nullable=False)
    type = db.Column(db.Enum(FavoriteTypeEnum),nullable=False)

class Films(db.Model):
    __tablename__ = 'films'
    id = db.Column(db.Integer,primary_key=True,unique=True)
    title = db.Column(db.String(50),nullable=False,unique=True)
    episode = db.Column(db.Integer,nullable=False,unique=True)
    release_date = db.Column(db.Integer,nullable=False)
    director = db.Column(db.String(50),nullable=False)
    producer = db.Column(db.String(50),nullable=False)

class Planets(db.Model):
    __tablename__ = 'planets'
    id = db.Column(db.Integer,primary_key=True,unique=True,nullable=False)
    name = db.Column(db.String(50),nullable=False,unique=True)
    population = db.Column(db.Integer,nullable=False)
    climate = db.Column(db.String(50),nullable=False)
    diameter = db.Column(db.String(50),nullable=False)
    gravity = db.Column(db.Integer,nullable=False)

class People(db.Model):
    __tablename__ = 'people'
    id = db.Column(db.Integer,primary_key=True,unique=True,nullable=False)
    name = db.Column(db.String(50),unique=True,nullable=False)
    species = db.Column(db.String(50),nullable=False)
    skin_color = db.Column(db.String(50),nullable=False)
    hair_color = db.Column(db.String(50),nullable=False)
    height = db.Column(db.Integer,nullable=False)
    homeworld = db.Column(db.String,ForeignKey('planets.id'),nullable=False)


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(db.Model, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e