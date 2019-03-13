from project import db, bcryptObj
import bcrypt

from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

class Announcement(db.Model):

    __tablename__ = "announcements"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)

    def __init__(self, title, description):
        self.title = title
        self.description = description


class Movie(db.Model):
    __tablename__ = "movies"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    studio = db.Column(db.String, nullable=False)
    genre = db.Column(db.String, nullable=False)
    status = db.Column(db.String, nullable=False)
    budget = db.Column(db.Integer, nullable=False)
    budget_spent = db.Column(db.Integer, nullable=False)
    advertising = db.Column(db.Integer, nullable=False)
    advertising_spent = db.Column(db.Integer, nullable=False)
    poster = db.Column(db.String)
    dom_gross = db.Column(db.String, nullable=False)
    int_gross = db.Column(db.String, nullable=False)
    china_gross = db.Column(db.String, nullable=False)
    release_date = db.Column(db.Date, nullable=True)
    production_date = db.Column(db.Date, nullable=True)

    def __init__(self, title, studio, genre, budget, curDate):
        self.title = title
        self.studio = studio
        self.genre = genre
        self.status = "Pre-production"
        self.budget = budget
        self.budget_spent = 0
        self.advertising = 0
        self.advertising_spent = 0
        self.poster = ""
        self.dom_gross = 0
        self.int_gross = 0
        self.china_gross = 0
        self.release_date = None
        self.production_date = curDate


class Studio(db.Model):
    __tablename__ = "studio"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    user = db.Column(db.String, nullable=False)
    cash = db.Column(db.Integer, nullable=False)

    def __init__(self, name, user, cash):
        self.name = name
        self.user = user
        self.cash = cash
        

class BoxOffice(db.Model):
    __tablename__ = "boxoffice"

    id = db.Column(db.Integer, primary_key=True)
    currentDate = db.Column(db.Date, nullable=False)

    def __init__(self, curDate):
        self.currentDate = curDate


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    studio = db.Column(db.String, nullable=False)
    isAdmin = db.Column(db.Boolean, nullable=False)
    cash = db.Column(db.Integer)

    def __init__(self, name, email, studio, password):
        self.name = name
        self.email = email
        self.studio = studio
        self.cash = 150
        pwhash = bcrypt.hashpw(password.encode('utf8'), bcrypt.gensalt())
        self.password = pwhash.decode('utf8')
        self.isAdmin = False
        
    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)

class DateChange(db.Model):
    __tablename__ = "datechanges"
    
    id = db.Column(db.Integer, primary_key=True)
    movie = db.Column(db.String, nullable=False)
    studio = db.Column(db.String, nullable=False)
    dateOfChange = db.Column(db.Date, nullable=False)
    oldDate = db.Column(db.Date)
    newDate = db.Column(db.Date, nullable=False)

    def __init__(self, movie, studio, dateOfChange, oldDate, newDate):
        self.movie = movie
        self.studio = studio
        self.dateOfChange = dateOfChange
        self.oldDate = oldDate
        self.newDate = newDate


class MovieChange(db.Model):
    __tablename__ = "moviechanges"

    id = db.Column(db.Integer, primary_key=True)
    movie = db.Column(db.String, nullable=False)
    studio = db.Column(db.String, nullable=False)
    dateOfChange = db.Column(db.Date, nullable=False)
    created = db.Column(db.Boolean, nullable=False)

    def __init__(self, movie, studio, dateOfChange, created):
        self.movie = movie
        self.studio = studio
        self.dateOfChange = dateOfChange
        self.created = created