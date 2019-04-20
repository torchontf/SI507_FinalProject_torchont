## __author__ == "torchont (Tasha Torchon)"
# SI 507 - Final Project
# Models

# Import statements
from movies_db import db

actor_set = db.Table("actor_set",db.Column("actor_id",db.Integer, db.ForeignKey("actors.id")),db.Column("movie_id",db.Integer, db.ForeignKey("movies.id")))

genre_set = db.Table("genre_set",db.Column("genre_id",db.Integer, db.ForeignKey("genres.id")),db.Column("movie_id",db.Integer, db.ForeignKey("movies.id")))

class Movie(db.Model):
    __tablename__ = "movies"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250),unique=True)
    year = db.Column(db.Integer)#, primary_key=True); a string in the system
    mpaa_rating = db.Column(db.String(10))
    runtime = db.Column(db.String(20))
    genre = db.relationship("Genre",secondary=genre_set,backref=db.backref("movies",lazy="dynamic"),lazy="dynamic") #many to many?
    director_id = db.Column(db.Integer, db.ForeignKey("directors.id"))
    actor_id = db.relationship("Movie",secondary=actor_set,backref=db.backref("actors",lazy="dynamic"),lazy="dynamic")#many to many?
    plot = db.Column(db.String(250)) #long
    language = db.Column(db.String(64)) #can be many but keep as one? no table for now
    country = db.Column(db.String(64)) #keep? no table for now
    # awards = "" #not a list. keep? Won 1 Oscar. Another 5 wins & 8 nominations
    poster = db.Column(db.String(250))
    imdb_rating = db.Column(db.Integer) #but would prefer as integer
    imdb_votes = db.Column(db.Integer) # but would prefer as integer
    prod_comp_id = db.Column(db.Integer, db.ForeignKey("prod_comps.id")) #is this worth keeping?

    def __repr__(self):
        return "{}".format(self.title)#, self.genre)


class Genre(db.Model):
    __tablename__ = "genres"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(65))

    def __repr__(self):
        return "{} (ID: {})".format(self.name,self.id)


class Director(db.Model):
    __tablename__ = "directors"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    movies = db.relationship('Movie',backref='Director')

    def __repr__(self):
        return "{} (ID: {})".format(self.name,self.id)


class Actor(db.Model):
    __tablename__ = "actors"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    birthdate = db.Column(db.String(64)) #date object?
    birthplace = db.Column(db.String(64))

def __repr__(self):
    return "{} (ID: {})".format(self.name,self.id)



class Production_Company(db.Model):
    __tablename__ = "prod_comps"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    location = db.Column(db.String(64))
    movies = db.relationship('Movie',backref='Production_Company')

    def __repr__(self):
        return "{} (ID: {})".format(self.name,self.id)


##### HELPER FUNCTION ####
def get_or_create_director(director_name):
    director = Director.query.filter_by(name=director_name).first()
    if director:
        return director
    else:
        director = Director(name=director_name)
        session.add(director)
        session.commit()
        return director
