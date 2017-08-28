import networkx as nx
import random as rnd
import numpy as np
import re
import powerlaw as pwl

from sympy import *
from lea   import *

##Attention this will req admin cred in MacOSX
##see below
import os

np.seterr(divide='ignore', invalid='ignore')

##Define a graph from user to timeline to post
##Too much sparse

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

##User PostId Timeline
##Again too much sparse

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


##Parses a file looking for each user
##Returns an array of files, each containing
##posts for each user

def userparser(filename):

    fh = open(filename, 'r')
    fh.readline()

    users = set()
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
        

    fh.close()

    return users

##For each user define a graph with all its posts
##An edge is added between two posts if the post are
##from the same source or if they are on the same timeline
#If preconfig

def user(filename):
    ##TODO
    pass
