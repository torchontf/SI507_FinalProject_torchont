# SI507_FinalProject_torchont

Tasha Torchon

[Link to this repository](https://github.com/torchontf/SI507_FinalProject_torchont)
---
## Project Description
My project will build on Project 3 by saving and displaying information about
movies to a database based on user input. The user will be able to save their
favorite movies to the database using it’s title (and perhaps one other parameter).
The remaining information about the film will be collected and saved in the
database using the OMDb API. Based on the route chosen, the user can also see a
description regarding certain movies, get suggestions for similar films, or see
simple data regarding their favorite films (e.g. percentages of the different
genres included in the database).
## How to run
1.  First, you should install all requirements with `pip install
-r requirements.txt`
2.  Second, you should run `SI507_FinalProject.py runserver`
## How to use
1.  After running the program, open a browser and enter <http://localhost:5000/> followed by the desired path, as defined below.
2.  <http://localhost:5000/> is described below under the `/(homepage)` route.
3.  <http://localhost:5000/movie/add/&lt;title\>> is described below under the `**/movie/add/&lt;title>/&lt;producer>/&lt;genre>` route.
4.  <http://localhost:5000/movie/all> is described below under the `/movie/all` route.
5.  <http://localhost:5000/movie/delete/&lt;title\>> is described below under the `/movie/delete/&lt;title>` route.
6.  <http://localhost:5000/movie/description/&lt;title\>> is described below under the `/movie/description/&lt;title>` route.
7.  <http://localhost:5000/movie/suggestions/&lt;title\>> is described below under the `**/movie/suggestions/&lt;title>` route.
8.  <http://localhost:5000/movie/data> is described below under the `**/movie/data` route.
9.  Images to come: Markdown syntax to include an screenshot/image: ![alt
text](image.jpg)
## Routes in this application
-  `/home` -> this is the home page
-  `/movie/add/&lt;title>` -> this route allows the user to add movies to the database through the URL using the movie's title (e.g. http://localhost:5000/movie/add/Deadpool). The rest of the movie's information(e.g. genre, director) will be filled in by an API request.
-  `/movie/all` -> this route allows one to view all the movie titles currently in the database.
-  `/movie/delete/&lt;title>` -> this route allows one to delete a movie from the database based on the title of the movie.
-  `/movie/description/&lt;title>` -> this route shows a brief description (as given by the OMDb API) of a movie
specified input by the user.
-  `/movie/suggestions/&lt;title>` -> this route shows suggestions for a movie input by the user based on the TasteDive API.
-  `/movie/data` -> this route shows data (e.g percentages of movies by genre and a pie chart) based on the user’s favorite movies, as inputted into the database through the app.
## How to run tests
As of April 18, 2019:
1. Run `SI507project_tools.py`
2. Run `SI507project_tests.py`
NOTE: Need not have 3 steps, but should have as many as are appropriate!
## In this repository:
-  torchontf/SI507_FinalProject_torchont
-  README.md
-  SI507_FinalProject.py
-  SI507project_database_diagram.jpg
-  SI507project_tools.py
-  SI507project_tests.py
---
## Code Requirements for Grading
Please check the requirements you have accomplished in your code as
demonstrated.
-  [x] This is a completed requirement.
-  [ ] This is an incomplete requirement.







Below is a list of the requirements listed in the rubric for you to copy
and paste.  See rubric on Canvas for more details.
### General
-  [ ] Project is submitted as a Github repository
-  [ ] Project includes a working Flask application that runs locally on a
computer
-  [ ] Project includes at least 1 test suite file with reasonable tests
in it.
-  [ ] Includes a `requirements.txt` file containing all required modules
to run program
-  [ ] Includes a clear and readable README.md that follows this template
-  [ ] Includes a sample .sqlite/.db file
-  [ ] Includes a diagram of your database schema
-  [ ] Includes EVERY file needed in order to run the project
-  [ ] Includes screenshots and/or clear descriptions of what your project
should look like when it is working
### Flask Application
-  [ ] Includes at least 3 different routes
-  [ ] View/s a user can see when the application runs that are
understandable/legible for someone who has NOT taken this course
-  [ ] Interactions with a database that has at least 2 tables
-  [ ] At least 1 relationship between 2 tables in database
-  [ ] Information stored in the database is viewed or interacted with in
some way
### Additional Components (at least 6 required)
-  [ ] Use of a new module
-  [ ] Use of a second new module
-  [ ] Object definitions using inheritance (indicate if this counts for 2
or 3 of the six requirements in a parenthetical)
-  [ ] A many-to-many relationship in your database structure
-  [ ] At least one form in your Flask application
-  [ ] Templating in your Flask application
-  [ ] Inclusion of JavaScript files in the application
-  [ ] Links in the views of Flask application page/s
-  [ ] Relevant use of `itertools` and/or `collections`
-  [ ] Sourcing of data using web scraping
-  [ ] Sourcing of data using web REST API requests
-  [ ] Sourcing of data using user input and/or a downloaded .csv or .json
dataset
-  [ ] Caching of data you continually retrieve from the internet in some
way
### Submission
-  [ ] I included a link to my GitHub repository with the correct
permissions on Canvas! (Did you though? Did you actually? Are you sure
you didn't forget?)
-  [ ] I included a summary of my project and how I thought it went **in
my Canvas submission**!
