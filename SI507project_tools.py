#__author__ == "Tasha Torchon (torchont)"
# SI 507 - Final Project
# -*- coding: utf-8 -*-

import codecs
import sys
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer)
import requests, json, csv
from advanced_expiry_caching import Cache
import plotly
import plotly.plotly as py
import plotly.graph_objs as go
# import plotly.tools as tls
# import matplotlib.pyplot as plt
# import numpy as np

plotly.tools.set_credentials_file(username="tftorchon", api_key="o9UplRPPVLe1Ce5K1m4l")
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
    # p_dict["info"] = 1 # not sure whether to include extra info: teaser, wiki article, youtube video

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

# def make_graph(genre_lis, g_count_lis): #to be edited. will need to figure out how to get these values from sqlite. Will I need to iterate in the function or is it automated?
#     cmap=plt.cm.get_cmap("spring")
#     labels = genre_lis
#     sizes = g_count_lis
#     plt.pie(sizes, labels=labels, autopct="%1.1f%%")
#     plt.axis("equal")
#     plt.savefig("data_pie.png")

def make_graph_plotly(genre_lis, g_count_lis):
    fig = {"data": [{"values": g_count_lis, "labels": genre_lis, "marker":{"line":{"color":"#000000", "width":2}}, "name": "Movies", "hoverinfo": "label+percent+name", "hole": .4, "type": "pie"}],"layout": {"title":"The Genres of Your Favorite Movies"}}
    py.plot(fig, filename='donut')
# https://matplotlib.org/gallery/pie_and_polar_charts/pie_and_donut_labels.html#sphx-glr-gallery-pie-and-polar-charts-pie-and-donut-labels-py



if __name__ == "__main__":
    gl = ["Comedy", "Action", "Horror", "Romance", "Drama"]
    gcl = [20, 35, 8, 2, 50]

    getTD_data("A Serious Man")
    #attempt mpl to plotly
    # mpl_fig = plt.pie(gcl, labels=gl, autopct="%1.1f%%")
    # cmap=plt.cm.get_cmap("spring")

    # make_graph(gl, gcl)
    # fig = {"data":[{"values": gl, "labels": gcl, "domain": {"column": 0}, "name": "Movie Genre", "hoverinfo": "label+percent+name", "hole": .4, "type": "pie"}], "layout": {"title":"The Genres of Your Favorite Movies", "grid": {"rows": 1, "columns": 2}, "annotations": [{"font": {"size": 20}, "showarrow": False, "text": "Genres", "x": 0.5, "y": 0.5}]}}

    # trace = go.Pie(labels=gl, values=gcl)
    # data = go.Data([trace])
    # layout = go.Layout(title="The Genres of Your Favorite Movies")
    # fig = go.Figure(data=trace, layout=layout)
    # py.plot([trace], filename="plotly_pie_chart")
    # py.plot(fig, filename="genre_donut")
    # colors = cmap=plt.cm.get_cmap("spring")
    # trace1 = go.Pie(labels=gl, values=gcl, marker=dict(line=dict(color='#000000', width=2)), name='Movies', hoverinfo = "label+percent+name", hole = .4)
    # "text":["CO2"],
    #       "textposition":"inside",
    #       "domain": {"column": 1},
    #       "name": "CO2 Emissions",
    #       "hoverinfo":"label+percent+name",
    #       "hole": .4,
    #       "type": "pie"
    #textinfo ="value", textfont=dict(size=20),

    # data=go.Data([trace1])
    # # layout=go.Layout(title="The Genres of Your Favorite Movies")#, xaxis={'title':'x1'}, yaxis={'title':'x2'})
    # figure=go.Figure(data=data,layout=layout)
    # # figure.layout.colorway=("spring")
    # py.plot(figure, filename='pyguide_1')



#Attempt without .data()
#     make_graph(gl, gcl)
#     movie = getOMDb_data("titanic")
#     suggestions = getTD_data("Sabrina")
#     print(percentage(5.98,10))
#
# # exploring cache structure
#     with open(PROJECT_CACHE.filename, 'r', encoding='utf-8') as cache_file:
#         cache_json = cache_file.read()
#         CACHE_DICTION = json.loads(cache_json)
#
#     print(CACHE_DICTION.keys())
