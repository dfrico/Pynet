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
json_data = twitter.get_followers_list(user_id='@main_user')
for user in json_data["users"]:
    print user["name"]
print "\n"
"""

json_ids = twitter.get_followers_ids(user_id='@main_user') # 1 request
for user in json_ids["ids"]:
    print user
    print type(json_ids["ids"])
    f_user1 = twitter.get_followers_ids(user_id=user) # followers of user 1. RATE LIMIT EXCEEDED. limit = 15
    common_set = set(f_user1["ids"]) & set(json_ids["ids"])
    for user in common_set:
        print "\t"
        print user




# edge if (user 2 is in) followers_main & followers_user1
