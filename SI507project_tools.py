#__author__ == "Tasha Torchon (torchont)"
# SI 507 - Final Project
# -*- coding: utf-8 -*-


##### IMPORT STATEMENTS #####
import codecs
import sys
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer)
import requests, json, csv
from advanced_expiry_caching import Cache
import plotly
import plotly.plotly as py
import plotly.graph_objs as go


###### GLOBAL VARIABLES AND API ACCESS #####
plotly.tools.set_credentials_file(username="tftorchon", api_key="o9UplRPPVLe1Ce5K1m4l")
TD_KEY = "334310-SI507Fin-8A5Y4QHO"
OMDB_KEY = "81f97ae3"
FNAME = "SI507project_cache.json"
PROJECT_CACHE = Cache(FNAME)
CACHE_DICTION = PROJECT_CACHE.cache_diction


##### FUNCTIONS #####
def params_unique_combo(root_url, params_d, private_keys=["apikey"]):
    """This function creates a unique parameter dictionary, which will later be used to call APIs."""

    alphabetized_keys = sorted(params_d.keys())
    res = []
    for k in alphabetized_keys:
        if k not in private_keys:
            res.append("{}-{}".format(k, params_d[k]))
    return root_url + "_".join(res)

def getOMDb_data(movie_title):
    """Takes a movie title string that it uses to call the OMDb API. The function returns a dictionary. If the movie exists in the system, the dictionary will have information about the movie (e.g. release date, director, languages). Otherwise, it will return a dictionary with an 'Error' key. """

    b_url = "https://www.omdbapi.com/"
    p_dict = {}
    p_dict["apikey"] = OMDB_KEY
    p_dict["t"] = movie_title
    p_dict["type"] = "movie"

    omdb_id = params_unique_combo(b_url, p_dict)

    if omdb_id in CACHE_DICTION: #Does this account for cases when this has expired?
        return CACHE_DICTION[omdb_id]
    else:
        omdb_resp = requests.get(b_url, p_dict)
        CACHE_DICTION[omdb_id] = json.loads(omdb_resp.text)
        omdb_d_json = PROJECT_CACHE._save_to_disk()
        return CACHE_DICTION[omdb_id]

def getTD_data(movie_title): #TasteDive API seems to be limited to about a handful of queries at a time. Supposed to get 300 per hour but I get an exceeded limit error after only a handful of tries.
    """Takes a movie title string that it uses to call the Taste Dive API. The function returns a dictionary. If the movie exists in the system, the dictionary will have movie suggestions that are similar to the input variable. Otherwise, it will return a dictionary where the value of 'Results' is an empty list. """

    b_url = "https://www.tastedive.com/api/similar"
    p_dict = {}
    p_dict["apikey"] = TD_KEY
    p_dict["q"] = movie_title
    p_dict["type"] = "movies"

    td_id = params_unique_combo(b_url, p_dict)

    if td_id in CACHE_DICTION:
        return CACHE_DICTION[td_id]
    else:
        td_resp = requests.get(b_url, p_dict)
        CACHE_DICTION[td_id] = json.loads(td_resp.text)
        td_d_json = PROJECT_CACHE._save_to_disk()
        return CACHE_DICTION[td_id]

def percentage(part, whole):
    """ Takes two numbers (integers or floats). Part represents some amount and whole represents a larger portion of which it is part. This function returns a string up to two decimal points, e.g. '33.33%'. """

    p = part/whole*100
    p_round = round(p,2)
    p_str = str(p_round)+"%"
    return p_str

def make_graph_plotly(genre_dict):
    """ Takes a dictionary where the keys are strings of different genres and values are integers or floats that represent the number of times the genres are present. It uses the dictionary to create a plotly donut chart that represent genre percentages. The function returns a URL to access the chart. """

    genre_lis, g_count_lis = zip(*genre_dict.items())

    fig = {"data": [{"values": g_count_lis, "labels": genre_lis, "marker":{"line":{"color":"#000000", "width":2}}, "name": "Movies", "hoverinfo": "label+value+name", "hole": .4, "type": "pie"}],"layout": {"title":"The Genres of Your Favorite Movies"}}
    graph_url = py.plot(fig, filename='movies_donut', auto_open=False)
    return graph_url


##### FUNCtiON CALLS #####
if __name__ == "__main__":

    g_d = {"Comedy":50, "Action":17, "Horror":8, "Romance":35, "Drama":20}
    print(make_graph_plotly(g_d))
    td_dict = getTD_data("Lethal Weapon")
    movie_dict = getOMDb_data("titanic")
    print(movie_dict.keys())
    print(td_dict.keys())
    print(percentage(5.9835,10))
