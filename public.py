import networkx as nx
from twython import Twython as tw

G = nx.Graph()

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
json_ids = twitter.get_followers_ids(user_id='@pynet_')
for user in json_ids["ids"]:
    print twitter.show_user(user_id=user)["screen_name"]
    f_user1 = twitter.get_followers_ids(user_id=user)  # followers of user 1. Limit = 15 users, add delay (1query/min)
    common_set = set(f_user1["ids"]) & set(json_ids["ids"])
    for user in common_set:
        if user not in already:
            print "\t" + twitter.show_user(user_id=user)["screen_name"]
            already.add(user)

# to-do: avoid bidirectional edges (mutual follow)? Design decision. Check NX.
