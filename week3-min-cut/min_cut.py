import random

count = 0

def read_input_data(file, size):
	adjacency = {}
	line_count = size
	with open(file, 'r') as f:
		for line in f:
			adj = line.split()
			adj = [int(a) for a in adj]
			adjacency[adj[0]] = adj[1:]
			line_count -= 1
			if line_count == 0:
				break
	#print len(adjacency)
	return adjacency

def remove_self_loops(super_node, non_super_node, adj):
	#print adj
	if super_node in adj:
		adj.remove(super_node)
	if non_super_node in adj:
		adj.remove(non_super_node)
	return adj

def edge_contraction(v, e, graph):
	super_node =  min(int(v), int(e))
	non_super_node = max(int(v), int(e))
	print "Super: {}, Non-Super: {}".format(super_node, non_super_node)
	for adj in graph[non_super_node]:
		graph[super_node].append(adj)
	graph.pop(non_super_node)
	for vertex in graph:
		if non_super_node in graph[vertex]:
			graph[vertex].remove(non_super_node)
	remove_self_loops(super_node, non_super_node, graph[super_node])
	print "V: {}, E: {}".format(v,e)
	print graph
	return graph

def choose_random_vertex(seed, size):
	random.seed(seed)
	vertex = random.randint(1, size)
	return vertex

def choose_random_edge(seed, adj_list):
	random.seed(seed)
	edge = adj_list[random.randint(0, (len(adj_list)) - 1)]
	return edge

def min_cut(seed, graph):
	global count
	print count
	count+=1
	if len(graph) == 2:
		return len(graph[list(graph.keys())[0]])
	mc = 0
	# Choose random vertex
	print graph
	v = choose_random_vertex(seed, len(graph))
	# Choose random edge from that list
	e = choose_random_edge(seed, graph[v])
	# Do Edge Contraction
	graph = edge_contraction(v, e, graph)
	# Recurive call
	mc = min_cut(seed, graph)
	print graph
	return mc

if __name__ == '__main__':
	graph = read_input_data('test.txt', 3)
	print min_cut(graph)