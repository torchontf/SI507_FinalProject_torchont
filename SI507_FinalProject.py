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
@app.route('/')
def homepage():
    movies = Movie.query.all()
    # print(movies)
    num_movies = len(movies)
    return render_template("home.html", num_movies=num_movies)

@app.route('/movie/add/<title>') #Create template to add link to all_movies
def add_movie(title):
    m_dict = getOMDb_data(title)
    if m_dict["Response"] == "False":
        return "That movie doesn't exist. Check your spelling and try again."
    else:
        title = m_dict["Title"]
        if Movie.query.filter_by(title=title).first():
            return "That movie is already in the system! Go back to the main app!" #how to add main app link?
        else:
            year = int(m_dict["Year"]) #leave as integer? Would this ever not be a number value?
            mpaa = m_dict["Rated"]
            runtime = m_dict["Runtime"]
            genre_names = m_dict["Genre"].split(", ")
            g_lis = []
            for g in genre_names:
                genre = get_or_create_genre(g)
                g_lis.append(genre)#many to many?; string of multiple genres separated by commas
            dir_name = m_dict["Director"]
            director = get_or_create_director(dir_name) #is a many to many relationship in the API, but portrayed as a one to many here
            actor_names = m_dict["Actors"].split(", ")
            a_lis = []
            for a in actor_names:
                actor = get_or_create_actor(a)
                a_lis.append(actor) #many to many?; string of multiple genres
            plot = m_dict["Plot"]#long
            languages =  m_dict["Language"]#can be many but keep as one? no table for now; keep if have country?
            country = m_dict["Country"] #keep? no table for now
            poster = m_dict["Poster"]
            imdb_rating = m_dict["imdbRating"]
            imdb_votes = m_dict["imdbVotes"]

            movie = Movie(title=title,year=year,mpaa_rating=mpaa,duration=runtime,genre=g_lis,director_id=director.id,actor=a_lis,plot=plot,language=languages,country=country,poster=poster,imdb_rating=imdb_rating,imdb_votes=imdb_votes)
            session.add(movie)
            session.commit()
            return "New movie: {} by Director {} has been added.<br> Check out the URL for ALL MOVIES to see the whole list.".format(movie.title, director.name)

@app.route('/movie/description/<title>')
def movie_description(title):
    m_dict = getOMDb_data(title)
    try:
        title=m_dict["Title"]
        in_db = Movie.query.filter_by(title=title).first() #session.query(Movie).filter(Movie.title == title).first()#issue
        # print(in_db)
        return render_template("description.html", in_db=in_db, title=title, poster_image=m_dict["Poster"], director=m_dict["Director"], genre=m_dict["Genre"], plot=m_dict["Plot"])
    except:
        return render_template("description.html")

@app.route('/movie/suggestions/<title>') #Having issue. Getting rate exceeded error. Should I just give it more time? Should I offer a message for when this happens?
def movie_suggestions(title): #Having issues. Not getting info. Should I try again later or rethink this project?
    td_dict = getTD_data(title)
    try:
        original_movie = td_dict["Similar"]["Info"][0]["Name"]
        suggestions = td_dict["Similar"]["Results"]
        s_lis = []
        for m in suggestions:
            s_lis.append(m["Name"])
        return render_template("suggestions.html", original_movie=original_movie, s_lis=s_lis)
    except:
        if td_dict["error"]:
            error = "There is an issue with the system. Please try again later."
        else:
            error = "This movie is not in the system. Please try another movie title."
        return render_template("suggestions.html", error=error)

@app.route('/movie/graph')
def movie_graph():
    genres_dict = {}
    g_set_lis = session.query(genre_set).all()
    for g_tup in g_set_lis:
        g_id = g_tup[0]
        genre = Genre.query.filter_by(id=g_id).first().name
        if genre not in genres_dict:
            num = session.query(genre_set).join(Genre).join(Movie).filter(Genre.id == g_id).count()
            genres_dict[genre] = num

    url = make_graph_plotly(genres_dict)
    print(url)
    return render_template("graph.html", url=url)


@app.route('/movie/all')
def see_all_movies():
    all_movies = []
    movies = Movie.query.order_by(Movie.title).all()
    for m in movies:
        director = Director.query.filter_by(id=m.director_id).first()
        all_movies.append((m.title,director.name,m.genre))
    return render_template('all_movies.html',all_movies=all_movies)

# @app.route('/producer/all')
# def see_all_producers():
#     producers = Producer.query.all()
#     names = []
#     for p in producers:
#         num_movies = len(Movie.query.filter_by(producer_id=p.id).all())
#         newtuple = (p.name,num_movies)
#         names.append(newtuple)
#     return render_template('all_producers.html',producer_names=names)

# @app.route('/movie/delete/<title>/<producer>')
# def delete_movie(title, producer):
#     producer = get_or_create_producer(producer)
#     if Movie.query.filter_by(title=title, producer_id=producer.id).first():
#         movie_delete = Movie.query.filter_by(title=title, producer_id=producer.id).delete()
#         session.commit()
#         return "{} by {} has been deleted from the app.".format(title, producer.name)
#     else:
#         return "This movie is not in the app. Check out the URL for ALL MOVIES to see the list."


if __name__ == "__main__":
    # db.create_all()
    app.run()
