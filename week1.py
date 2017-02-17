import argparse
import numpy as np

def get_args():
	parser = argparse.ArgumentParser(description='Find inversion in a set of samples from a file')
	parser.add_argument('samples', metavar='SAMPLES', type=int,
						help='number of input samples from file')
	parser.add_argument('file', metavar='FILE', type=argparse.FileType('r'),
						help='file to read samples from')

	args = parser.parse_args()
	samples = args.samples
	file = args.file
	return samples, file

def read_samples(samples, file):
	print "\nReading {} inputs from file {}\n".format(samples, file.name)
	A = []
	for s in range(0, samples):
		try:
			number = int(file.readline())
			A= np.append(A, number)
		except (ValueError):
			print "Sample {} is not an integer".format(s)

	return A

def calculate_inversions(s, A):
	# Base Case
	if s <= 1:
		return A

	# Divide
	B, C = np.array_split(A, 2)

	# Conquer
	
	# Merge

samples, file = get_args()
A = read_samples(samples, file)
print "Input array: {}".format(A)
inversions = calculate_inversions(samples, A)

