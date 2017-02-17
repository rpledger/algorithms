import argparse

parser = argparse.ArgumentParser(description='Find inversion in a set of samples from a file')
parser.add_argument('samples', metavar='SAMPLES', type=int, nargs=1,
					help='number of input samples from file')
parser.add_argument('file', metavar='FILE', type=argparse.FileType('r'), nargs=1,
					help='file to read samples from')

args = parser.parse_args()
print args
#while True:
#	try: 
#		samples = int(raw_input("How many inputs?: "))
#		break
#	except ValueError:
#		print("Oops! That was not a valid number. Try again...")
#
file_name = input("File name?: ")
f = open(file_name, 'r')
if not f:
	print "Not a readable file..."
	exit

print "Reading {} inputs from file {}".format(samples, file_name)

