from objects import *
import networkx as nx
print "reading in b"
b = nx.read_gpickle('first_bipartite_graph.gpickle')
print "done reading in b"
print "looking for giel"
my_node = None
for node in b.nodes():
	if node.id == 16538689:
		my_node = node
print "making rec"
recommender = Soundcloud_recommender(b, my_node)
print "done making rec"
print "gathering data..."
data = recommender.gather_data('sc_ratings', recommender.user_partition_index^1)


