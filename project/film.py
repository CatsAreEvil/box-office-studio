# movie = database object, film = runtime object
import datetime

class Film():
    def __init__(self, movie):
        #database fields
        self.movie = movie
        self.title = movie.title
        self.studio = movie.studio
        self.genre = movie.genre
        self.status = movie.status
        self.budget = movie.budget
        self.budget_spent = movie.budget_spent
        self.advertising = movie.advertising
        self.advertising_spent = movie.advertising_spent
        self.dom_gross = movie.dom_gross
        self.int_gross = movie.int_gross
        self.china_gross = movie.china_gross
        self.release_date = movie.release_date
        self.production_date = movie.production_date
        self.poster = movie.poster

        #calculated fields
        self.scale = round(((self.budget * self.getGenreScale(self.genre)) + 500) / 30)
        self.pre_production_end = self.production_date + datetime.timedelta(days=self.scale * 0.25)
        self.filming_end = self.production_date + datetime.timedelta(days=self.scale * 0.75)
        self.end_date = self.production_date + datetime.timedelta(days=self.scale) #date movie finishes filming


    def update(self, currentDate):
        if self.status == "Pre-production":
            if currentDate > self.pre_production_end:
                self.status = "Filming"
            
        if self.status == "Filming":
            if currentDate > self.filming_end:
                self.status = "Post-production"
            
        if self.status == "Post-production":
            if currentDate > self.end_date:
                self.status = "Finished"

        if self.status == "Finished":
            if self.release_date != None:
                if currentDate > self.release_date:
                    self.status = "Released"

        # update db fields
        self.updateDB
        
    def updateDB(self):
        self.movie.status = self.status
        self.movie.budget = self.budget
        self.movie.budget_spent = self.budget_spent
        self.movie.advertising = self.advertising
        self.movie.advertising_spent = self.advertising_spent
        self.movie.dom_gross = self.dom_gross
        self.movie.int_gross = self.int_gross
        self.movie.china_gross = self.china_gross
        self.movie.release_date = self.release_date
        self.movie.poster = self.poster


    def getGenreScale(self, genre):
        if genre == "Sci-Fi":
            scale = 10
        elif genre == "Fantasy":
            scale = 8
        elif genre == "Drama":
            scale = 2
        elif genre == "Horror":
            scale = 4
        elif genre == "Comedy":
            scale = 3
        elif genre == "War":
            scale = 6
        elif genre == "Superhero":
            scale = 8
        elif genre == "Action":
            scale = 6
        
        return scale
