import networkx as nx
import random as rnd
import numpy as np
import re

from sympy import *
from lea   import *

G = nx.Graph()

filename1 = "feed-100014305273231.csv"

user1 = filename1[5:-4]

fh = open(filename1,'r')

fh.readline()

for line in fh.readlines():
     s = line.strip().split(',')
     TimeLine = s[3]
     PostId = s[5]
     G.add_edge(PostId, TimeLine)
     G.add_edge(user1, TimeLine)
    
fh.close()

filename2 = "feed-100016786692466.csv"

user2 = filename2[5:-4]

fh = open(filename2,'r')

fh.readline()

for line in fh.readlines():
     s = line.strip().split(',')
     TimeLine = s[3]
     PostId = s[5]
     G.add_edge(PostId, TimeLine)
     G.add_edge(user2, TimeLine)
    
fh.close()

filename3 = "feed-100016788883580.csv"

user3 = filename3[5:-4]

fh = open(filename3,'r')

fh.readline()

for line in fh.readlines():
     s = line.strip().split(',')
     TimeLine = s[3]
     PostId = s[5]
     G.add_edge(PostId, TimeLine)
     G.add_edge(user3, TimeLine)
    
fh.close()

filename4 = "feed-100016926932367.csv"

user4 = filename4[5:-4]

fh = open(filename4,'r')

fh.readline()

for line in fh.readlines():
     s = line.strip().split(',')
     TimeLine = s[3]
     PostId = s[5]
     G.add_edge(PostId, TimeLine)
     G.add_edge(user4, TimeLine)
    
fh.close()


print len(G), len(G.edges())

