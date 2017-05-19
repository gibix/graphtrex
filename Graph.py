import csv
import sys

import networkx as nx

G = nx.DiGraph()

f = open(sys.argv[1], 'rt')
try:
    reader = csv.reader(f)
    for row in reader:
        G.add_edge(row[3], row[5])

    print G.edges()
        
finally:
    f.close()
