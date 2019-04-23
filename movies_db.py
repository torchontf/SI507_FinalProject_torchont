## __author__ == "torchont (Tasha Torchon)"
# SI 507 - Final Project
# Database

# Import statements
from flask_sqlalchemy import SQLAlchemy
# from movies_models import *

db = SQLAlchemy() # For database use
session = db.session # to make queries easy
