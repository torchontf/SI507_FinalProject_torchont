#__author__ == "Tasha Torchon (torchont)"
# SI 507 - Final Project

import unittest
import sqlite3
from SI507project_tools import *

class API_Functions(unittest.TestCase):
    def test_getOMDb_data(self):
        self.assertTrue(getOMDb_data("Phantom Thread"),"Testing that getOMDb_data runs")
        self.assertIsInstance(getOMDb_data("Phantom Thread"),dict,"Testing that getOMDb_data returns a Python object of type dictionary")
    def test_getTD_data(self):
        self.assertTrue(getTD_data("Adaptation"),"Testing that getTD_data runs")
        self.assertIsInstance(getTD_data("Adaptation"),dict,"Testing that getTD_data returns a Python object of type dictionary")

class Caching(unittest.TestCase):
    def test_cache(self):
        with open("SI507project_cache.json") as cache_f:
            self.assertTrue(cache_f is not None, "Testing existence of json file")
            r = json.loads(cache_f.read())
            self.assertTrue(len(r.keys())>0,"Testing that file has content")
            cache_f.close()
        movie_str = str(CACHE_DICTION.keys())
        self.assertIn("https://www.omdbapi.com/",movie_str,"Testing that CACHE_DICTION has content from OMDb API")# Failed. Am I testing wrong thing?
        self.assertIn("https://www.tastedive.com/api",movie_str ,"Testing that CACHE_DICTION has content from TasteDive API")

class Database(unittest.TestCase):
    def setUp(self):
        self.conn = sqlite3.connect("finalproject_movies.db") # Connecting to database that should exist in autograder
        self.cur = self.conn.cursor()
    def test_for_movies_table(self):
        res = self.cur.execute("select * from movies")
        data = res.fetchall()
        self.assertTrue(data, "Testing that you get a result from making a query to the movies table")
    def test_foreign_key_movie(self):
        res = self.cur.execute("select * from movies INNER JOIN directors ON movies.director_id = directors.id")
        data = res.fetchall()
        self.assertTrue(data, "Testing that result of selecting based on relationship between movies and directors does work")
    def tearDown(self):
        self.conn.commit()
        self.conn.close()

if __name__ == "__main__":
    unittest.main(verbosity=2)
