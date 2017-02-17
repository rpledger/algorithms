import argparse

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


samples, file = get_args()


print "\nReading {} inputs from file {}\n".format(samples, file.name)
arr[samples] = []
for s in range(0, samples):
	try:
		number = int(file.readline())

	except (TypeError, ValueError):
		print "Sample {} is not an integer".format(s)
