from flask import render_template, Blueprint
import datetime
from project.models import *


schedule_blueprint = Blueprint(
    'schedule', __name__,
    template_folder = 'templates'
)

@schedule_blueprint.route('/schedule')
def schedule():
    movies = {}
    localSystem = BoxOffice.query.first()
    i = 0
    while i < 4:
        movies[i] = Movie.query.filter_by(release_date=(localSystem.currentDate + datetime.timedelta(days=i*7))).all()
        i = i + 1
        
    return render_template("schedule.html", system=localSystem, movies=movies, datetime=datetime, offset=0)

@schedule_blueprint.route('/schedule/<int:offset>')
def schedules(offset):
    movies = {}
    localSystem = BoxOffice.query.first()
    i = 0
    while i < 4:
        movies[i] = Movie.query.filter_by(release_date=((localSystem.currentDate + datetime.timedelta(days=offset)) + datetime.timedelta(days=i*7))).all()
        i = i + 1
        
    return render_template("schedule.html", system=localSystem, movies=movies, datetime=datetime, offset=offset)