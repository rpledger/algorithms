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
#while True:
#	try: 
#		samples = int(raw_input("How many inputs?: "))
#		break
#	except ValueError:
#		print("Oops! That was not a valid number. Try again...")
#
#file_name = input("File name?: ")
#f = open(file_name, 'r')

print "Reading {} inputs from file {}".format(samples, file.name)

