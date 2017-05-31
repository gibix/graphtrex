import networkx as nx
import random as rnd
import numpy as np
import re
import powerlaw as pwl

from sympy import *
from lea   import *

#sometimes an error on numpy arrays will show up
#ignore it
np.seterr(divide='ignore', invalid='ignore')

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

degree = np.array(G.degree().values())
#for i in degree:
#    print i

##PARAMETER ESTIMATION###
#The lib powerlaw allows to estimate the exponent alpha
# and the minimum value fro the scaling of x_min

fit_function = pwl.Fit(degree)
fit_function
fit_function.power_law

fit_function.power_law.alpha
print fit_function.power_law.alpha

fit_function.power_law.sigma
print fit_function.power_law.sigma

#The vaue of xmin can be fixed
#this values should be changed 

fit_function.power_law.xmin
print fit_function.power_law.xmin

fit_function_fixmin = pwl.Fit(degree, xmin=1)
fit_function_fixmin.xmin
print fit_function_fixmin.xmin

fit_function_fixmin.power_law.sigma
print fit_function_fixmin.power_law.sigma

#We look at the values of teh Kolmogorov-Smirnov
#distance of the two fits to compare them

fit_function.supported_distributions
R,p = fit_function.
fit_function.power_law.D
print fit_function.power_law.D

fit_function_fixmin.power_law.sigma
print fit_function_fixmin.power_law.sigma

