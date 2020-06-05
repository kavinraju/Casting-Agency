from sqlalchemy import Column, Integer, String, Table, DateTime, ForeignKey
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import datetime
import json

""" keystore consists of all the passwords required for the backend """
from environments.config import database_uri, SQLALCHEMY_TRACK_MODIFICATIONS

database_path_default = database_uri

db = SQLAlchemy()

def setup_db(app, database_path=database_path_default):
    #app.config.from_pyfile('environments\config\config.py')
    app.config['SQLALCHEMY_DATABASE_URI'] = database_path
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = SQLALCHEMY_TRACK_MODIFICATIONS
    db.app = app
    db.init_app(app)
    migrate = Migrate(app, db)
    db.create_all() # TODO Uncomment this while running the unit test for the first time.


movie_actors = db.Table('movie_actors',
        Column('actor_id', Integer, ForeignKey('actors.id'), primary_key=True),
        Column('movie_id', Integer, ForeignKey('movies.id'), primary_key=True)
    )

class Movie(db.Model):
    __tablename__ = 'movies'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    release_date = Column(DateTime(), default=datetime.utcnow, nullable=False)

    actors = db.relationship('Actor', secondary=movie_actors ,backref=db.backref('movies', lazy=True))

    def __init__(self, title, release_date):
        self.title = title
        self.release_date = release_date

    def insert(self):
        db.session.add(self)
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()
    
    def update(self):
        db.session.commit()

    def __repr__(self):
        return '<' + 'Movie: ' + self.title + ' Release Date: ' + str(self.release_date) + '>'
    
    def format(self):
        return {
            'id': self.id,
            'title': self.title,
            'release_date': self.release_date
            #'actors': json.dumps(self.actors)
        }
 
    

class Actor(db.Model):
    __tablename__ = 'actors'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    gender = Column(String(6), nullable=False)

    #movies = Column(Integer, db.ForeignKey('movies.id', onupdate='cascade', ondelete='set null'))
    #movies = db.relationship('Movie', secondary=movie_actors, backref=db.backref('actors', lazy=True))

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def insert(self):
        db.session.add(self)
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()
    
    def update(self):
        db.session.commit()


    def format(self):
        return {
            'id': self.id,
            'name': self.name,
            'gender': self.gender,
            'age': self.age
        }

    def __repr__(self):
        return '<' + 'Actor: ' + self.name + ' Gender: ' + self.gender + ' Age: ' + str(self.age) + '>'