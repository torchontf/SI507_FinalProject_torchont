#__author__ == "Tasha Torchon (torchont)"
# SI 507 - Final Project

import unittest
from unittest import mock
from SI507project_tools import *

class Caching(unittest.TestCase):
    def test_cache(self):
        with open("SI507project_cache.json") as cache_f:
            self.assertTrue(cache_f is not None, "testing existence of json file")
            r = json.loads(cache_f.read())
            self.assertTrue(len(r.keys())>0,"testing that file has content")
            self.assertTrue("https://www.omdbapi.com" in r, "testing that file has content from OMDb API") # Failed. Am I testing wrong thing?
            self.assertTrue("https://www.tastedive.com/api" in r, "testing that file has content from TasteDive API")# Failed. Am I testing wrong thing?
            cache_f.close()

class DataRoute(unittest.TestCase):
    def test_percentage(self):
        t = percentage(4.9, 80)
        self.assertEqual(t, "6.13%", "testing output of percentage function")
    def test_graph(self):
        with open('data_pie.png', 'rb') as imgfile: #https://pythontips.com/2014/01/15/the-open-function-explained/#more-416
            # jpgdata = img.read()
            self.assertTrue(imgfile is not None, "testing existence of the graph")
            imgfile.close()

    @mock.patch("%s.my_module.plt" %__name__) # This test has an error. Trying to test whether function for creating graph works. How do I automate it?
    def test_make_graph(self):
        gl, gcl = ["comedy", "action", "horror"], [20, 35, 8]
        mock_plt = make_graph(gl, gcl)
        assert mock_plt.figure.called


# class Database(unittest.TestCase): #Complete later
#     def test_db(self):
#         pass

if __name__ == "__main__":
    unittest.main(verbosity=2)
