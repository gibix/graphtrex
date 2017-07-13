# import networkx as nx
# import random as rnd
# import numpy as np
# import re
# import powerlaw as pwl
# 
# from sympy import *
# from lea   import *
# 
# np.seterr(divide='ignore', invalid='ignore')
# 
# G = nx.Graph()
# 
# 
# users = []
# 
# for idx, filename in enumerate(filenames):
# 
#     users.append(filename[5:-4])
# 
#     #Open f and ignore the first line
#     fh = open(filename, 'r')
#     fh.readline()
# 
#     for line in fh.readlines():
#         s = line.strip().split(',')
#         TimeLine = s[3]
#         PostId = s[5]
#         G.add_edge(PostId, TimeLine)
#         G.add_edge(users[idx], TimeLine)
# 
#     fh.close()
# 

from lib import *

filename = "fbtrex-French2017.csv"

G = posttlineuser(filename)

print "The graph has", len(G) , "nodes"
print "The graph has" ,len(G.edges()), "edges"

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

#TODO compare powerlaw to other ditributions

#fit_function.supported_distributions
#R,p = fit_function.
#fit_function.power_law.D
#print fit_function.power_law.D

#fit_function_fixmin.power_law.sigma
#print fit_function_fixmin.power_law.sigma
