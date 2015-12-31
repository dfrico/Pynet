import networkx as nx
from twython import Twython as tw
from datetime import datetime
from time import sleep

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
sleep(60)
followers1 = twitter.get_followers_ids(user_id='blayhem')
for user in followers1["ids"]:
    username = twitter.show_user(user_id=user)["screen_name"]
    G.add_node(username)
    G.add_edge('@blayhem', username)
    # for i in tqdm(range(60)):
    sleep(60)

    already.add(user)

    print username

    followers2 = twitter.get_followers_ids(user_id=user)
    G.node[username]['weight'] = len(followers2)

    for follower in (set(followers2["ids"]) & set(followers1["ids"])):
        if follower not in already:
            G.add_edge(twitter.show_user(user_id=follower)["screen_name"], username)
            print "\t" + twitter.show_user(user_id=follower)["screen_name"]

nx.write_gexf(G, "graph.gexf")
