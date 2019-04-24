## __author__ == "torchont (Tasha Torchon)"
# SI 507 - Final Project
# Application

# Import statements
import os
from flask import Flask, render_template, session, redirect, url_for
from movies_db import db
from SI507project_tools import *
from movies_models import *

# Application configurations
app = Flask(__name__)
app.debug = True
app.use_reloader = True

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./finalproject_movies.db' # TODO: decide what your new database name will be -- that has to go here
app.config['SECRET_KEY'] = 'e98trdzxtyuikm4e6h'

app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

with app.app_context():
    db.init_app(app)

@app.before_first_request
def create_tables():
    db.create_all()


##### ROUTES #####
@app.route("/")
def homepage():
    movies = Movie.query.all()
    return render_template("home.html", num_movies=len(movies))


@app.route("/movie/add/<title>") #Create template to add link to all_movies
def add_movie(title):
    m_dict = getOMDb_data(title)
    if m_dict["Response"] == "False":
        error = "That movie doesn't exist. Check your spelling and try again."
        return render_template("add_movie.html", error=error)
    else:
        title = m_dict["Title"]
        if Movie.query.filter_by(title=title).first():
            error = "That movie is already in the system. Try another title."
            return  render_template("add_movie.html", error=error)#how to add main app link?
        else:
            genre_names = m_dict["Genre"].split(", ")
            g_lis = []
            for g in genre_names:
                genre = get_or_create_genre(g)
                g_lis.append(genre)
            dir_name = m_dict["Director"]
            director = get_or_create_director(dir_name) # A many to many relationship in the API, but portrayed as a one to many in this app.
            actor_names = m_dict["Actors"].split(", ")
            a_lis = []
            for a in actor_names:
                actor = get_or_create_actor(a)
                a_lis.append(actor) #many to many?; string of multiple genres

            movie = Movie(title=title,year=int(m_dict["Year"]),mpaa_rating=m_dict["Rated"],duration=m_dict["Runtime"],genre=g_lis,director_id=director.id,actor=a_lis,plot=m_dict["Plot"],language=m_dict["Language"],country=m_dict["Country"],poster=m_dict["Poster"],imdb_rating=m_dict["imdbRating"],imdb_votes=m_dict["imdbVotes"])
            session.add(movie)
            session.commit()
            return render_template("add_movie.html", title=title, director=director.name)


@app.route("/movie/description/<title>")
def movie_description(title):
    m_dict = getOMDb_data(title)
    try:
        title=m_dict["Title"]
        in_db = Movie.query.filter_by(title=title).first() #session.query(Movie).filter(Movie.title == title).first()#issue
        # print(in_db)
        return render_template("description.html", in_db=in_db, title=title, poster_image=m_dict["Poster"], director=m_dict["Director"], genre=m_dict["Genre"], plot=m_dict["Plot"])
    except:
        return render_template("description.html")


@app.route("/movie/suggestions/<title>") #Having issue. Getting rate exceeded error. Should I just give it more time? Should I offer a message for when this happens?
def movie_suggestions(title): #Having issues. Not getting info. Should I try again later or rethink this project?
    td_dict = getTD_data(title)

    try:
        original_movie = td_dict["Similar"]["Info"][0]["Name"]
        suggestions = td_dict["Similar"]["Results"]
        s_lis = []
        for m in suggestions:
            s_lis.append(m["Name"])

        if suggestions == []:
            error = "This movie is not in the system. Please try another movie title."
            return render_template("suggestions.html", error=error)
        else:
            return render_template("suggestions.html", original_movie=original_movie, s_lis=s_lis)
    except:
            error = "There is an issue with the system. Please try again later."
            return render_template("suggestions.html", error=error)


@app.route("/movie/graph")
def movie_graph():
    genres_dict = {}
    g_set_lis = session.query(genre_set).all()
    if g_set_lis:
        for g_tup in g_set_lis:
            g_id = g_tup[0]
            genre = Genre.query.filter_by(id=g_id).first().name
            if genre not in genres_dict:
                num = session.query(genre_set).join(Genre).join(Movie).filter(Genre.id == g_id).count()
                genres_dict[genre] = num

        url = make_graph_plotly(genres_dict)
        return render_template("graph.html", url=url)
    else:
        return render_template("graph.html")


@app.route("/movie/all")
def all_movies():
    all_movies = []
    movies = Movie.query.order_by(Movie.title).all()
    for m in movies:
        director = Director.query.filter_by(id=m.director_id).first()
        all_movies.append((m.title,m.year,director.name))
    return render_template("all_movies.html",all_movies=all_movies)


@app.route("/movie/delete/<title>")
def delete_movie(title):
    m_dict = getOMDb_data(title)
    title = m_dict["Title"]
    if Movie.query.filter_by(title=title).first():
        m = Movie.query.filter_by(title=title).first()
        Movie.query.filter_by(title=title).delete()
        genre_set.delete().where(genre_set.c.movie_id==m.id)
        actor_set.delete().where(actor_set.c.movie_id==m.id)
        session.commit()
        return render_template("delete.html",title=title)
    else:
        return render_template("delete.html")


if __name__ == "__main__":
    # db.create_all()
    app.run()
