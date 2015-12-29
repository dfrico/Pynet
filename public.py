import networkx as nx
from twython import Twython as tw
from datetime import datetime
import time
import matplotlib.pyplot as plt

import os
import cPickle as pickle

print datetime.now()

G = nx.Graph()
G.clear()

APP_KEY = ''
APP_SECRET = ''
# PRIVATE
OAUTH_TOKEN = ''
OAUTH_TOKEN_SECRET = ''

twitter = tw(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
"""
json_data = twitter.get_followers_list(user_id='@pynet_')
for user in json_data["users"]:
    print user["name"]
print "\n"
"""
already = {''}
json_ids = twitter.get_followers_ids(user_id='pynet_')
for user in json_ids["ids"]:
    G.add_edge('@pynet_', twitter.show_user(user_id=user)["screen_name"])
    # time.sleep(60)
    G.add_node(twitter.show_user(user_id=user)["screen_name"])
    already.add(user)
    print twitter.show_user(user_id=user)["screen_name"]
    f_user1 = twitter.get_followers_ids(user_id=user)  # followers of user 1. Limit = 15 users, add delay (1query/min)
    for user_f in (set(f_user1["ids"]) & set(json_ids["ids"])):
        if user_f not in already:
            G.add_edge(twitter.show_user(user_id=user_f)["screen_name"], twitter.show_user(user_id=user)["screen_name"])
            print "\t" + twitter.show_user(user_id=user_f)["screen_name"]

print G.edges()
nx.draw_circular(G, with_labels=True, node_size=100)
plt.savefig("path.svg")

if not os.path.exists('newgraph.pickle'):
    os.system('touch newgraph.pickle')
with open('newgraph.pickle', 'w') as f:
    pickle.dump(G, f)
    print 'Pickled the graph'
