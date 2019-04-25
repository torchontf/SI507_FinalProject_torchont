# SI507_FinalProject_torchont

Tasha Torchon

[Link to this repository](https://github.com/torchontf/SI507_FinalProject_torchont)
---
## Project Description
My project builds on Project 3 by saving movies to a database and displaying information about movies based on user input. The user is able to save their favorite movies to the database using it’s title. The remaining information about the film is collected and saved in the database using the OMDb API. Based on the route chosen, the user can also see a
description of a movie, get suggestions for similar films, or see a donut chart based on the genres of their favorite movies, among other things.

## How to run
1.  First, you should install all requirements with `pip install
-r requirements.txt`
2.  Second, you should run `movies_app.py runserver`
3.  Third, to access the different routes, you should type in the URLs as described in the ## How to use ## section.

## How to use
1.  After running the program, open a browser and enter <http://localhost:5000/> followed by the desired path, as defined below.
2.  <http://localhost:5000/> is described below under the `/(homepage)` route. ![Homepage](https://github.com/torchontf/SI507_FinalProject_torchont/blob/master/Photos/HomepageMoviesAdded.PNG)
3.  <http://localhost:5000/movie/add/&lt;title>> is described below under the `**/movie/add/&lt;title>/&lt;producer>/&lt;genre>` route. This movie requires adding a movie title in place of &lt;title\>. Examples of movie titles include, "Brick", "Captain Marvel", "When Harry Met Sally", "My Fair Lady", "A Serious Man", "You've Got Mail", "The Conjuring 2", "Taxi Driver", and "Pulp Fiction". A functioning url for adding "Guys and Dolls" is <http://localhost:5000/movie/add/guys%20and%20dolls>. ![Adding Guys and Dolls](https://github.com/torchontf/SI507_FinalProject_torchont/blob/master/Photos/AddMovie.PNG)
  NB: When typing in a URL, capitalization is not an issue. Spacing is not an issue and will automatically be replaced by %20 when the URL is loading. If there are multiple movies of the same name, the API will only return one. It's not clear how the API selects such films. For best results, it is best to enter movies as closely to the actual title as possible. "Conjuring" will return information about an 1896 short silent film. "The Conjuring" will return information about a 2013 horror film. "Youve Got Mail" (without an apostrophe) will return an error. Etc.
4.  <http://localhost:5000/movie/description/&lt;title>> is described below under the `/movie/description/&lt;title>` route. A functioning url for seeing information about "Black Orpheus" is  <http://localhost:5000/movie/description/black%20orpheus>. ![Black Orpheus Description Route](https://github.com/torchontf/SI507_FinalProject_torchont/blob/master/Photos/Description.JPG)
5.  <http://localhost:5000/movie/suggestions/&lt;title>> is described below under the `**/movie/suggestions/&lt;title>` route. A functioning url for seeing suggestions for the movie Sabrina (1954) is <http://localhost:5000/movie/suggestions/sabrina> ![Sabrina based on Sabrina](https://github.com/torchontf/SI507_FinalProject_torchont/blob/master/Photos/MovieSuggestions.PNG)
  NB: I am having some issues with the TasteDive API. Even though I should have a limit of 300 calls to the API per hour, I get messages stating that I have exceeded my limit after only a handful of calls. I have tried getting a new API but am faced with the same issue. I sent an e-mail to TasteDive about it. In the meantime, if this route only gives errors, use the `SI507project_cache.json` file included in this repository to see suggestions for "Lethal Weapon" <http://localhost:5000/movie/suggestions/lethal%20weapon>, "Phantom Thread" <http://localhost:5000/movie/suggestions/phantom%20thread>, or "Juno" <http://localhost:5000/movie/suggestions/juno>.
6.  <http://localhost:5000/movie/graph> is described below under the `**/movie/graph` route.
![Genres Graph](https://github.com/torchontf/SI507_FinalProject_torchont/blob/master/Photos/GraphWithMovies.PNG)
7.  <http://localhost:5000/movie/all> is described below under the `/movie/all` route.
![All Movies](https://github.com/torchontf/SI507_FinalProject_torchont/blob/master/Photos/AllMovies.PNG
)
8.  <http://localhost:5000/movie/delete/&lt;title>> is described below under the `/movie/delete/&lt;title>` route. A reasonable URL to access this route is <http://localhost:5000/movie/delete/adaptation>
![Adaptation Deleted](https://github.com/torchontf/SI507_FinalProject_torchont/blob/master/Photos/Delete.PNG)

## Routes in this application
-  `/home` -> this is the home page. It tells the user the number of movies in the app.
-  `/movie/add/&lt;title>` -> this route allows the user to add movies to the database through the URL using the movie's title. The rest of the movie's information(e.g. genre, director) will be filled in by an API request. A movie can only be entered into the database once. A link to the all movies route is included.
-  `/movie/description/&lt;title>` -> this route gives the movie title, poster, director(s), genre(s), and plot of this movie. It also tells the user whether the movie is already in the database.
-  `/movie/suggestions/&lt;title>` -> this route shows 20 suggestions based on the TasteDive API for a movie title input by the user.
-  `/movie/graph` -> this route shows a donut graph based on the genres of the user's favorite movies, which have been added to the database. A graph will not appear if no movies have been saved. To save movies to the database, use the <http://localhost:5000/movie/description/&lt;title>> URL.
-  `/movie/all` -> this route allows one to view all the movie titles currently in the database. A link to the homepage is included.
-  `/movie/delete/&lt;title>` -> this route allows one to delete a movie from the database based on the title of the movie. When called, this route will delete the movie from the movies table as well as the genre_set and actor_set association tables. A movie that isn't already in the database cannot be deleted. A link to all movies is included.

## How to run tests
1.  Run `movies_app.py.`
2.  Use the <http://localhost:5000/movie/add/&lt;title>> and <http://localhost:5000/movie/suggestions/&lt;title>> URLs at least once. The process to do so is described in 3. and 5. of the # How to use # section above. Feel free to try the other routes as well.
3. Run `SI507project_tests.py`

## In this repository:
-  torchontf/SI507_FinalProject_torchont
-  Photos folder (Contains photos included in README, photos of error messages, and photos of the sqlite database)
-  templates folder
-  README.md
-  SI507project_cache.json (Refer to 5. in # How to use section #)
-  SI507project_database_diagram.jpg
-  SI507project_tests.py
-  SI507project_tools.py
-  advanced_expiry_caching.py
-  finalproject_movies.db
-  movies_app.py
-  movies_db.py
-  movies_models.py
-  requirements.txt

---
## Code Requirements for Grading
Please check the requirements you have accomplished in your code as
demonstrated.
-  [x] This is a completed requirement.
-  [ ] This is an incomplete requirement.







Below is a list of the requirements listed in the rubric for you to copy
and paste.  See rubric on Canvas for more details.
### General
-  [x] Project is submitted as a Github repository
-  [x] Project includes a working Flask application that runs locally on a
computer
-  [x] Project includes at least 1 test suite file with reasonable tests
in it.
-  [x] Includes a `requirements.txt` file containing all required modules
to run program
-  [x] Includes a clear and readable README.md that follows this template
-  [x] Includes a sample .sqlite/.db file
-  [x] Includes a diagram of your database schema
-  [x] Includes EVERY file needed in order to run the project
-  [x] Includes screenshots and/or clear descriptions of what your project
should look like when it is working
### Flask Application
-  [x] Includes at least 3 different routes
-  [x] View/s a user can see when the application runs that are
understandable/legible for someone who has NOT taken this course
-  [x] Interactions with a database that has at least 2 tables
-  [x] At least 1 relationship between 2 tables in database
-  [x] Information stored in the database is viewed or interacted with in
some way
### Additional Components (at least 6 required)
-  [x] Use of a new module
-  [ ] Use of a second new module
-  [ ] Object definitions using inheritance (indicate if this counts for 2
or 3 of the six requirements in a parenthetical)
-  [x] A many-to-many relationship in your database structure
-  [ ] At least one form in your Flask application
-  [x] Templating in your Flask application
-  [ ] Inclusion of JavaScript files in the application
-  [x] Links in the views of Flask application page/s
-  [ ] Relevant use of `itertools` and/or `collections`
-  [ ] Sourcing of data using web scraping
-  [x] Sourcing of data using web REST API requests
-  [x] Sourcing of data using user input and/or a downloaded .csv or .json
dataset
-  [x] Caching of data you continually retrieve from the internet in some
way
### Submission
-  [x] I included a link to my GitHub repository with the correct
permissions on Canvas! (Did you though? Did you actually? Are you sure
you didn't forget?)
-  [x] I included a summary of my project and how I thought it went **in
my Canvas submission**!
