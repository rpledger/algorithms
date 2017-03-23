import random

def read_input_data(file, size):
	adjacency = {}
	line_count = size
	with open(file, 'r') as f:
		for line in f:
			adj = line.split()
			adjacency[adj[0]] = adj[1:]
			line_count -= 1
			if line_count == 0:
				break
	#print len(adjacency)
	return adjacency

#def remove_self_loops():

def edge_contraction(v, e, graph):
	super_node = min(v, e)
	non_super_node = max(v,e)
	for adj in graph[non_super_node]:
		graph[super_node].append(adj)
	graph.pop(non_super_node)
	return graph

def choose_random_vertex(seed, size):
	random.seed(seed)
	vertex = random.randint(1, size)
	return str(vertex)

def choose_random_edge(seed, adj_list):
	random.seed(seed)
	edge = adj_list[random.randint(0, (len(adj_list)) - 1)]
	return edge

def min_cut(seed, graph):
	# Choose random vertex
	v = choose_random_vertex(seed, len(graph))
	# Choose random edge from that list
	e = choose_random_edge(seed, graph[v])
	# Do Edge Contraction
	graph = edge_contraction(v, e, graph)
	# Remove self loops

if __name__ == '__main__':
	graph = read_input_data('test.txt', 3)
	#min_cut(graph)