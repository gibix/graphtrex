# Roadmap for graphtrex analysis

This project is intended to provide an implementation of complex network dynamics analysis on the various datasets generously provided by the [tracking.exposed]( https://facebook.tracking.exposed) team.

In particular the first couple of months of research are intended to dive into experimental datasets like that harvested during the [2017 French elections](https://github.com/tracking-exposed/experiments-data).

Analytics on different projects promoted by the community will be added in the future, for this propose moduarity is considered in 1.

All our analysis are focused on giving an heuristic insight onto the dynamical variations of news feed and timeline, in order to give to the final user a better prospective on how s\he is affected by algorithmic filtering.

------

## 1. Code style and functionality

The code available in the networkx folder, was inteded as a first draft on which kind of data structures
and graph metrics would have been employed. The code has a sequential appearance, whereas instead 
functions and dats strcutures should be re-usable.

[] Divide the code in two modules : data structure initialization and network analysis

[] Add a IPython notebook for graph visualization

## 2. Data structures and visulization

[x] Add graph edges as  User -> PostID -> Timeline  

[] PostId -> PostId where an edge implies that two different  posts are present in two users' timeline.
   Timeline position is added as vertex property.

[] Other?
   
## 3. Network analysis

Please for an intro refer to [Strogatz, 2001 Exploring Complex Networks](http://www.math.cornell.edu/m/sites/default/files/imported/People/strogatz/exploring_complex_networks.pdf) and [Albert, Barabasi 2002 Statistical Mechanics of Complex Networks](https://arxiv.org/pdf/cond-mat/0106096.pdf)

[] Study global dynamics of the network : this should be accomplished in various ways for different parameters, such as clustering coefficient, average path length and scale factor.

[] Find critical nodes : after the previous point, we try to find the most critical points in the network.

[] Find (if it so) the time necessary for a connected graph to transit towards a union of highly clusterized subgraphs. This analyis, more than others, should be affected by the particular data structure that is implemented. 

For example connecteing each user to  a post and to a timeline will necessarly create some nodes that have a high connectivity degree, making of each user an hub in the network, portratiting necessarly to a scale-free dynamics. This will lead to a completely different clustering coefficient then, let's say, post -> post edges. 
Anyway having complementary data structures will certainly not pauper our research.


