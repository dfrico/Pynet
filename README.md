# Pynet
## A python module for Twitter data visualization.

Pynet is a project still in progress. It allows you to visualize your twitter connections, people who follow you and follow each other, as a graph.
To run it, type
```
git clone https://github.com/blayhem/pynet pynet
```
First, you have to create a [Twitter App](http://apps.twitter.com/) for your user.
Give it a name, a description, and go to the tokens tab to obtain your user tokens.
With the four tokens at hand, run the script as follows:
```
python pynet.py
```
Copy the tokens as asked, and then follow the instructions.

At the end, you'll get a .gexf file, which you have to open with [Gephi](https://gephi.org).
There, rearrange the nodes with some graph-drawing algorithms, such as the Fruchterman-Reingold algorithm, and color the graph as preferred.

##### Here's the [link](http://blayhem.github.io/post/Visualizing%20Data%20with%20Pynet/) to my blog, where I explain the process of creating Pynet.

###### Disclaimer: it's still very in beta. Although it works.
###### Disclaimer 2: if you have a lot of followers, be patient. It takes a lot of time.
