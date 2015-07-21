def make_link(G, node1, node2):
	if node1 not in G:
		G[node1] = {}
	(G[node1])[node2] = 1
	if node2 not in G:
		G[node2] = {}
	(G[node2])[node1] = 1
	return G

a_ring  = {}

n = 5

for i in range (n):
	make_link(a_ring, i, (i+1)%n)

print len(a_ring)

print sum([len(a_ring[node]) for node in a_ring.keys()])/2

print a_ring
