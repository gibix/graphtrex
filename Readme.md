# Roadmap for graphtrex analysis

This project is intended to provide an implementation of complex network dynamics analysis on the various datasets generously provided by the [tracking.exposed]( https://facebook.tracking.exposed) team.

In particular the first couple of months of research are intended to dive into experimental datasets like that harvested during the [2017 French elections](https://github.com/tracking-exposed/experiments-data).

Analytics on different projects promoted by the community will be added in the future, for this propose modularity is considered in 1.

All our analysis are focused on giving an heuristic insight onto the dynamical variations of news feed and timeline, in order to give to the final user a better prospective on how s\he is affected by algorithmic filtering.

------

## 1. Code style and functionality

The code available in the networkx folder, was inteded as a first draft on which kind of data structures
and graph metrics would have been employed. The code has a sequential appearance, whereas instead
functions and dats structures should be re-usable.

- [ ] Divide the code in two modules : data structure initialization and network analysis

- [ ] Add a IPython notebook for graph visualization

## 2. Data structures and visualization

- [x] Add graph edges as *User -> PostID -> Timeline*

- [ ] *PostId -> PostId* where an edge implies that two different posts are present in two users' timeline.
   Timeline position is added as vertex property.

- [ ] A graph can be structured in different ways: i.e. using posts or users as vertices. Find a way of make a dynamical (in time) graph based non user activity.    

- [ ] Other?

## 3. Network analysis

Please for an intro refer to [Strogatz, 2001 Exploring Complex Networks](http://www.math.cornell.edu/m/sites/default/files/imported/People/strogatz/exploring_complex_networks.pdf) and [Albert, Barabasi 2002 Statistical Mechanics of Complex Networks](https://arxiv.org/pdf/cond-mat/0106096.pdf) as well as [Barrat, Vespignani - Dynamical Processes on Complex Networks]

- [ ] Study global dynamics of the network : this should be accomplished in various ways for different parameters, such as clustering coefficient, average path length and scale factor.

- [ ] Find critical nodes : after the previous point, we try to find the most critical points in the network.

- [ ] Find (if it so) the time necessary for a connected graph to transit towards a union of highly clusterized subgraphs. This analyis, more than others, should be affected by the particular data structure that is implemented.
For example connecting each user to a post and to a timeline will necessarly create some nodes that have a high connectivity degree, making of each user an hub in the network, portratiting necessarly to a scale-free dynamics. This will lead to a completely different clustering coefficient then, let's say, post -> post edges. 
Anyway having complementary data structures will certainly not pauper our research.

Up to this point, putting our best efforts, the analysis could be completed for the end of 2017.
Of course we did not saturate the whole body of research in social network analysis.
The analysis in 4. are mainly intended for a dataset more complex than that of the french elections.


## 4. Future directions

A detailed mathematical grounding for the topics presented below is out of scope for this document.
Please refer to [Cultural dissemination in a complex network](http://www.sciencedirect.com/science/article/pii/S037843710800962X), [A matrix iteration for dynamic network
summaries](http://centaur.reading.ac.uk/28768/1/dynsumresub.pdf), [Bistability Through Triadic Closure](https://core.ac.uk/download/pdf/1442966.pdf), [Complex Dynamics in a Model
of Social Norm](https://www.reading.ac.uk/web/files/maths/Preprint_12_21_Parsons.pdf)

### Fully coupled systems

There is a large literature in psycology that is based on individuals' attitudes and behaviors being in a tensioned equilibrium between excitatory and inhibiting processes.
Typically the state of an individual is represented by a set of state variables, some measuring atcivating elements ans some measuring the inhibitng elements.

Activator-inhibitor systems have had an impact whitin mathematical models where an uniformity equilibrium across a population of individual systems become destabilized by the very act of passive coupling between them. Such Turing instabilities can sometimes seem counterproductive.
Homophily is a term that describes how associations are more likely to occur between people who have similar attitudes and beliefs. The main goal is to show how individuals' activating-inhibitor dynamics coupled through a homophilic evolving network produce systems that have pesudoperiodic consensus and fractionation.

This would a very exciting topic to dive into : there are numerous commentators in socioeconomic fields who assert that divergent attitudes, beliefs and social norms require leaders and are imposed on populations, or else are driven by partial experience and eventes.
But here we can see that transient existence of locally clustered subgroups, holding different views, can be an emergent behavior within coupled systems.

### Epidemic dynamics

Especially for critical vertices, it could be interesting to try to fit the spread of a post in different users' timeline using epidemic-like models, this could be accomplished solving the differential equations of the deterministic SIR model and simulating a discrete and stochastic SIR model by randomly extracting the transition elements at each step. Dependence for initial conditions should be highly considered.

For an interesting body of research on how to nicely visualize epidemic diffusion network by temporal dynamcis look at [2001, Liljeros](www.nature.com/nature/journal/v411/n6840/full/411907a0.html) which found that the network of human sexual contacts is scale-free and [2011, Rocha](http://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1001109) which published a temporal datasets of sexual contacts in Brazil.

### Evolving networks in continuos and discrete time

Consider each user connected through a dynamically undirected network representing a post in common or some other kind of interaction that is considered valid for an edge between the two nodes.

*A(t)* would be the *NxN* adjacency matrix, where for *t!=0* *A(t)* is a stochastic objected befined by probability distribution of a set of all possible asjacency matrices.

Assuming that each edge could evolve independently over time, though it is conditionally dependent upon the current network, we could consider that the probability that from an adjacency matrix *A(t)* we could obtain *A(dt +t)* is enough to specify its expected value.

The evolution model is given by a Markow first order model where we consider edge birth and mortality porbabilities. Anyway considering the communicability matrix which provides a weighted count of all possible dynamic paths between all pairs of vertices. Its row sum represnt the ability of an user to send messages to other, while column sum represent teh ability of corresponding people to receive messages from others.

### Text Mining and Natural Language Processing (NLP)

- [ ] Use "naive" encoding like one-hot encoding or bag-of-words to model frequency of words and construct useful infographics such as word clouds.
- [ ] Create a (or exploit an already existing) neural network to deduce syntactic components. This goal can be achieved in various ways, some useful components to practice and compare are: word embedding, hebbian learning, PCA, and recurrent networks. Once the subject is pinpointed, it can be used as a more sophisticaed way of categorizing a certain post, hopefully less naive than word clouds. It could be helpful to see if we can manage to have a good result compared to google NLP API.
- [ ] Sentiment analysis. Infer the positive/negative sentiment (and, in the future, salience) of a sentence. 
- [ ] Guess the source of a post given its content. If a certain entity uses the same words or the same writing style, a neural network should in principle be able to learn this style and categorize the post. It can also be used to generate new text using the same or similar words, depending on the temperature. This task as well can be accomplished in various ways, using recurrent networks or markov chains for example. 
