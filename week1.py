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

def merge_and_calc_split_inversions(B, C, s):
	i = 0
	j = 0
	D = []
	for k in range(0,s):
		if i >= np.size(B):
			D = np.insert(D, k, C[j])
			j+=1
		elif j >= np.size(C):
			D =np.insert(D, k, B[i])
			i+=1 
		elif B[i] < C[j]:
			D = np.insert(D, k, B[i])
			i+=1
		elif C[j] < B[i]:
			D = np.insert(D, k, C[j])
			j+=1
	return D, 0

def sort_and_calc_inversions(A, s):
	# Base Case
	if s == 1:
		return A, 0
	else:
		# Divide
		B, C = np.array_split(A, 2)

		# Conquer
		B,x = sort_and_calc_inversions(B, s/2)
		C, y = sort_and_calc_inversions(C, s/2)

		# Merge
		D, z= merge_and_calc_split_inversions(B, C, s)

		return D, x+y+z

samples, file = get_args()
A = read_samples(samples, file)
print "Input array: {}".format(A)
A_sort, inversions = sort_and_calc_inversions(A, samples)
print A_sort

