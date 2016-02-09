# Pynet
## A python module for Twitter data visualization.

##### Update:
You **need** to create an ```init.py``` file with the following structure:
```
from pynet import Pynet as py
APP_KEY =             [list of (your) token(s) for the APP_KEY]
APP_SECRET =          [list of (your) token(s) for the APP_SECRET]
# PRIVATE
OAUTH_TOKEN =         [list of (your) token(s) for the OAUTH_TOKEN]
OAUTH_TOKEN_SECRET =  [list of (your) token(s) for the OAUTH_TOKEN_SECRET]
pynet = py()
pynet.pynet(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
```

==================================================

Pynet is a project still in progress. It allows you to visualize your twitter connections, people who follow you and follow each other, as a graph.
1. Type
```
git clone https://github.com/blayhem/pynet pynet
```
2. You have to create a [Twitter App](http://apps.twitter.com/) for your user.
Give it a name, a description, and go to the tokens tab to obtain your user tokens.

3. With the four tokens at hand, follow the steps in the update (creating the ```init.py``` file) and run it as
```
python init.py
```


At the end, you'll get a .gexf file, which you have to open with [Gephi](https://gephi.org).
There, rearrange the nodes with some graph-drawing algorithms, such as the Fruchterman-Reingold algorithm, and color the graph as preferred.

##### Here's the [link](http://blayhem.github.io/blog/post/Visualizing%20Data%20with%20Pynet/) to my blog, where I explain the process of creating Pynet.

###### Disclaimer: it's still in beta. Although it works.
