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

#def edge_contraction(e):

def choose_random_vertex(seed, size):
	random.seed(seed)
	vertex = random.randint(0, (size - 1))
	return vertex



#def min_cut():
	# Choose random vertex
	# Choose random edge from that list
	# Do Edge Contraction

if __name__ == '__main__':
	graph = read_input_data('test.txt', 3)
	#min_cut(graph)