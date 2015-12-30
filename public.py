import networkx as nx
from twython import Twython as tw
from datetime import datetime
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

already = {''}
i=0
followers1 = twitter.get_followers_ids(user_id='pynet_')
for user in followers1["ids"]:
    username = twitter.show_user(user_id=user)["screen_name"]
    G.add_node(username)
    G.add_edge('@pynet_', username)
    # time.sleep(60)
    already.add(user)
    """
    mapping = {i: user}
    i += 1
    G = nx.relabel_nodes(G, mapping)
    """
    print username

    followers2 = twitter.get_followers_ids(user_id=user)
    G.node[username]['weight'] = len(followers2)

    for follower in (set(followers2["ids"]) & set(followers1["ids"])):
        if follower not in already:
            G.add_edge(twitter.show_user(user_id=follower)["screen_name"], username)
            print "\t" + twitter.show_user(user_id=follower)["screen_name"]


# nx.draw_circular(G, with_labels=True, node_size=20, node_color='black')
# plt.savefig("path.svg")
nx.write_gexf(G, "graph.gexf")
"""
if not os.path.exists('newgraph.pickle'):
    os.system('touch newgraph.pickle')
with open('newgraph.pickle', 'w') as f:
    pickle.dump(G, f)
    print 'Pickled the graph'
"""


# edge if (user 2 is in) followers_main & followers_user1

"""
# twitter = tw(APP_KEY, APP_SECRET)
# enter authentication tokens by hand, not by this
# auth = twitter.get_authentication_tokens(callback_url='http://mysite.com/callback')
# twitter.update_status(status='Testing twython & netpy...')

# followers = twitter.get_followers_list(user_id='blayhem')
# json_data = json.loads(twitter.get_followers_list(user_id='blayhem'))
with open('../../follow.json') as f:
    json_data = json.load(f)
    # users = [x["name"] for x in json_data["name"]]
    # for user in users: print user.name
    # for user in json_data: print user
    for user in json_data["users"]:
        print user["name"]


"""
