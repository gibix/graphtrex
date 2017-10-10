import networkx as nx
import random as rnd
import numpy as np
import re
import powerlaw as pwl
import pickle
#import ppickle

from sympy import *
from lea   import *

import matplotlib.pyplot as plt

##Attention this will req admin cred in MacOSX
##see below
import os

np.seterr(divide='ignore', invalid='ignore')

"""
  Define a graph from user to timeline to post
  Too much sparse
"""

def posttlineuser(filename):
    G = nx.Graph()

    #Open f and ignore the first line
    fh = open(filename, 'r')
    fh.readline()

    for line in fh.readlines():
        s = line.strip().split(',')
        User = s[3]
        TimeLine = s[5]
        PostId = s[7]
        G.add_edge(PostId, TimeLine)
        G.add_edge(User, TimeLine)

    fh.close()

    return G

"""
  User PostId Timeline
  Again too much sparse
"""

def userposttl(filename):
    G = nx.Graph()

    fh = open(filename, 'r')
    fh.readline()

    for line in fh.readlines():
        s = line.strip().split(',')
        User = s[3]
        PostId = s[7]
        TimeLine = s[5]
        G.add_edge(User, PostId)
        G.add_edge(PostId, TimeLine)
    
    fh.close()

    return G

"""
  Parses a file looking for each user
  Returns an array of files, each containing
  posts for each user and an array of dictionaries
  where for each timeline is present a dictionaire 
  mapping each source to the number of posts

  Even if a list of dictionaries is an esoteric
  data structure (ie shit) is preferred to a matrix 
  because we have a different number of sources in each
  timeline, in different order and we need only to map
  each univocally to the number of posts.
"""

def userparser(filename):

    fh = open(filename, 'r')
    fh.readline()

    users = set()
    timeline = ""
    sources = []
    postcount = {} 
    
    #Data is saved for in a csv file for
    #late retrievement, in this way we can
    #implement different user centered topologies

    for line in fh.readlines():
        
        s = line.strip().split(',')
        
        if s[3] in users:
            
            filename = s[3][1:-1] + ".csv"
            tmp = open(filename, 'a')
            tmp.write(line)
            tmp.close()
       
        else: 
            users.add(s[3])
            filename = s[3][1:-1] + ".csv"
            
            #Create an empty file user.csv
            #REQUIRES ADMIN CRED IN MACOSX
            os.mknod(filename)
            tmp = open(filename,'a')
            tmp.write(line)
            tmp.close()

        if timeline != s[5]:
            
            timeline = s[5]
            postcount = {}
            postcount[s[10]] = 1
            sources.append(postcount)

        else:

            #TODO condense in an inline statement
            if s[10] in sources[-1].keys():
                sources[-1][s[10]] += 1
            else:
                sources[-1][s[10]] = 1

    #Sources are normalized before being stored
    #to avoid repeating this operation at each
    #file instantiation

    sources = normalize(sources)

    #Write the timeline data in a pickle file
    #Assumes data.pkl is present

    output = open('data.pkl', 'wb')
    pickle.dump(sources, output)
    output.close()
        

    fh.close()

    return users, sources

"""
 For each user define a dynamical network representing its newsfeed
 
 The time parameter is considered the timeline, an edge is
 added between two posts if they are from the same source or
 are distance of DMAX, if both the weights are added.
 
 In the first case, the weight is given as a normalized fraction
 of the number of posts of each source present in a timeline.
 
 In the second, if the distance d is leq to DMAX the weight is
 e^(-d). Here DMAX is set to 3, consider that e^-4 ~=  0.01

 At each cycle, the adjacency matrix of the graph is damped by 
 a 'forgetting' factor that should be optimized to fit the data.
 Here we randomize it as one of the source values in part 1.


"""

def usernetwork(user,data_pkl='data.pkl', DMAX = 3):
   
    pkl_file = open(data_pkl, 'rb')
    timelines = pickle.load(pkl_file)

    G = nx.Graph()

    filename = user + '.csv'
    fh = open(filename, 'r')

    timelineid = 0
    timeline = ""

    pass
"""
Takes a list of dictionaries with numerical values
Return the list with the dictionary values normalized
(ie sum(dictionary.values) == 1)

Weights should add to 1 so that properly process
probabilities

"""
def normalize(sources):
    
   for timeline in sources:
       si = 1.0 / sum(timeline.itervalues())
       for k in timeline:
           timeline[k] *= si

   return sources


def posttouser(filename):
   
    G = nx.MultiGraph()

    fh = open(filename, 'r')
    fh.readline()

    for line in fh.readlines():
        s = line.strip().split(',')
        user = s[3]
        postid = s[7]
        G.add_edge(postid, user)


    fh.close()

    return G

def cleandeg(G, degmax):
    for n in G.nodes():
        if G.degree(n) == degmax:
            G.remove_node

def vizspringimage(G, filename):

    pos=nx.spring_layout(G)

    plt.figure( figsize = (80,60) )

    s=nx.draw_networkx_nodes(G,pos,node_size=0.1,node_color=nx.degree(G).values(),alpha=1,cmap=plt.cm.coolwarm )

    nx.draw_networkx_edges(G, pos, alpha=0.5)

    #show the colorbar on the right side
    cbar=plt.colorbar(s)
    cbar.ax.set_ylabel('Degree', size=22)

    plt.axis('off')

    save_to_file(filename, plt)

def save_to_file(filename, fig=None):
    formats = ["pdf","png"]
    if fig is None:
        for form in formats:
            plt.savefig("%s.%s"%(filename, form))
        else:
            for form in formats:
                fig.savefig("%s.%s"%(filename, form))
