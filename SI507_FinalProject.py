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
    num_movies = len(movies)

    return render_template('home.html', num_movies=num_movies)

# @app.route('/movie/add/<title>/<producer>/<genre>/')
# def add_movie(title, producer, genre):
#     if Movie.query.filter_by(title=title).first():
#         return "That movie is already in the system! Go back to the main app!"
#     else:
#         producer = get_or_create_producer(producer)
#         movie = Movie(title=title,producer_id=producer.id,genre=genre)
#         session.add(movie)
#         session.commit()
#         return "New movie: {} by Director {} has been added.<br> Check out the URL for ALL MOVIES to see the whole list.".format(movie.title, producer.name)
#
# @app.route('/movie/all')
# def see_all_movies():
#     all_movies = []
#     movies = Movie.query.order_by(Movie.title).all()
#     for m in movies:
#         producer = Producer.query.filter_by(id=m.producer_id).first()
#         all_movies.append((m.title,producer.name,m.genre))
#     return render_template('all_movies.html',all_movies=all_movies)

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
