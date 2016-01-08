import networkx as nx
from twython import Twython as Tw
import twython
from datetime import datetime
from time import sleep
import os
from networkx.readwrite import json_graph
import json

print datetime.now()
G = nx.Graph()
G.clear()

APP_KEY = raw_input("Enter app key: ")
APP_SECRET = raw_input("Enter app secret key: ")
# PRIVATE
OAUTH_TOKEN = raw_input("Enter personal key: ")
OAUTH_TOKEN_SECRET = raw_input("Enter personal secret key: ")

twitter = Tw(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
main_user = raw_input("Enter your twitter @ username: ")

"""
main_user has FOLLOWERS1, where each USER and its USERNAME
has FOLLOWERS2, where each USER2 has a USERNAME2.
"""
try:
    already = {''}
    followers1 = twitter.get_followers_ids(user_id=main_user)
    print("\nUp and running! Please grab a coffee, this is going to take 1min per follower.\n")
    sleep(60)

    if not os.path.exists('graph.json'):
            os.system('touch graph.json')

    for user in followers1["ids"]:
        username = twitter.show_user(user_id=user)["screen_name"]
        # G.add_node(username)
        G.add_edge(main_user, username)
        # for i in tqdm(range(60)): TO-DO: INSERT PROGRESS BAR INSTEAD OF PRINTING THE USER NAMES.
        sleep(60)

        already.add(user)
        print username

        if not twitter.show_user(user_id=user)["protected"]:
            followers2 = twitter.get_followers_ids(user_id=user)

            G.node[username]['Size'] = len(followers2["ids"])

            for user2 in (set(followers2["ids"]) & set(followers1["ids"])):
                if user2 not in already:
                    username2 = twitter.show_user(user_id=user2)["screen_name"]
                    G.add_edge(username2, username)
                    print "\t" + username2

        nx.write_gexf(G, "graph.gexf")  # networkx export to gexf for Gephi.

        with open('graph.json', 'w') as f:
            f.write(json.dumps(json_graph.node_link_data(G)))   # json export to sigma JS

    print("\n END OF FILE \n")
except twython.exceptions.TwythonAuthError:
    print "\nError in the tokens."
except twython.exceptions.TwythonRateLimitError:
    print "\nRate limit exceeded: too much requests. Please wait 15 min and try again."
except twython.exceptions.TWITTER_HTTP_STATUS_CODE:
    print "\nError connecting. Check your internet connection."
