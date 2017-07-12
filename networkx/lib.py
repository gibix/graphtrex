import networkx as nx
import random as rnd
import numpy as np
import re
import powerlaw as pwl

from sympy import *
from lea   import *

np.seterr(divide='ignore', invalid='ignore')

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
