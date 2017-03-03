comparision_count = 0

def read_samples(num, file):
	f = open(file, 'r')
	print "Reading {} inputs from file {}".format(num, file)
	A =[]
	for s in range(0,num):
		try:
			sample = int(f.readline())
			A.append(sample)
		except(ValueError):
			print "Sample ({}) not an interger".format(sample)
			f.close()
			exit()
	f.close()
	return A

def choose_pivot(A, l, r, method):
	if method == 0:
		p = 0
	elif method == 1:
		p = r - 1
	elif method == 2: 
		p = 0
	#p = 0
	if p != 0:
		A[l], A[p] = A[p], A[l]
	return A, p

def partition(A, l, r):
	p = A[l]
	i = l + 1
	for j in range (l+1, r):
		if A[j] < p:
			A[i], A[j] = A[j], A[i]
			i = i + 1
	A[l], A[i-1] = A[i-1], A[l]
	pi = i-1
	return A, pi

def quick_sort(A, l, r, method):
	global comparision_count
	comparision_count = comparision_count + r - l - 1

	p = 0
	if (r-l) == 1:
		return A
	A, p = choose_pivot(A, l, r, method)
	A, p = partition(A, l, r)
	if p - l > 0:
		A = quick_sort(A, l, p, method)
	if r - (p + 1) > 0:
		A = quick_sort(A, p+1, r, method)
	return A


#file = "QuickSort.txt"
#num = int(raw_input("How many samples?: "))
#A = read_samples(num, file)
##print "Input Array: {}".format(A)
#A_sorted = quick_sort(A, 0, num)
##print "Array sorted: {}".format(A_sorted)
#print "Number of Comparisions: {}".format(comparision_count)