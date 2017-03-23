import unittest

import min_cut

class TestMinCutMethods(unittest.TestCase):

	def test_read_input_data(self):
		graph1 = {
			'1': ['2','3'],
			'2': ['1'],
			'3': ['1']
		}
		self.assertEqual(graph1, min_cut.read_input_data('test.txt', 3))

	def test_read_input_data_bad_num(self):
		graph2 = {
			'1': ['2','3'],
			'2': ['1'],
		}
		self.assertEqual(graph2, min_cut.read_input_data('test.txt', 2))

	def test_random_vertex_seed_0(self):
		graph = min_cut.read_input_data('test.txt', 3)
		self.assertEqual(2, min_cut.choose_random_vertex(0, len(graph)))

	def test_random_vertex_seed_1(self):
		graph = min_cut.read_input_data('test.txt', 3)
		self.assertEqual(0, min_cut.choose_random_vertex(1, len(graph)))

	def test_random_vertex_seed_1(self):
		graph = min_cut.read_input_data('test.txt', 3)
		self.assertEqual(0, min_cut.choose_random_vertex(1, len(graph)))

if __name__ == '__main__':
    unittest.main()