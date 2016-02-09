# coding=utf-8
import networkx as nx
import twython
from time import sleep
import os
# JSON imports
from networkx.readwrite import json_graph
import json                         # TO-DO: review imports


class Pynet(object):
    def pynet(self, APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET):
        try:
            G = nx.Graph()
            main_user = raw_input("Enter your twitter @ username: ")
            # main_user = 'pynet_'
            rate = 0
            i = 1

            twitter = twython.Twython(APP_KEY[i], APP_SECRET[i], OAUTH_TOKEN[i], OAUTH_TOKEN_SECRET[i])
            already = {''}
            musn = twitter.show_user(screen_name=main_user)["id"]  # Main User Screen Name to get ID
            followers1 = twitter.get_followers_ids(user_id=musn)
            time = twitter.show_user(screen_name=main_user)["followers_count"]  # Estimated time in min (= number of followers)

            if time/len(APP_KEY) == 1:
                print("\nUp and running! Please grab a coffee, this is going to take "+str(time/len(APP_KEY)) +
                      " minute ¯\_(ツ)_/¯\n")
            else:
                print("\nUp and running! Please grab a coffee, this is going to take "+str(time/len(APP_KEY)) +
                      " minutes ¯\_(ツ)_/¯\n")

            sleep(60/(len(APP_KEY)))

            if not os.path.exists('graph.json'):
                os.system('touch graph.json')

            for user in followers1["ids"]:

                """
                main_user has FOLLOWERS1, where each USER and its USERNAME
                has FOLLOWERS2, where each USER2 has a USERNAME2.
                """

                username = twitter.show_user(user_id=user)["screen_name"]
                G.add_edge(main_user, username)
                # for i in tqdm(range(60)): TO-DO: INSERT PROGRESS BAR INSTEAD OF PRINTING THE USER NAMES.
                sleep(60/(len(APP_KEY)))

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

                rate += 1

                if rate == 14:
                    if i < len(APP_KEY):
                        i += 1
                    else:
                        i = 0
                    twitter = twython.Twython(APP_KEY[i], APP_SECRET[i], OAUTH_TOKEN[i], OAUTH_TOKEN_SECRET[i])
                    rate = 0
            print("\n END OF FILE. Check .gexf file.\n")

        except twython.exceptions.TwythonAuthError:
            print "\nError in the tokens."
        except twython.exceptions.TwythonRateLimitError:
            print "\nRate limit exceeded: too much requests. Please wait 15 min and try again."
        except twython.exceptions.TWITTER_HTTP_STATUS_CODE:
            print "\nError connecting. Check your internet connection."
        except twython.exceptions.TwythonError:
            print("\nGeneric error ¯\_(ಥ_ಥ)_/¯")
        except KeyboardInterrupt:
            print "\nService manually stopped."



"""
if not os.path.exists('newgraph.pickle'):
    os.system('touch newgraph.pickle')
with open('newgraph.pickle', 'w') as f:
    pickle.dump(G, f)
    print 'Pickled the graph'

# twitter = Tw(APP_KEY, APP_SECRET)
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