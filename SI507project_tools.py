#__author__ == "Tasha Torchon (torchont)"
# SI 507 - Final Project
# -*- coding: utf-8 -*-

import codecs
import sys
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer)
import requests, json, csv
# import plotly.plotly as py
# import plotly.graph_objs as go
import matplotlib.pyplot as plt
from advanced_expiry_caching import Cache

TD_KEY = "334310-SI507Fin-F9CCSCRU"
OMDB_KEY = "81f97ae3"
FNAME = "SI507project_cache.json"
PROJECT_CACHE = Cache(FNAME)
CACHE_DICTION = PROJECT_CACHE.cache_diction

def params_unique_combo(root_url, params_d, private_keys=["apikey"]):
    """This function creates a unique parameter dictionary, which will later be used to call APIs."""

    alphabetized_keys = sorted(params_d.keys())
    res = []
    for k in alphabetized_keys:
        if k not in private_keys:
            res.append("{}-{}".format(k, params_d[k]))
    return root_url + "_".join(res)

def getOMDb_data(movie_title):
    b_url = "https://www.omdbapi.com/"
    p_dict = {}
    p_dict["apikey"] = OMDB_KEY
    p_dict["t"] = movie_title

    omdb_id = params_unique_combo(b_url, p_dict)

    if omdb_id in CACHE_DICTION: #Does this account for cases when this has expired?
        return CACHE_DICTION[omdb_id]
    else:
        omdb_resp = requests.get(b_url, p_dict)
        CACHE_DICTION[omdb_id] = json.loads(omdb_resp.text)
        omdb_d_json = PROJECT_CACHE._save_to_disk()
        return CACHE_DICTION[omdb_id]

def getTD_data(movie_title):
    b_url = "https://www.tastedive.com/api/similar"
    p_dict = {}
    p_dict["apikey"] = TD_KEY
    p_dict["q"] = movie_title
    p_dict["type"] = "movies"

    td_id = params_unique_combo(b_url, p_dict)

    if td_id in CACHE_DICTION: #Does this account for cases when this has expired?
        return CACHE_DICTION[td_id]
    else:
        td_resp = requests.get(b_url, p_dict)
        CACHE_DICTION[td_id] = json.loads(td_resp.text)
        td_d_json = PROJECT_CACHE._save_to_disk()
        return CACHE_DICTION[td_id]

def percentage(part, whole): #based on structure of matplotlib, I may not need this. I will keep just in case graphing is too complicated in the app.
    p = part/whole*100
    p_round = round(p,2)
    p_str = str(p_round)+"%"
    return p_str

def make_graph(genre_lis, g_count_lis): #to be edited. will need to figure out how to get these values from sqlite. Will I need to iterate in the function or is it automated?
    labels = genre_lis
    sizes = g_count_lis
    plt.pie(sizes, labels=labels, autopct="%1.1f%%")
    plt.axis("equal")
    plt.savefig("data_pie.png")
# https://matplotlib.org/gallery/pie_and_polar_charts/pie_and_donut_labels.html#sphx-glr-gallery-pie-and-polar-charts-pie-and-donut-labels-py

if __name__ == "__main__":
    gl = ["comedy", "action", "horror"]
    gcl = [20, 35, 8]

    make_graph(gl, gcl)
    movie = getOMDb_data("titanic")
    suggestions = getTD_data("Sabrina")
    print(percentage(5.98,10))

# exploring cache structure
    with open(PROJECT_CACHE.filename, 'r', encoding='utf-8') as cache_file:
        cache_json = cache_file.read()
        CACHE_DICTION = json.loads(cache_json)

    print(CACHE_DICTION.keys())
