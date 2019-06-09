from flask import render_template, Blueprint, request
from project.models import *
from project import db
from flask_login import current_user
import datetime

admin_blueprint = Blueprint(
    'admin', __name__,
    template_folder = 'templates'
)

@admin_blueprint.route('/admin', methods=['GET', 'POST'])
def admin():
    localSystem = BoxOffice.query.first()
    if request.method == 'POST':
        if request.form['submit_button'] == 'Next week':
            
            # change date
            lastDay = localSystem.currentDate
            nextDay = localSystem.currentDate + datetime.timedelta(days=1)
            localSystem.currentDate = nextDay

            # remove old announcemnts/changes
            # update movies
            movies = db.session.query(Movie).all()
            for movie in movies:
                lastDayGross = Results.query.filter_by(movie=movie.title, date=lastDay).first()
                movie.update(localSystem.currentDate, lastDayGross)
                if movie.status == "Released":
                    gross = movie.cur_gross
                    if gross > 0:
                        result = Results(localSystem.currentDate, movie.title, gross)
                        db.session.add(result)

            # create announcments

            db.session.commit()
        elif request.form['submit_button'] == 'Reset':
            BoxOffice.query.delete()
            db.session.add(BoxOffice("2019-3-1"))
            DateChange.query.delete()
            Movie.query.delete()
            MovieChange.query.delete()
            Results.query.delete()
            for user in db.session.query(User).all():
                user.cash = 150

            db.session.commit()

    return render_template('admin.html', user=current_user, system=localSystem)