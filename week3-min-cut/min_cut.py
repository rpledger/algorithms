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
	return adjacency

def remove_self_loops(super_node, non_super_node, adj):
	if super_node in adj:
		adj[:] = [a for a in adj if a != super_node]
	if non_super_node in adj:
		adj[:] = [a for a in adj if a != non_super_node]
	return adj

def edge_contraction(v, e, graph):
	super_node =  min(int(v), int(e))
	non_super_node = max(int(v), int(e))
	for adj in graph[non_super_node]:
		graph[super_node].append(adj)
	graph.pop(non_super_node)
	for vertex in graph:
		if non_super_node in graph[vertex]:
			graph[vertex] = [x if x != non_super_node else super_node for x in graph[vertex]]
	remove_self_loops(super_node, non_super_node, graph[super_node])
	return graph

def choose_random_vertex(seed, keys):
	random.seed(seed)
	r = random.randint(1, len(keys)-1)
	vertex = keys[r]
	return vertex

def choose_random_edge(seed, adj_list):
	random.seed(seed)
	edge = adj_list[random.randint(0, (len(adj_list)) - 1)]
	return edge

def minimum_cut(seed, graph):
	global count
	count+=1
	if len(graph) == 2:
		return len(graph[list(graph.keys())[0]])
	mc = 0
	# Choose random vertex
	v = choose_random_vertex(seed, graph.keys())
	# Choose random edge from that list
	e = choose_random_edge(seed, graph[v])
	# Do Edge Contraction
	graph = edge_contraction(v, e, graph)
	# Recurive call
	mc = minimum_cut(seed, graph)
	#print graph
	return mc

if __name__ == '__main__':
	graph = read_input_data('min_cut_data.txt', 200)
	print "MIN CUT: {}".format(minimum_cut(11, graph))