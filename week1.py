while True:
	try: 
		samples = int(raw_input("How many inputs?: "))
		break
	except ValueError:
		print("Oops! That was not a valid number. Try again...")

file_name = input("File name?: ")
f = open(file_name, 'r')
if not f:
	print "Not a readable file..."
	exit

print "Reading {} inputs from file {}".format(samples, file_name)

