import unittest

import min_cut

class TestMinCutMethods(unittest.TestCase):

	def test_read_input_data(self):
		graph1 = {
			1: [2,3],
			2: [1],
			3: [1]
		}
		self.assertEqual(graph1, min_cut.read_input_data('test.txt', 3))

	def test_read_input_data_bad_num(self):
		graph2 = {
			1: [2,3],
			2: [1],
		}
		self.assertEqual(graph2, min_cut.read_input_data('test.txt', 2))

	# def test2_read_input(self):
	# 	graph2 = {
	# 		1:	[2, 3, 10],
	# 		2:	[1],
	# 		3:	[1],
	# 		4:	[5, 6, 8, 10],
	# 		5:	[4, 6],
	# 		6:	[4, 5, 7],
	# 		7:	[6, 9],
	# 		8:	[4, 9, 10],
	# 		9:	[7, 8],
	# 		10:	[1, 4, 8]
	# 	}
	# 	self.assertEqual(graph2, min_cut.read_input_data('test2.txt', 10))

	def test_random_vertex_seed_0(self):
		graph = min_cut.read_input_data('test.txt', 3)
		self.assertEqual(3, min_cut.choose_random_vertex(0, graph.keys()))

	def test_random_vertex_seed_1(self):
		graph = min_cut.read_input_data('test.txt', 3)
		self.assertEqual(2, min_cut.choose_random_vertex(1, graph.keys()))

	def test_choose_random_edge_seed_0(self):
		graph = min_cut.read_input_data('test.txt', 3)
		v = min_cut.choose_random_vertex(0, graph.keys())
		print graph
		self.assertEqual(1, min_cut.choose_random_edge(0, graph[v]))

	def test_choose_random_edge_seed_1(self):
		graph = min_cut.read_input_data('test.txt', 3)
		v = min_cut.choose_random_vertex(1, graph.keys())
		print graph
		self.assertEqual(1, min_cut.choose_random_edge(1, graph[v]))

	def test_choose_random_edge_seed_2(self):
		graph = min_cut.read_input_data('test.txt', 3)
		v = min_cut.choose_random_vertex(2, graph.keys())
		print graph
		self.assertEqual(1, min_cut.choose_random_edge(2, graph[v]))

	def test2_choose_random_edge_seed_0(self):
		graph = min_cut.read_input_data('test2.txt', 10)
		v = min_cut.choose_random_vertex(2, graph.keys())
		print graph
		self.assertEqual(8, min_cut.choose_random_edge(2, graph[v]))

	def test_edge_contraction_seed_0(self):
		graph_test = {
			1: [2],
			2: [1]
		}
		graph = min_cut.read_input_data('test.txt', 3)
		v = min_cut.choose_random_vertex(0, graph.keys())
		e = min_cut.choose_random_edge(0, graph[v])
		self.assertEqual(graph_test, min_cut.edge_contraction(v, e, graph))


	# def test2_edge_contraction_seed_0(self):
	# 	graph_test = {
	# 		1:	[2, 3, 10],
	# 		2:	[1],
	# 		3:	[1],
	# 		4:	[5, 6, 8, 10],
	# 		5:	[4, 6],
	# 		6:	[4, 5, 7],
	# 		7:	[6],
	# 		8:	[4, 10, 7],
	# 		10:	[1, 4, 8]
	# 	}
	# 	graph = min_cut.read_input_data('test2.txt', 10)
	# 	v = min_cut.choose_random_vertex(0, graph.keys())
	# 	e = min_cut.choose_random_edge(0, graph[v])
	# 	self.assertEqual(graph_test, min_cut.edge_contraction(v, e, graph))

	def test_edge_contraction_seed_1(self):
		graph_test = {
			1: [3],
			3: [1]
		}
		graph = min_cut.read_input_data('test.txt', 3)
		v = min_cut.choose_random_vertex(1, graph.keys())
		e = min_cut.choose_random_edge(1, graph[v])
		self.assertEqual(graph_test, min_cut.edge_contraction(v, e, graph))

	def test_remove_self_loop(self):
		graph = [1, 2, 1]
		graph_test = [2]
		#graph = min_cut.read_input_data('test.txt', 3)
		#v = min_cut.choose_random_vertex(1, len(graph))
		#e = min_cut.choose_random_edge(1, graph[str(v)])
		self.assertEqual(graph_test, min_cut.remove_self_loops(1, 3, graph))

	def test_min_cut_seed_0(self):
		graph = min_cut.read_input_data('test.txt', 3)
		self.assertEqual(1, min_cut.minimum_cut(0, graph))

	def test_min_cut_seed_1(self):
		graph = min_cut.read_input_data('test.txt', 3)
		self.assertEqual(1, min_cut.minimum_cut(1, graph))

	def test2_min_cut_seed_0(self):
		graph = min_cut.read_input_data('test2.txt', 10)
		self.assertEqual(2, min_cut.minimum_cut(0, graph))

if __name__ == '__main__':
    unittest.main()